---
name: photo-relic-editorial
description: "Create distinctive Photo Relic editorial artworks from user-provided photographs: preserve the real photo and pair it with a recognizable, artful abstract relic shaped like memory, modern printmaking, quiet Eastern restraint, and source-derived light. Use when the user asks to turn a photo into minimal art, photographic relic posters, abstract editorial photography, gallery-like photo posters, Douyin-ready art series covers, graphic photo abstraction, afterimage compositions, or similar visual treatments while keeping the original photograph truthful."
---

# Photo Relic Editorial

## Overview

Use this skill to transform a user-provided photograph into a vertical editorial artwork with a consistent signature: the real photograph above, and a "Photo Relic" below. The relic is not a literal illustration, decorative poster, or vague haze. It is a compressed visual memory of the photograph: a few precise marks that preserve the subject's identity, light, weight, and emotional temperature.

The aesthetic should feel like real photography meeting a modern paper print: quiet, restrained, source-derived, recognizable, and artful enough to become a repeatable visual series.

This is a creative image-generation skill. When producing the final image, use the image generation/editing tool with the user's photo as the reference image.

## Workflow

1. Inspect the supplied photograph before writing the generation prompt.
2. Identify 3-5 source cues from the real image:
   - the main subject identity and the full relationship that makes it recognizable
   - the photo's emotional core, reduced to a short concept such as "held dusk", "falling sky", "quiet order", "wet neon", or "alone in the plaza"
   - dominant colors plus one possible signature accent: vermilion, small gold, dusk orange, or a source-specific warm light
   - strongest light or shadow direction, including large cold/warm areas
   - key structural cues: roof layers, towers, arches, windows, paths, stairs, horizon, ground, water, people scale, or silhouettes
3. Choose a compact Photo Relic recipe before prompting:
   - layout rhythm
   - relic grammar
   - mark weight
   - title mode
   - motion seed when useful for social-video follow-up
4. Read `references/afterimage-editorial-prompt.md` before composing the final image prompt.
5. Ask for the missing photo only if no usable source image is available.
6. Generate one finished vertical artwork unless the user asks for variants.
7. Use the Quality Gate before finalizing. If the result clearly fails one major gate, regenerate once with tighter constraints.

## Signature Aesthetic

Make the result feel like this:

Real photograph above. Memory print below. The lower relic should look as if time pressed the photo into a few ink marks on warm paper.

Use these signature traits consistently:

- Preserve the photographic region as truth. The user's photography is the root of the work.
- Use a warm ivory, off-white, or very quiet source-light panel for the relic area.
- Build the relic from deep blue, ink black, gray-green, stone gray, muted teal, and one small warm accent when the source supports it.
- Use one primary form plus a few support marks. Do not fill the panel.
- Make the relic recognizable at thumbnail size, but not literal enough to become a normal illustration.
- Let marks feel like modern printmaking: flat ink blocks, softened edges, small breaks, negative-space cuts, and measured irregularity.
- Keep titles small, poetic, and label-like. The image should not read as an advertisement.
- Favor a stable series identity over one-off novelty.

## Creative Rules

- Preserve the photograph's content and truth. Do not redraw, beautify, repaint, expand, hallucinate, or stylize the original photographic area.
- Let the relic come from the photo. Use its real colors, light logic, negative space, edges, subject placement, and spatial tension.
- Always create one clear primary relic shape. The viewer should sense the whole subject relationship through the simplified form.
- Keep the relic complete enough to preserve the photo's main identity. For architecture, include roof/mass, base, entrance or path, ground/horizon, and scale marks when they matter.
- Translate details into marks, not decorations: roof layers become stacked arcs; windows become sparse cuts or tiny dots; people become short vertical ticks; water becomes one or two horizontal residues; dusk becomes one small warm signal.
- Use atmosphere only as support. Light may hold the relic, but it must not replace the form.
- Prefer quiet precision over ornament. Use breathing room, one primary motif, a few supporting marks, and restrained title treatment.
- Keep the family resemblance to minimal editorial photo art, but avoid copying any specific external skill's text, layout formula, examples, or named style.
- Avoid loud gradients, commercial-poster hierarchy, heavy watercolor, fake vintage texture, stickers, collage clutter, UI overlays, platform watermarks, and decorative geometry unrelated to the photo.

## Composition Patterns

Choose one pattern based on the photograph. Do not output a panel made only of fields, lines, or swatches; the relic must have a central motif and enough surrounding structure to carry the whole photograph.

- **Paper Relic**: Use a clean ivory/off-white lower plate. Place a small-to-medium source-derived relic in the lower-middle, with generous blank space and one title.
- **Light-Pressed Relic**: Use a very restrained cold/warm light field sampled from the photo, then press a clear ink-like subject shape into it.
- **Architectural Seal**: Reduce a building or skyline into blocks, arcs, voids, base lines, and a small warm accent. Keep identity strong and ornament low.
- **Horizon Memory**: For cities, water, roads, or open landscapes, anchor the relic with one calm horizon/base mark so the form does not float.
- **Human Scale Echo**: If people matter, reduce them to small irregular vertical marks that show scale and atmosphere. Do not draw faces, limbs, or clothing detail.
- **Motion Cover Seed**: When the user wants Douyin or social-video potential, compose the still image so it can animate: photo holds, subject outline descends, relic marks assemble, title appears last.

## Recipe Selection

Pick one option from each axis before writing the image prompt. Vary the recipe when recent outputs look too similar, but keep the series identity stable.

Layout rhythm:

- **photo-over-paper**: preserved photo above, warm paper relic below; default.
- **deep-paper**: smaller photo band, larger paper field; use when the relic needs air.
- **axis-diptych**: photo and relic share a strong central axis; use for symmetrical architecture.
- **horizon-cover**: photo above, lower relic anchored by a horizon/base; use for cities, water, plazas, roads, and skylines.
- **social-cover**: readable composition for a 9:16 video cover; keep the relic and title clear on mobile.

Relic grammar:

- **ink-seal architecture**: deep block shapes, negative-space cuts, and one accent.
- **stacked-order**: arcs, bands, steps, or floors reduced into calm layers.
- **skyline-memory**: landmark plus supporting bars, horizon, sparse light marks.
- **light-relic**: subject silhouette pressed into a subdued light field.
- **edge-remnant**: a few decisive edges cluster into one recognizable motif.

Mark weight:

- **quiet ink**: medium-dark marks with softened edges; default.
- **graphic ink**: bolder flat blocks when the subject needs stronger recognition.
- **thin trace**: fine lines for cranes, railings, paths, water, or delicate edges.
- **single accent**: one warm point or short bar only, used like a signature.

Title mode:

- **small English title**: safe default for an editorial series.
- **small Chinese title**: use when the user asks for Chinese feeling or social-video resonance.
- **textless**: use when the relic is strong enough.
- **micro bilingual**: use only when explicitly requested.

Motion seed:

- **outline descent**: subject outline separates from the photo and settles into the relic panel.
- **ink assembly**: relic marks appear one by one from largest form to smallest accent.
- **light fade**: photo light fades into the lower paper field before the relic appears.
- **still only**: default unless the user asks about Douyin/video.

## Output Prompting

When invoking the image tool, include:

- the source photo must remain real and unaltered in the photographic region
- a vertical editorial artwork layout suitable for a repeatable art series
- one recognizable primary Photo Relic derived only from the source photo
- a warm paper or restrained source-light panel that supports the relic without competing with it
- modern printmaking language: flat ink blocks, soft edges, negative-space cuts, sparse lines, and one small source-derived accent when useful
- restrained typography, usually one very small title only
- exact prohibitions against rewriting, replacing, beautifying, or inventing content in the photo

Do not mention internal analysis in the final prompt. Translate the visual decision into concise production language.

## Quality Gate

Before finalizing, check the generated result:

- The photograph remains truthful and recognizable in the photo region.
- The relic is recognizable at thumbnail size.
- The relic preserves the full subject relationship, not only a decorative fragment.
- The lower panel feels like a memory print, not a normal illustration, infographic, or generic poster.
- The marks are few, deliberate, and source-derived.
- There is a stable series signature: warm paper, deep ink, one possible accent, generous blank space, quiet title.
- The result has enough artistic strangeness to feel memorable, but enough clarity to be shared quickly on mobile.
- Typography is absent or very small; it does not become the main visual.
- The palette clearly comes from the source photo.
- There are no UI overlays, watermarks, social media artifacts, fake film borders, stickers, or unrelated decorations.

If one major item fails, regenerate once with a shorter, stricter prompt focused on that failure.
