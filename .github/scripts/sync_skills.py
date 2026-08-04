#!/usr/bin/env python3
"""将配置中的独立 Skill 仓库同步为本仓库内的真实文件。"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "skills.json"
README_PATH = ROOT / "README.md"
SKILLS_PATH = ROOT / "skills"
START_MARKER = "<!-- skills:start -->"
END_MARKER = "<!-- skills:end -->"
NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


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
        repository = source.get("repository")
        description = source.get("description")
        source_path = source.get("path", ".")
        if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
            raise ValueError(f"无效的 Skill 目录名：{name!r}")
        if name in names:
            raise ValueError(f"重复的 Skill 目录名：{name}")
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


def _render_readme(readme, sources):
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise ValueError("README.md 必须各包含一个技能清单起止标记")

    rows = ["| Skill | 用途 | 上游仓库 |", "|---|---|---|"]
    for source in sources:
        repository = source["repository"]
        link = repository[:-4] if repository.endswith(".git") else repository
        label = urlsplit(link).path.strip("/")
        if source["path"] != ".":
            link = f"{link}/tree/HEAD/{source['path']}"
            label = f"{label}/{source['path']}"
        description = source["description"].replace("\n", " ").replace("|", "\\|")
        rows.append(
            f"| `{source['name']}` | {description} | [{label}]({link}) |"
        )

    before, marked = readme.split(START_MARKER)
    _, after = marked.split(END_MARKER)
    table = "\n".join(rows)
    return f"{before}{START_MARKER}\n{table}\n{END_MARKER}{after}"


def _clone_sources(sources, temporary_root):
    repositories = temporary_root / "repositories"
    staged_skills = temporary_root / "skills"
    repositories.mkdir()
    staged_skills.mkdir()

    clones = {}
    for index, repository in enumerate(
        dict.fromkeys(source["repository"] for source in sources)
    ):
        clone_path = repositories / str(index)
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
        clones[repository] = clone_path

    for source in sources:
        clone_path = clones[source["repository"]]
        source_path = clone_path / source["path"]
        skill_file = source_path / "SKILL.md"
        if not skill_file.is_file() or skill_file.is_symlink():
            raise RuntimeError(
                f"{source['repository']} 的 {source['path']} 目录缺少真实的 SKILL.md 文件"
            )

        target_path = staged_skills / source["name"]
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

    return staged_skills


def _replace_skills(staged_skills):
    # 所有上游均成功克隆后才替换，避免一次网络失败清空上次同步结果。
    if SKILLS_PATH.exists():
        shutil.rmtree(SKILLS_PATH)
    staged_skills.replace(SKILLS_PATH)


def _self_check():
    sources = [
        {
            "name": "example-skill",
            "repository": "https://github.com/example/example-skill",
            "path": "skills/example-skill",
            "description": "示例 | 用途",
        }
    ]
    readme = f"before\n{START_MARKER}\nold\n{END_MARKER}\nafter\n"
    rendered = _render_readme(readme, sources)
    assert _is_safe_source_path("skills/example-skill")
    assert not _is_safe_source_path("../example-skill")
    assert "示例 \\| 用途" in rendered
    assert (
        "| `example-skill` | 示例 \\| 用途 | "
        "[example/example-skill/skills/example-skill]"
        "(https://github.com/example/example-skill/tree/HEAD/skills/example-skill) |"
        in rendered
    )
    print("self-check passed")


def _main():
    sources = _load_sources()
    readme = _render_readme(README_PATH.read_text(encoding="utf-8"), sources)

    with tempfile.TemporaryDirectory(prefix=".skills-sync-", dir=ROOT) as directory:
        staged_skills = _clone_sources(sources, Path(directory))
        _replace_skills(staged_skills)

    README_PATH.write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-check"]:
        _self_check()
    elif sys.argv[1:]:
        raise SystemExit("用法：sync_skills.py [--self-check]")
    else:
        _main()
