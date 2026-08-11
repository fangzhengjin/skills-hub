#!/usr/bin/env python3
"""将配置中的独立 Skill 仓库同步为本仓库内的真实文件。"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "skills.json"
README_PATH = ROOT / "README.md"
SKILLS_PATH = ROOT / "skills"
START_MARKER = "<!-- skills:start -->"
END_MARKER = "<!-- skills:end -->"
NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
UTC_PLUS_8 = timezone(timedelta(hours=8))


def _load_sources():
    data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    sources = data.get("skills")
    if not isinstance(sources, list) or not sources:
        raise ValueError("skills.json 中的 skills 必须是非空数组")

    normalized = []
    names = set()
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError("每个 Skill 配置必须是对象")

        name = source.get("name")
        category = source.get("category")
        repository = source.get("repository")
        description = source.get("description")
        source_path = source.get("path", ".")
        if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
            raise ValueError(f"无效的 Skill 目录名：{name!r}")
        if name in names:
            raise ValueError(f"重复的 Skill 目录名：{name}")
        if not isinstance(category, str) or not category.strip():
            raise ValueError(f"Skill {name} 缺少分类")
        if not isinstance(repository, str) or not _is_github_repository(repository):
            raise ValueError(f"无效的 GitHub 仓库地址：{repository!r}")
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"Skill {name} 缺少用途说明")
        if not _is_safe_source_path(source_path):
            raise ValueError(f"Skill {name} 的仓库内路径无效：{source_path!r}")

        names.add(name)
        normalized.append(
            {
                "name": name,
                "category": category.strip(),
                "repository": repository.rstrip("/"),
                "path": str(Path(source_path)),
                "description": description.strip(),
            }
        )

    return normalized


def _is_github_repository(repository):
    parsed = urlsplit(repository)
    parts = [part for part in parsed.path.split("/") if part]
    return (
        parsed.scheme == "https"
        and parsed.netloc == "github.com"
        and len(parts) == 2
        and not parsed.query
        and not parsed.fragment
    )


def _is_safe_source_path(source_path):
    return (
        isinstance(source_path, str)
        and bool(source_path)
        and not Path(source_path).is_absolute()
        and ".." not in Path(source_path).parts
    )


def _load_update_times(readme):
    if START_MARKER not in readme or END_MARKER not in readme:
        return {}

    _, marked = readme.split(START_MARKER, 1)
    catalog, _ = marked.split(END_MARKER, 1)
    update_times = {}
    current_name = None
    for line in catalog.splitlines():
        match = re.search(r'<a href="skills/([^"]+)">', line)
        if match:
            current_name = match.group(1)
            continue

        match = re.search(
            r"同步时间：? ?([^<]+?)(?: · 来源：|</(?:sub|small)>)", line
        )
        if match and current_name:
            updated_at = match.group(1).strip()
            if updated_at != "—":
                update_times[current_name] = updated_at
            current_name = None
            continue

        # 兼容切换为 HTML 清单前的 README，避免迁移时丢失已有同步时间。
        match = re.match(r"^\| `([^`]+)` \|", line)
        if match:
            updated_at = line.rsplit("|", 2)[1].strip()
            if updated_at != "—":
                update_times[match.group(1)] = updated_at
    return update_times


def _render_readme(readme, sources, update_times):
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise ValueError("README.md 必须各包含一个技能清单起止标记")

    categories = {}
    for source in sources:
        categories.setdefault(source["category"], []).append(source)

    rows = []
    for category, category_sources in categories.items():
        if rows:
            rows.append("")
        rows.append(f"<h3>{escape(category)}</h3>")
        rows.append("<ul>")
        for source in category_sources:
            repository = source["repository"]
            link = repository[:-4] if repository.endswith(".git") else repository
            label = urlsplit(link).path.strip("/")
            if source["path"] != ".":
                link = f"{link}/tree/HEAD/{source['path']}"
            name = source["name"]
            description = escape(source["description"].replace("\n", " "))
            updated_at = escape(update_times.get(name, "—"))
            rows.extend(
                [
                    "  <li>",
                    f'    <a href="skills/{name}"><strong>{name}</strong></a><br>',
                    f"    {description}<br>",
                    f"    <sub>同步时间：{updated_at} · 来源："
                    f'<a href="{escape(link, quote=True)}">{escape(label)}</a></sub>',
                    "  </li>",
                ]
            )
        rows.append("</ul>")

    before, marked = readme.split(START_MARKER)
    _, after = marked.split(END_MARKER)
    catalog = "\n".join(rows)
    return f"{before}{START_MARKER}\n{catalog}\n{END_MARKER}{after}"


def _clone_sources(sources, temporary_root, current_skills):
    repositories = temporary_root / "repositories"
    staged_skills = temporary_root / "skills"
    repositories.mkdir()
    staged_skills.mkdir()

    clones = {}
    successful_names = set()
    for index, repository in enumerate(
        dict.fromkeys(source["repository"] for source in sources)
    ):
        clone_path = repositories / str(index)
        try:
            subprocess.run(
                [
                    "git",
                    "clone",
                    "--depth",
                    "1",
                    repository,
                    str(clone_path),
                ],
                check=True,
            )
        except subprocess.CalledProcessError:
            continue
        clones[repository] = clone_path

    for source in sources:
        clone_path = clones.get(source["repository"])
        source_path = clone_path / source["path"] if clone_path else None
        skill_file = source_path / "SKILL.md" if source_path else None
        target_path = staged_skills / source["name"]
        if skill_file and skill_file.is_file() and not skill_file.is_symlink():
            shutil.copytree(
                source_path,
                target_path,
                ignore=shutil.ignore_patterns(".git"),
                symlinks=True,
            )
            # 子目录未必自带许可证，复制仓库根许可证以保留上游再分发声明。
            license_path = clone_path / "LICENSE"
            if (
                source["path"] != "."
                and license_path.is_file()
                and not (target_path / "LICENSE").exists()
            ):
                shutil.copy2(license_path, target_path / "LICENSE")
            successful_names.add(source["name"])
            continue

        previous_path = current_skills / source["name"]
        if previous_path.is_dir():
            shutil.copytree(previous_path, target_path, symlinks=True)
            result = "已保留上次成功同步的版本"
        else:
            result = "没有可保留的旧版本，已跳过"
        reason = "仓库克隆失败" if clone_path is None else "上游缺少真实的 SKILL.md 文件"
        print(f"警告：{source['name']} {reason}，{result}", file=sys.stderr)

    return staged_skills, successful_names


def _find_changed_skills(skill_names):
    changed_names = set()
    for name in skill_names:
        skill_path = SKILLS_PATH.relative_to(ROOT) / name
        result = subprocess.run(
            ["git", "status", "--porcelain", "--", str(skill_path)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        if result.stdout:
            changed_names.add(name)
    return changed_names


def _replace_skills(staged_skills):
    # 完成新旧版本组装后再整体替换，避免留下半成品目录。
    if SKILLS_PATH.exists():
        shutil.rmtree(SKILLS_PATH)
    staged_skills.replace(SKILLS_PATH)


def _replace_selected_skills(staged_skills, sources, current_skills):
    """只替换指定 Skill，保留当前目录中的其他内容。"""
    current_skills.mkdir(parents=True, exist_ok=True)
    for source in sources:
        staged_path = staged_skills / source["name"]
        if not staged_path.exists():
            continue
        target_path = current_skills / source["name"]
        if target_path.exists():
            shutil.rmtree(target_path)
        staged_path.replace(target_path)


def _self_check():
    sources = [
        {
            "name": "example-skill",
            "category": "示例分类",
            "repository": "https://github.com/example/example-skill",
            "path": "skills/example-skill",
            "description": "示例 | 用途",
        }
    ]
    readme = f"before\n{START_MARKER}\nold\n{END_MARKER}\nafter\n"
    updated_at = "2026-08-09 12:00"
    rendered = _render_readme(readme, sources, {"example-skill": updated_at})
    assert _is_safe_source_path("skills/example-skill")
    assert not _is_safe_source_path("../example-skill")
    assert _load_update_times(rendered) == {"example-skill": updated_at}
    assert "<h3>示例分类</h3>" in rendered
    assert "<ul>" in rendered
    assert "<li>" in rendered
    assert "<sub>" in rendered
    assert "示例 | 用途" in rendered
    assert (
        '<a href="skills/example-skill"><strong>example-skill</strong></a>'
        in rendered
    )
    assert (
        f"<sub>同步时间：{updated_at} · 来源："
        '<a href="https://github.com/example/example-skill/tree/HEAD/'
        'skills/example-skill">example/example-skill</a></sub>'
        in rendered
    )
    legacy_readme = (
        f"{START_MARKER}\n| `example-skill` | 示例 | 上游 | {updated_at} |\n"
        f"{END_MARKER}"
    )
    assert _load_update_times(legacy_readme) == {"example-skill": updated_at}

    fallback_sources = [
        {
            "name": "removed-skill",
            "repository": "https://github.com/example/removed-skill",
            "path": ".",
        },
        {
            "name": "updated-skill",
            "repository": "https://github.com/example/updated-skill",
            "path": ".",
        },
    ]
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        current_skills = root / "current"
        previous_skill = current_skills / "removed-skill"
        previous_skill.mkdir(parents=True)
        (previous_skill / "SKILL.md").write_text("previous", encoding="utf-8")
        temporary_root = root / "temporary"
        temporary_root.mkdir()

        original_run = subprocess.run

        def fake_clone(command, check):
            assert check
            clone_path = Path(command[-1])
            clone_path.mkdir()
            if command[-2].endswith("/updated-skill"):
                (clone_path / "SKILL.md").write_text("updated", encoding="utf-8")

        subprocess.run = fake_clone
        try:
            staged_skills, successful_names = _clone_sources(
                fallback_sources, temporary_root, current_skills
            )
        finally:
            subprocess.run = original_run

        assert (staged_skills / "removed-skill" / "SKILL.md").read_text(
            encoding="utf-8"
        ) == "previous"
        assert (staged_skills / "updated-skill" / "SKILL.md").read_text(
            encoding="utf-8"
        ) == "updated"
        assert successful_names == {"updated-skill"}

        selected_staging = root / "selected"
        selected_skill = selected_staging / "new-skill"
        selected_skill.mkdir(parents=True)
        (selected_skill / "SKILL.md").write_text("new", encoding="utf-8")
        _replace_selected_skills(
            selected_staging,
            [{"name": "new-skill"}],
            current_skills,
        )
        assert (current_skills / "new-skill" / "SKILL.md").read_text(
            encoding="utf-8"
        ) == "new"
        assert (current_skills / "removed-skill" / "SKILL.md").read_text(
            encoding="utf-8"
        ) == "previous"
    print("self-check passed")


def _main(skill_name=None):
    sources = _load_sources()
    selected_sources = sources
    if skill_name:
        selected_sources = [
            source for source in sources if source["name"] == skill_name
        ]
        if not selected_sources:
            raise ValueError(f"skills.json 中不存在 Skill：{skill_name}")
    previous_readme = README_PATH.read_text(encoding="utf-8")
    update_times = _load_update_times(previous_readme)

    with tempfile.TemporaryDirectory(prefix=".skills-sync-", dir=ROOT) as directory:
        staged_skills, successful_names = _clone_sources(
            selected_sources, Path(directory), SKILLS_PATH
        )
        if skill_name:
            _replace_selected_skills(staged_skills, selected_sources, SKILLS_PATH)
        else:
            _replace_skills(staged_skills)

    changed_names = _find_changed_skills(successful_names)
    if changed_names:
        updated_at = datetime.now(UTC_PLUS_8).strftime("%Y-%m-%d %H:%M")
        for name in changed_names:
            update_times[name] = updated_at

    readme = _render_readme(previous_readme, sources, update_times)
    README_PATH.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-check"]:
        _self_check()
    elif len(sys.argv) == 3 and sys.argv[1] == "--skill":
        _main(sys.argv[2])
    elif sys.argv[1:]:
        raise SystemExit("用法：sync_skills.py [--self-check | --skill NAME]")
    else:
        _main()
