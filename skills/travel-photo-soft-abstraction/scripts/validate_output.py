#!/usr/bin/env python3
"""Machine-check objective layout properties of a generated artwork."""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageOps, ImageStat
except ImportError as exc:
    raise SystemExit("Pillow is required: install it with `python -m pip install Pillow`") from exc


def mean_rgb(image: Image.Image) -> tuple[float, float, float]:
    return tuple(ImageStat.Stat(image.convert("RGB")).mean)


def background_uniformity(image: Image.Image) -> tuple[bool, list[list[float]], float]:
    """Sample empty-field zones while avoiding the motif and archive microtype."""
    width, height = image.size
    sample_centers = (
        (0.12, 0.18), (0.50, 0.18),
        (0.12, 0.48), (0.88, 0.48),
        (0.50, 0.88), (0.88, 0.88),
    )
    half_w = max(2, round(width * 0.018))
    half_h = max(2, round(height * 0.018))
    samples: list[tuple[float, float, float]] = []
    for x_fraction, y_fraction in sample_centers:
        x = round(width * x_fraction)
        y = round(height * y_fraction)
        patch = image.crop((x - half_w, y - half_h, x + half_w, y + half_h))
        samples.append(mean_rgb(patch))
    channel_span = max(
        max(sample[channel] for sample in samples) - min(sample[channel] for sample in samples)
        for channel in range(3)
    )
    return channel_span <= 4.0, [[round(value, 1) for value in sample] for sample in samples], channel_span


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--original", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    with Image.open(args.output) as opened:
        image = opened.convert("RGB")
    width, height = image.size
    ratio = width / height

    source = None
    if args.original:
        with Image.open(args.original) as opened:
            source = ImageOps.exif_transpose(opened).convert("RGB")
    if not source:
        raise SystemExit("--original is required; delivery validation cannot infer photo integrity")
    split = source.height
    split_fraction = split / height
    lower = image.crop((0, split, width, height))
    panel_larger = height - split > split
    panel_ratio_ok = 1.10 <= (height - split) / split <= 1.60
    native_dimensions = width == source.width and height > source.height
    lower_mean = mean_rgb(lower)
    neutral_spread = max(lower_mean) - min(lower_mean)
    lower_brightness = statistics.fmean(lower_mean)
    split_ok = panel_larger
    neutral_ok = lower_brightness >= 205 and neutral_spread <= 25
    uniform_background_ok, background_samples, background_channel_span = background_uniformity(lower)
    photo_match = None
    actual = image.crop((0, 0, source.width, source.height))
    photo_match = native_dimensions and ImageChops.difference(actual, source).getbbox() is None

    report = {
        "output": str(args.output.resolve()),
        "dimensions": [width, height],
        "aspect_ratio": round(ratio, 4),
        "layout": "upper-lower",
        "estimated_photo_fraction": round(split_fraction, 4),
        "lower_panel_mean_rgb": [round(value, 1) for value in lower_mean],
        "lower_background_sample_rgb": background_samples,
        "lower_background_max_channel_span": round(background_channel_span, 2),
        "checks": {
            "lower_panel_larger_than_full_frame_photo": split_ok,
            "lower_panel_height_ratio_is_1.10_to_1.60": panel_ratio_ok,
            "lower_panel_bright_and_neutral": neutral_ok,
            "lower_panel_background_is_uniform": uniform_background_ok,
            "photo_keeps_native_pixel_dimensions": native_dimensions,
        },
        "manual_checks_required": [
            "upper photograph is the locked current user upload and remains pixel-identical",
            "motif maps to named source facts and uses 65-85% negative space",
            "compose_artwork.py added exact NO. 00X at upper-right",
            "compose_artwork.py added only the exact date and phrase elsewhere",
            "no new grain, haze, tonal drift, or invented content",
        ],
    }
    if photo_match is not None:
        report["checks"]["photo_pixels_exactly_match_original"] = photo_match
    else:
        report["manual_checks_required"].append("rerun with --original for deterministic photo comparison")
    passed = all(report["checks"].values())
    report["machine_result"] = "PASS" if passed else "FAIL"
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else report)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
