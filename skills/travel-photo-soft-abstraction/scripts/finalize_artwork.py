#!/usr/bin/env python3
"""Compose and validate the only deliverable artwork in one fail-closed command."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("original", type=Path)
    parser.add_argument("abstract_panel", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--number", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--phrase", required=True)
    parser.add_argument("--font", type=Path)
    args = parser.parse_args()

    original = args.original.resolve()
    panel = args.abstract_panel.resolve()
    output = args.output.resolve()
    if not original.is_file():
        raise SystemExit(f"Original photograph not found: {original}")
    if not panel.is_file():
        raise SystemExit(f"Abstract panel not found: {panel}")
    if output in (original, panel):
        raise SystemExit("Output must be a new file; never overwrite an input")

    scripts = Path(__file__).resolve().parent
    compose = [
        sys.executable, str(scripts / "compose_artwork.py"),
        str(original), str(panel), str(output),
        "--number", args.number, "--date", args.date, "--phrase", args.phrase,
    ]
    if args.font:
        compose.extend(("--font", str(args.font.resolve())))

    try:
        subprocess.run(compose, check=True)
        subprocess.run(
            [sys.executable, str(scripts / "validate_output.py"), str(output),
             "--original", str(original)],
            check=True,
        )
    except (subprocess.CalledProcessError, OSError):
        if output.is_file():
            output.unlink()
        raise SystemExit("FINALIZATION FAILED: invalid output removed; deliver no artwork")

    print(f"DELIVERY PASS: {output}")
    print("The locked user-uploaded photograph is present and pixel-verified. Return this file only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
