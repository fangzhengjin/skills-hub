# Prompt Compiler

Compile only information that can become visible pixels. Prefer one concrete visual decision over several vague aesthetic labels.

## Field Order

Every generation prompt must answer these questions in order:

1. **Canvas:** ratio, paper surface, border/mockup status.
2. **Attention geometry:** negative-space percentage, cluster size, and position.
3. **Input-photo contract, when applicable:** image role, preservation level, concrete invariants or reference traits, permitted changes, and new elements.
4. **Visual metaphor:** the one subject or relation that carries the meaning.
5. **Focal-element form:** photo, clipping, silhouette, block, specimen, printed illustration, texture window, typography, or overlapping panels.
6. **Material treatment:** halftone, xerox softness, risograph grain, letterpress bleed, torn or softened edge, scanline, or slight misregistration.
7. **Typography:** one short phrase, optional archive microtext, font family, and spatial behavior.
8. **Color:** exact main hue, material form, and approximate visual share; optional tiny support hue only when needed.
9. **Reproduction and mood:** flat scanned-paper view, light, contrast, and emotional temperature.
10. **Hard avoids:** the shortest relevant anti-identity list.

## Four-paragraph Prompt Shape

1. Canvas + paper + negative space + cluster size and location.
2. Input-photo contract when applicable + visual metaphor + focal-element form + material treatment.
3. Typography + exact main hue + chromatic material form and share + print defects.
4. Flat scan mood + relevant avoid list.

Do not recite the field names. Write decisive image directions as four compact paragraphs.

## Prompt Template

```text
Tall vertical [ratio] paper poster, full-frame [paper_tone] aged paper with [paper_texture], no border and no mockup. Keep [negative_space]% as open paper. Place one [cluster_scale]% visual cluster at [position], comfortably away from the edges.

Translate “[theme]” into [one_visual_relation]. Render it as [focal_element_form] using [focal_element_treatment]. Keep the event isolated and imageable; do not expand it into a full scene.

Use [typography_mode] for the short phrase “[short_text]”, with optional [microtext_role]. Use [exact_hue] as the sole saturated color, carried by [color_material] and occupying about [canvas_color_share]% of the canvas or [cluster_color_share]% of the visual cluster. Apply [print_defects] without washing out the chromatic ink.

Flat orthographic scanned-paper appearance, matte absorbent surface, diffuse light, low-to-medium contrast, [mood]. Avoid [relevant_avoids].
```

For an edit target or supporting insert, replace the second paragraph with:

```text
Use the supplied image as [edit_target / supporting_insert] with [high / medium] preservation. Keep [preservation_invariants] recognizable. Allow changes only to [permitted_changes], and introduce only [new_poster_elements]. Translate “[theme]” into [one_visual_relation] and stage it as [focal_element_form] using [focal_element_treatment], without expanding it into a full scene.
```

For a reference image, replace the second paragraph with:

```text
Use the supplied image only as a visual reference for [reference_traits]. Preserve none of its source subject, identity, wording, or exact composition. Create a new [new_subject_and_relation] for “[theme]” and stage it as [focal_element_form] using [focal_element_treatment] in a clearly different composition, without expanding it into a full scene.
```

## Compilation Rules

- For an article or complex idea, extract one thesis and one visual relation. Do not summarize the article in the picture.
- For an edit target or supporting insert, name the input image role and repeat the preservation invariants in the prompt. Do not rely on a vague instruction such as `keep the subject similar`.
- For High preservation, prefer an original-photo crop, clipping, or printed fragment over redrawing. Do not convert an identifiable person, pet, product, character, or artwork into a silhouette or loose illustration unless the user explicitly permits reinterpretation.
- For a reference image, describe only the visual traits to learn and explicitly require a new subject and composition.
- If the user supplies exact poster text, use it. Otherwise invent one short phrase in the user's language or in concise English when that fits the mood.
- Keep exact readable text short. Treat longer words as texture only when the user does not require accurate reading.
- Describe low contrast or muted grayscale only for paper, photographs, and secondary ink. Preserve saturation in the main color accent.
- State actual placement and size. Avoid words such as `somewhere`, `minimal`, `nice`, `artistic`, or `balanced` without renderable constraints.
- Use one main hue. A second hue is allowed only as a tiny subordinate mark and never as equal visual weight.
- In the final generation prompt, name the actual visible carrier: photo crop, paper cutout, ink block, specimen, printed illustration, texture window, or typography. Do not substitute ambiguous compositional shorthand for that concrete noun.
- When the theme is not maritime, do not introduce ship-mooring objects, nautical emblems, or generic pictograms. When the user explicitly requests a maritime subject, describe only the requested object and its visible treatment.
- Choose negative constraints relevant to the selected recipe; do not waste prompt space on an indiscriminate catalogue.

## Compact Negative Bank

Select the relevant items:

```text
full-bleed scene, commercial headline, product ad, logo, CTA, brand campaign, glossy paper mockup, clean UI white, cinematic lighting, hard shadow, depth of field, 3D render, neon, cyberpunk, cute cartoon, anime poster, fashion editorial drama, dense scrapbook, too many objects, multicolor palette, stock-photo realism, long clean text block, copied reference wording, copied reference composition
```
