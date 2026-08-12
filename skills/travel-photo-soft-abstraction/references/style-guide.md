# Style Guide

## Visual thesis

Pair the exact photograph uploaded by the user with a newly generated reconstruction of its distilled visual evidence. The lower panel must deconstruct and reinterpret relationships from the upper image; it must not reproduce the scene in a new style. Selected bundled lower panels determine only the reconstruction's visual grammar.

The lower panel should feel lightly art-directed rather than merely summarized. It should make the source relationships cleaner, more balanced, and more memorable while remaining source-readable. Subtle fidelity is preferred over a strong abstract proposition unless the user explicitly asks for more abstraction.

## Layout

- Always use an upper/lower composition for every source orientation.
- Preserve the photograph at its exact native pixel width, height, orientation, and RGB values. Do not resample it.
- Give the lower abstract field 1.10–1.60 times the photograph's height.
- Use abstract-only output only when explicitly requested.
- Keep divisions straight and unornamented.
- Build one coherent reconstructed motif rather than a literal scene. Use measured simplification, spacing, mild compression, and cleaner color grouping to clarify source relationships, with generous but not overpowering negative space.
- Make the complete motif moderately compact: target 35–45% of lower-panel width and no more than 32% of lower-panel height, with roughly 65–75% visual empty space. Reduce it as one group without altering internal relationships.
- Use the selected references to choose motif scale, position, and distribution. Keep poetic negative space, but do not reduce every source to a tiny centered diagram.
- Prefer gentle asymmetric placement or scale adjustment when it improves balance. Avoid dramatic distortion unless explicitly requested.
- Keep marks inside the validated motif zone. Leave the upper 25%, lower 20%, far left, far right, and central background-sampling areas visibly blank and uniform unless the finalizer is updated.
- Avoid borders, shadows, cards, frames, collage effects, oversized motifs, and decorative corner filling.

## Source-to-reconstruction mapping

- Deconstruct the photograph's dominant masses, axes, boundaries, counts, intervals, gaps, directions, overlaps, depth, color roles, asymmetry, and meaningful voids before selecting marks.
- Preserve relational invariants rather than exact coordinates: dominance, directional flow, left/right and above/below order, count groups, clustering, intervals, overlap, and depth hierarchy.
- Abstract and distill each retained fact into the smallest useful mark or field.
- Reconstruct those marks into a new composition. Permit deliberate displacement or scale change when it improves clarity, but never rearrange arbitrarily.

- Mass or field -> one clean flat block or quiet plane.
- Compact object -> dot, circle, pill, short line, or tiny silhouette.
- Horizon or boundary -> one thin line.
- Direction or motion -> taper, streak, aligned bars, or directional sequence.
- Repeated objects -> repeated modules with source spacing and scale hierarchy.
- Radial structure -> partial arc plus selected spokes and nodes.
- Enclosure or occlusion -> nested or overlapping shapes without completing hidden content.
- Reflection or shadow -> shortened, lighter echo aligned to its source.
- Close portrait -> reduced field-and-feature topology that preserves source-relative placement and asymmetry without reconstructing identity-sensitive detail.
- Framing architecture or landscape -> simplified edge masses that remain in their source-relative positions and preserve left-right weight.

Use one primary motif family and two to four supporting families when needed for source recognition. Preserve source asymmetry and irregular spacing.

Default to subtle editorial abstraction:

- Keep one primary source fact and two to four secondary source facts if they make the lower panel feel tied to this exact photograph.
- Translate literal nouns into formal roles only where needed to prevent cute icon or sticker behavior: tower -> vertical signal, mountain -> cold mass, road -> dark passage, shoreline -> shore weight, window lights -> light intervals, boat or buoy -> floating dot.
- Let omission remove clutter, not identity. Preserve distinctive source relationships before adding stronger abstraction.
- Reject a lower panel if its first read is a cute icon, travel sticker, generic logo, unrelated symbol system, or exact scene tracing.

Do not redraw, miniaturize, vectorize, filter, or style-convert the photographed scene. A valid panel is a new abstract construction whose source can be explained through retained relationships, not through copied object outlines or scene geometry.

## Reference style transfer boundary

- Lock the current user-uploaded photograph path before selecting references.
- Pass that user upload and 3–4 selected references together to the image tool.
- Label the user upload as content evidence only and bundled references as lower-panel style evidence only.
- Borrow the references' abstraction grammar, soft or flat mark character, scale variation, sparse editorial balance, restrained palette behavior, and atmospheric emptiness.
- Never borrow their photographed subjects, exact arrangements, obsolete texture, metadata, or photo grading.
- Never use a bundled reference, earlier upload, previous composite, screenshot, or generated image as the upper photograph.
- Never style, redraw, or regenerate the current user-uploaded photograph.

## Surface mode

Use **CLEAN only**.

- Preserve `USER_PHOTO` exposure, white balance, saturation, black level, highlight brightness, local contrast, sharpness, detail, and noise profile.
- Add no film grain, paper grain, sensor noise, haze, bloom, vignette, faded blacks, color cast, softened highlights, or global grading.
- Use one perfectly uniform, uninterrupted light neutral-ivory lower field near `#F3F0E8`. The center, edges, corners, number area, and archive-text area must share the same background color.
- Render clean matte shapes with controlled but subtly organic contours when structurally appropriate. Keep the field perfectly clean and any variation inside marks imperceptible at normal viewing size.
- Generate the abstract panel as a temporary local asset, then run `scripts/finalize_artwork.py` to compose and verify the only deliverable file. Never return or display the temporary panel.

## Color

- Extract 3–5 color roles from the photograph.
- Preserve source saturation and luminance relationships.
- Slightly prefer assigning different sampled color roles to different meaningful marks when this improves distinction.
- Use 2–3 restrained accent roles when the source genuinely contains them; keep their approximate dominance subordinate to the primary structure.
- Allow a small saturated accent only when present in the source.
- Keep a monochrome or narrowly colored source correspondingly restrained; never add variety merely to make the abstraction colorful.
- Avoid invented neon, rainbow palettes, glossy gradients, and global muting.
- Use neutral ivory near `#F3F0E8`; do not warm it into aged paper.

## Mark-making

- Prefer clean matte flat fills, hairline graphite or ink lines, small dots, and short bars.
- Use soft blur or translucent streaks only when the source itself contains blur, rain, glow, or defocus.
- Avoid thick paint, watercolor blooms, torn paper, tape, embossing, stains, and 3D depth.

## Photographic treatment

Never send the photographic panel through generative editing. Pass the locked current user-upload path as the first argument to `finalize_artwork.py` and preserve its exact native dimensions and pixels. Do not substitute, resize, crop, resample, or alter it.

## Microtype

- Treat number, date, and phrase as required parts of the completed lower-panel composition, not optional metadata.
- Place exact `NO. 00X` in extremely small, widely tracked, light-gray monospaced type at the upper-right of the lower panel.
- Add exactly two tiny lines in another empty corner: factual `DD MON YYYY`, then a 1–3 word uppercase English atmosphere phrase derived from the image.
- Add the three text items only through deterministic finalization. Add no camera data, coordinates, captions, titles, place names, signatures, color swatches, `FRAME`, `STUDY`, or extra metadata.

## Quality checklist

- Every major abstract mark maps to an observable source fact.
- The lower panel has a named visual intention, and every retained mark supports source-readable simplification.
- The complete reconstructed motif occupies 35–45% of lower-panel width and at most 32% of lower-panel height; its internal scale hierarchy and relationships remain unchanged.
- Visual empty space occupies approximately 65–75% without scattering marks merely to fill the panel.
- The motif occupies its planned 25–50% envelope, up to 60% only for structurally wide sources, and empty space occupies 65–85%.
- The palette comes from the source and retains its luminance relationships.
- Distinct accent colors encode different source facts rather than decorating repeated versions of the same mark.
- Required archive text is exact, tiny, and peripheral.
- Side-by-side comparison shows no new grain, speckling, darkening, warming, graying, desaturation, softness, highlight loss, or compression in the photographic panel.
- CLEAN output uses one flat neutral-ivory field without gradients, lighting falloff, glow, shadow, bands, patches, seams, paper noise, stains, or mottling. Any visible or measurable empty-area background variation is a rejection.
- Surface style never overrides source structure.
- The result is more than a literal object diagram, but it should still read as a clean abstraction of the same photo rather than an unrelated symbolic composition.

## Reference selection

Read `structural-reference-index.md` and inspect 3–4 relevant images from all 19. Use their lower panels as explicit style references while keeping locked `USER_PHOTO` as the sole content source and final upper panel.
