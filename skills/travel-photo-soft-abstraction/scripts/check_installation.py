#!/usr/bin/env python3
"""Fail fast when the distributed skill is incomplete."""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED = (
    "SKILL.md",
    "references/analysis-method.md",
    "references/structural-reference-index.md",
    "references/style-guide.md",
    "references/run-log-template.md",
    "scripts/compose_artwork.py",
    "scripts/finalize_artwork.py",
    "scripts/validate_output.py",
)

STRUCTURAL_REFS = tuple(
    f"assets/style-references/memory-reference-{index:03d}.png" for index in range(1, 20)
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = Path(args.skill_dir).resolve()

    missing = [name for name in REQUIRED if not (root / name).is_file()]
    missing_refs = [name for name in STRUCTURAL_REFS if not (root / name).is_file()]

    if missing or missing_refs:
        if missing:
            print("FAIL missing required files: " + ", ".join(missing))
        if missing_refs:
            print("FAIL missing structural references: " + ", ".join(missing_refs))
        return 1

    print(f"PASS complete installation with {len(STRUCTURAL_REFS)} structural references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
