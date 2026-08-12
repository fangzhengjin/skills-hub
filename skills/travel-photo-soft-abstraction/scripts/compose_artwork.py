#!/usr/bin/env python3
"""Place an untouched, 1:1 source photo above a generated CLEAN abstraction."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError as exc:
    raise SystemExit("Pillow is required: install it with `python -m pip install Pillow`") from exc


NUMBER_RE = re.compile(r"^NO\. \d{3}$")
DATE_RE = re.compile(r"^\d{2} [A-Z]{3} \d{4}$")
PHRASE_RE = re.compile(r"^[A-Z0-9]+(?: [A-Z0-9]+){0,2}$")


def load_font(size: int, explicit: Path | None) -> ImageFont.ImageFont:
    candidates = [
        explicit,
        Path("C:/Windows/Fonts/consola.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"),
        Path("/System/Library/Fonts/Menlo.ttc"),
    ]
    for candidate in candidates:
        if candidate and candidate.is_file():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default(size=size)


def resize_panel_full_frame(image: Image.Image, width: int) -> Image.Image:
    image = ImageOps.exif_transpose(image).convert("RGB")
    height = round(image.height * width / image.width)
    return image.resize((width, height), Image.Resampling.LANCZOS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("original", type=Path)
    parser.add_argument("lower_panel", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--number", required=True, help='Exact form: "NO. 001"')
    parser.add_argument("--date", required=True, help='Exact form: "02 AUG 2026"')
    parser.add_argument("--phrase", required=True, help="One to three uppercase words")
    parser.add_argument("--font", type=Path)
    args = parser.parse_args()

    if not NUMBER_RE.fullmatch(args.number):
        raise SystemExit('Invalid --number; expected exact form "NO. 001"')
    if not DATE_RE.fullmatch(args.date):
        raise SystemExit('Invalid --date; expected exact form "02 AUG 2026"')
    if not PHRASE_RE.fullmatch(args.phrase):
        raise SystemExit("Invalid --phrase; expected one to three uppercase words")
    with Image.open(args.original) as opened:
        source = ImageOps.exif_transpose(opened).convert("RGB")
    with Image.open(args.lower_panel) as opened:
        panel = ImageOps.exif_transpose(opened).convert("RGB")

    # The photograph is pasted at native pixel dimensions. Never resize or crop it.
    photo = source
    width = photo.width
    photo_height = photo.height
    lower = resize_panel_full_frame(panel, width)
    lower_height = lower.height
    lower_ratio = lower_height / photo_height
    if not 1.10 <= lower_ratio <= 1.60:
        raise SystemExit(
            f"Abstract panel aspect ratio is incompatible: displayed height/photo height={lower_ratio:.3f}; "
            "regenerate the complete panel at a ratio yielding 1.10-1.60 without cropping"
        )
    height = photo_height + lower_height
    canvas = Image.new("RGB", (width, height), "white")
    canvas.paste(photo, (0, 0))
    canvas.paste(lower, (0, photo_height))
    lower_origin = (0, photo_height)
    lower_size = (width, lower_height)

    draw = ImageDraw.Draw(canvas)
    base = min(width, height)
    font = load_font(max(10, round(base * 0.012)), args.font)
    color = (145, 145, 140)
    lower_x, lower_y = lower_origin
    lower_width, lower_height = lower_size
    inset_x = round(lower_width * 0.045)
    inset_y = round(lower_height * 0.055)
    draw.text((lower_x + lower_width - inset_x, lower_y + inset_y), args.number, font=font, fill=color, anchor="ra")
    archive = f"{args.date}\n{args.phrase}"
    draw.multiline_text(
        (lower_x + inset_x, lower_y + lower_height - inset_y),
        archive,
        font=font,
        fill=color,
        anchor="ld",
        spacing=max(2, round(width * 0.004)),
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)
    print(f"PASS composed {args.output.resolve()} at {width}x{height} layout=upper-lower photo=1:1 panel=full-frame")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
