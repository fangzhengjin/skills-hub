---
name: travel-photo-soft-abstraction
description: Analyze a user-uploaded travel photograph and reconstruct it as a CLEAN upper-photo/lower-abstraction editorial artwork. Use when Codex should preserve the original photo unchanged above, generate a source-readable softly abstract lower panel guided by bundled references, and add a number, date, and short phrase. This is subtle visual distillation, not style transfer, heavy symbolism, or a miniature redraw.
---

# Travel Photo Soft Abstraction

Treat the task as three deliberate operations: **deconstruct**, **abstract/distill**, and **reconstruct**. The lower panel is a new visual composition made from relationships extracted from the upper photograph. It is neither a miniature redraw nor a style-converted copy. Derive all lower-panel evidence from the source photograph and only the mark language from the bundled references. Never apply reference style to the original photograph.

Default to **subtle editorial optimization mode** unless the user explicitly asks for stronger abstraction. A successful lower panel should still feel like the original skill's clean travel-photo abstraction: source-readable relationships are simplified, polished, and better balanced rather than aggressively symbolized. Prefer a clear distilled memory of the photograph over either a literal redraw or a generic abstract diagram.

## Input role lock

- Define `USER_PHOTO` as the photograph attached or uploaded by the user in the current request. Record its exact local path before analysis.
- Define `STYLE_REFS` as selected files from `assets/style-references/`. They guide only the lower generated panel.
- Define `GENERATED_PANEL` as the new abstract image produced for the lower half.
- The final composite must contain exactly `USER_PHOTO` above and `GENERATED_PANEL` below. Never place a style reference, prior output, screenshot, or generated derivative in the photographic position.
- Use the same locked `USER_PHOTO` path for visual analysis, metadata/date inspection, palette evidence, `finalize_artwork.py`, and validation. If the path becomes unavailable, stop instead of substituting another image.

## Non-negotiable delivery contract

- Treat the image-generation result as a temporary abstract-panel asset. Never display or return it to the user.
- Obtain real local filesystem paths for the untouched original and generated abstract panel. If either path is unavailable, stop and return no artwork.
- Produce the deliverable only with `scripts/finalize_artwork.py`; do not run the compositor and validator separately for final delivery.
- Return an image only after the finalizer prints `DELIVERY PASS`. Return only its output path, never the generated panel path.
- If generation, local saving, composition, or validation fails, return no image and name the failed stage. An abstract panel without the original is always an intermediate failure.
- Keep `USER_PHOTO` above the abstraction at its exact native width, height, orientation, and RGB pixel values. Never resize it, even proportionally.

## Deconstruct-distill-reconstruct contract

1. **Deconstruct:** separate the source into high-information evidence: dominant mass, axes, boundaries, counts, intervals, directions, overlaps, depth order, color roles, asymmetry, and meaningful voids.
2. **Abstract and distill:** discard photographic surface, literal object outlines, texture, perspective detail, minor objects, and redundant evidence. Reduce each retained fact to the smallest suitable mark or field.
3. **Reconstruct:** compose the distilled marks into a new nonliteral arrangement that preserves the source's relational identity and spatial rhythm without reproducing its scene layout literally.
- Preserve relational invariants such as relative dominance, left/right or above/below order, directional flow, count groups, gaps, clustering, overlap, and depth hierarchy. Exact coordinates and source aspect ratio are evidence, not a tracing template.
- Permit displacement, compression, separation, overlap, and scale change only when they clarify the extracted relationships. Never rearrange arbitrarily or add decoration without source evidence.
- Require the result to read as an abstract visual memory of this exact photograph, not a generic subject icon, miniature illustration, vectorized scene, filtered photograph, or style transfer.
- Keep the reconstructed motif within a responsive area surrounded by CLEAN poetic negative space; do not draw a frame around it.

## Subtle optimization contract

- Before prompt writing, state one short **visual intention** for the source: what should feel cleaner, more balanced, more poetic, or more memorable than a plain summary.
- Keep one primary source fact and two to four secondary source facts when they help the lower panel remain connected to the specific photograph. Do not over-delete distinctive evidence merely to make the result look more "artistic".
- Use recognizable source nouns during analysis when they help fidelity. Translate them into simpler formal language only in the generation prompt where literal nouns would cause a cute icon, travel sticker, or mechanical miniature.
- Permit only gentle formal changes: slight simplification, softened geometry, scale reduction, measured spacing, mild compression, or cleaner color grouping. Avoid dramatic distortion unless the user explicitly asks for stronger abstraction.
- Make a lower panel fail if it reads first as a cartoon sticker, vector souvenir, generic logo, unrelated symbol system, or exact scene tracing. A quietly recognizable distilled scene structure is acceptable and often preferred.
- Keep marks inside the validated motif zone. Leave the upper 25%, lower 20%, far left, far right, and central empty-background sampling areas visibly blank and uniform unless the finalizer is updated.

## Lower-panel text contract

- The completed lower panel must contain exactly three peripheral microtype items: sequential `NO. 00X`, factual `DD MON YYYY`, and one image-derived uppercase English phrase of 1-3 words.
- Keep the number at the upper-right of the lower field. Place the date and phrase as two separate lines in another empty corner.
- Generate the abstract artwork with no text, then add all three items deterministically with `finalize_artwork.py`. The no-text generation rule applies only to the temporary generated artwork, not to the completed lower panel.
- Treat missing, duplicated, misspelled, malformed, or additional text as rejection.
- During reconstruction, preserve relational invariants rather than exact coordinates. Permit evidence-based displacement, compression, separation, overlap, and rescaling; never use the source geometry as a tracing template.

## Reconstructed-motif scale contract

- Keep every existing visual, analytical, text, source-integrity, and composition rule unchanged; adjust only the reconstructed motif's overall scale.
- Make the complete reconstructed motif occupy approximately 35-45% of the lower panel's width and no more than 32% of its height.
- Leave approximately 65-75% of the lower panel visually empty. Treat the clean field as intentional poetic space without making the result feel disconnected from the photo.
- Scale the motif as one coherent group. Preserve all internal size ratios, intervals, directions, overlaps, hierarchy, and asymmetry while reducing it.
- Keep the motif near the lower-middle or reference-supported asymmetric position. Do not enlarge individual elements to compensate, scatter them across the panel, or turn the motif into a generic logo.

## Uniform CLEAN-background contract

- Use one continuous, perfectly uniform neutral-ivory background across the entire generated lower panel, targeting `#F3F0E8`.
- Treat the background as a single flat color plane, not as atmosphere. Permit color variation only inside source-derived reconstructed marks.
- Add no gradient, lighting falloff, glow, shadow, vignette, edge darkening, horizontal or vertical band, patch, seam, paper tone, canvas texture, noise, grain, mottling, haze, bloom, stain, or compression-like discoloration.
- Do not place a lighter strip behind the number or a different field behind the date and phrase. The motif and all three microtype items must sit on the same uninterrupted background color.
- Inspect empty areas at the center, all four sides, and all four corners at normal size and with sampled RGB values. Reject and regenerate the panel if empty-area color visibly or measurably changes across the field.

## Required workflow

1. Run `scripts/check_installation.py`. Stop and report an incomplete installation if it fails.
2. Confirm that a built-in image generation tool is callable. If it is absent, unavailable, denied, or fails, stop and tell the user. Use programmatic tools only for deterministic composition, exact microtype, and validation; never use them to draw the abstract motif.
3. Lock the exact path of the photograph uploaded by the user in this request as `USER_PHOTO`, then inspect it as the sole content source. Read [references/analysis-method.md](references/analysis-method.md), [references/style-guide.md](references/style-guide.md), [references/structural-reference-index.md](references/structural-reference-index.md), and [references/run-log-template.md](references/run-log-template.md). Never silently substitute a bundled reference, earlier upload, previous result, screenshot, or recompressed export.
4. Select and inspect 3-5 of the 19 bundled images using `structural-reference-index.md`. Select references whose lower panels offer relevant abstraction grammar, spatial density, mark language, palette restraint, and poetic use of empty space. Use all 19 as the eligible style library.
5. Record the primary element's identity, shape, count, normalized position, relative scale, color, direction, and depth. Identify one structural axis plus meaningful intervals, gaps, overlaps, clusters, or repetitions. Identify distinct source-derived color roles that can support restrained emphasis.
6. Complete the abstraction-plan worksheet in `analysis-method.md`. Add a visual intention, choose a subtle abstraction intensity unless the user asks otherwise, map every proposed mark to a named source fact, and remove only decorative or redundant marks.
7. Use one primary motif family and two to four supporting families when the photograph needs them for recognition. Encode relationships rather than photographic surface: preserve counts, coordinates, size ratios, directions, spacing, asymmetry, occlusion, and negative-space distribution while simplifying texture and detail. Translate these facts through the selected references' lower-panel vocabulary-flat or softly organic masses, hairlines, dots, bars, isolated silhouettes, restrained color fields, and measured asymmetry-without copying any specific reference composition. In subtle mode, keep enough recognizable source structure for the lower panel to feel like this photograph's clean abstract companion.
8. Always use an upper/lower composition. Paste `USER_PHOTO` above at exactly its native pixel width and height, without resize, crop, resampling, retouching, or generative editing. Generate the lower panel at a compatible ratio, scale it proportionally to the photo width, and preserve its complete frame without cropping. Follow the selected references' motif scale and poetic negative space.
9. Determine the archive number before generation. Use `NO. 001` for the first completed artwork; otherwise continue the highest completed number. Reserve the number only for the selected final.
10. Prepare exactly two archive lines: line 1 is `DD MON YYYY`, using verified capture date or otherwise the artwork creation date; line 2 is a concrete, quiet, image-derived English phrase of 1-3 uppercase words.
11. Supply the image tool with locked `USER_PHOTO` plus 3-5 selected bundled references in one generation call (the tool accepts at most five images total). Label roles explicitly: `Image 1 = USER-UPLOADED CONTENT SOURCE ONLY`; `Images 2-N = BUNDLED LOWER-PANEL STYLE REFERENCES ONLY`. Generate only `GENERATED_PANEL`. Save it locally; never treat a style reference or Image 1 as generated output.
12. Use **CLEAN mode only**, joined with the selected references' poetic restraint. Match their lower-panel balance, quiet editorial tone, sparse hierarchy, varied mark scale, subtle organic geometry, and controlled source-derived color accents. Translate any visibly textured reference treatment into a clean matte equivalent. Keep one uninterrupted, exactly uniform neutral-ivory background near `#F3F0E8`; allow no gradient, lighting variation, band, patch, seam, paper texture, watercolor bloom, haze, stain, vignette, or differing text-area field.
13. Reject and regenerate the lower panel if it resembles a style-transferred photograph, exact tracing, posterization, sticker, generic logo, unrelated symbol system, or over-complete illustration. Also reject it if a major mark lacks source correspondence, empty space falls outside 65-75%, the motif exceeds its envelope, any text appears, or sampled empty-background areas differ visibly or measurably in color.
14. Run `scripts/finalize_artwork.py USER_PHOTO GENERATED_PANEL FINAL --number "NO. 00X" --date "DD MON YYYY" --phrase "WORDS"`. Verify that the first positional argument is the same locked user-upload path from step 3. Never pass a bundled reference or prior output in that position.
15. Confirm that the final output contains exactly three text items: `NO. 00X`, `DD MON YYYY`, and the 1-3 word uppercase phrase. Add no other metadata, color swatches, captions, place names, camera data, GPS, `FRAME`, or `STUDY` text.
16. Inspect the final output side by side with the original. Reject it if the upper photo differs in width, height, orientation, pixels, crop, tone, color, sharpness, content, grain, or exposure.
17. For every revision, regenerate only the lower panel from the original analysis; never recursively edit the final composite.
18. Require `DELIVERY PASS` from `finalize_artwork.py`. It runs validation with the original and removes the candidate on failure. Treat a missing output, missing pass message, or photographic pixel mismatch as rejection.
19. Complete the run log from `references/run-log-template.md`, including the actual model, image tool, generated panel, and composition command. Never claim a tool or model that cannot be verified.
20. Save one polished result with a descriptive non-overwriting filename. Increment the sequence only after the final is saved.

## Generation prompt scaffold

```text
Use case: visual distillation
Asset type: abstract lower panel only, for later deterministic composition
Input image: Image 1 is the photograph uploaded by the user in the current request. It is the sole content source, never an edit target. Generate no photographic panel and do not reproduce Image 1.
Style references: Images 2-N are bundled lower-panel style references only. They are not the original photograph and must never appear in the final upper panel. Match only their abstraction vocabulary, spatial balance, restrained palette, quiet editorial tone, and poetic negative space.
Core method: DECONSTRUCT, ABSTRACT/DISTILL, RECONSTRUCT - NEVER STYLE TRANSFER. First separate Image 1 into dominant masses, axes, boundaries, counts, color roles, directions, overlaps, intervals, depth, asymmetry, and meaningful voids. Then remove photographic detail and literal outlines. Finally rebuild only the retained relationships as a new nonliteral system of minimal marks. Preserve relational identity and spatial rhythm, not the exact scene or pixel geometry.
Subtle mode: default to subtle editorial optimization, not heavy symbolism. State one visual intention for the lower panel, then keep the source facts that preserve recognition and compositional rhythm. Prefer cleaner grouping, restrained simplification, better spacing, and source-derived color order over dramatic deletion. Avoid literal nouns only when they would make the result a cute icon, sticker, or mechanical miniature.
Layout: portrait lower panel planned for an untouched full-frame photograph above it. Create one coherent reconstructed motif occupying about 35-45% of panel width and at most 32% of panel height, leaving roughly 65-75% visually empty. Scale the motif as one coherent group while preserving its internal hierarchy and relationships. Allow measured displacement, compression, separation, overlap, and scale change when these make the source relationships clearer. Do not place the abstraction inside a miniature scene frame, trace the source aspect ratio as a visible box, scatter marks to fill space, or collapse it into one unrelated symbol.
Validation-safe placement: keep the upper 25% and lower 20% of the generated panel blank unless the motif is known not to touch validation sample zones. Do not let tall spikes, broad curves, or reflections reach the background sampling areas.
Surface mode: CLEAN ONLY with poetic negative space. Use one perfectly uniform, uninterrupted flat field at or near #F3F0E8 across every background pixel. The center, edges, corners, number area, and date/phrase area must share the same background color. Create atmosphere only through sparse placement, pauses, distance, asymmetry, and silence - never through surface effects. Use clean matte marks with subtly organic contours when structurally justified. Add no gradient, light falloff, glow, shadow, edge darkening, band, patch, seam, grain, noise, paper texture, fibers, watercolor bloom, haze, vignette, stains, faded color, or grading.
Color emphasis: slightly prefer several distinct accent roles sampled from `USER_PHOTO` when they clarify different source facts. Preserve their original saturation, luminance hierarchy, and approximate dominance. Do not force extra colors into a monochrome source.
Text: generate no text of any kind. The deterministic compositor adds the exact archive number, date, and phrase later.

Core visual evidence:
- Visual intention: [one sentence naming the clean editorial feeling or relationship to preserve]
- Abstraction intensity: [subtle-editorial, poetic-minimal, or stronger-artistic; default subtle-editorial]
- Primary element: [identity, shape, count, position, scale, color, direction]
- Structural axis: [horizon, vertical, curve, or diagonal and normalized location]
- Spatial rhythm: [intervals, clusters, gaps, depth, overlap, or repetition]
- Secondary evidence: [two to four supporting relationships when useful]

Deconstruction and reconstruction mapping:
- [source fact] -> [minimal mark + relative placement + relative size]
- [source fact] -> [minimal mark]
- [source fact] -> [minimal mark]

Removal decision: omit [textures, background detail, or low-information objects].
Constraints: preserve source relationships before decorative style; every major mark needs source justification; one primary motif family and two to four supporting families when useful; quiet, clean, sparse, restrained; make only gentle formal improvements unless stronger abstraction is requested.
Avoid: photograph, exact scene reconstruction, generic style transfer, heavy stylization, vectorized logo, posterization, literal tracing, complete illustration, cute icon, travel sticker, souvenir graphic, unrelated symbol system, decorative filler, regularized spacing, invented symmetry, invented content, any text, numbers, captions, color swatches, watermark, gradient background, uneven background, lighting falloff, background bands or seams, visible grain, dirty paper, yellow cast, gray veil, watercolor, haze, or texture.
```

## Output rules

- Default to one result and CLEAN mode.
- Preserve identity-sensitive subjects and existing occlusions. Never reconstruct concealed faces, bodies, or structures.
- Vary abstractions through different valid source evidence or symbol mappings, not arbitrary color themes.
- Favor restrained differentiation among source-derived accent colors, not decorative recoloring.
- If the lower panel cannot be explained as a short source-evidence-to-mark list, or if it merely looks like the upper scene in another visual style, revise it.
- If the lower panel looks like a cartoon sticker, unrelated symbol system, or exact tracing, revise toward a clean source-readable abstraction with modest deletion and better spacing.
- Reject both extremes: a style-transferred scene and a generic diagram that ignores the selected references' visual language.
- Keep final text limited to `NO. 00X`, the date, and the phrase, all added during deterministic finalization.
- Treat any new photographic grain, tonal drift, color cast, or softness as a failed output, not as acceptable atmosphere.
- Treat any nonuniformity in the lower panel's empty background as a failed output. Require one continuous CLEAN background color behind the motif, number, date, and phrase.
- Return only the file that received `DELIVERY PASS`; never return the temporary abstract panel.
