---
name: photo-small-world-revival
description: Reinterpret a user-supplied everyday photo as a small, source-specific hand-drawn world on spacious white paper. Unlike a general photo-revival treatment, this skill must preserve one primary subject, one companion element, and their clearly visible relation, then perform a restrained reconstruction using exactly one fixed scene recipe (Held Moment, Table Island, Window Distance, or Passing Trace), one vivid source color, and no photographic pixels. It discards most scenery and descriptive detail. Use for family snapshots, pets, food, objects, travel moments, windows, street scenes, and quiet personal memories when the user wants to focus on a specific subject relationship. Choose photo-revival instead when the goal is a broader poetic redraw that retains more of the overall scene atmosphere without the explicit primary-companion structure.
---

# Photo Small World Revival

Generate a finished raster illustration by default. Keep the relationship that made the snapshot worth taking and let most of the page remain unoccupied.

Return the image, selected scene recipe, and a short Chinese rationale. Reveal the final prompt only when requested.

## Non-Negotiable Identity

Every result must contain:

1. One portrait 2:3 white or near-white paper page.
2. Roughly 72-88% quiet paper.
3. One compact illustrated world occupying roughly 12-24% of the page.
4. One primary subject and one companion element joined by a visible source-derived relation.
5. One localized vivid source hue; all other colors remain neutral or softly source-compatible.
6. One hand-rendered material system and a natural irregular edge.
7. One short handwritten caption unless the user explicitly requests no text.

The page must read as:

```text
one remembered relation held sharply -> most descriptive reality released
```

Do not preserve photographic pixels anywhere in the final image.

## Read the Photograph

Build a Small World Card:

- **Primary:** the person, pet, object, food, vehicle, structure, or view that carries the memory.
- **Companion:** one element that gives the primary meaning or scale.
- **Relation:** touch, gaze, containment, support, distance, repetition, shelter, reflection, or shared direction.
- **Gesture:** the dominant lean, curve, horizon, frame, hand action, or movement.
- **Identity cues:** two to four source-specific details required for recognition.
- **Color witness:** one meaningful source hue and the element that owns it.
- **Discard:** background objects, surface detail, signage, clutter, and photographic lighting effects that do not support the relation.

Write one internal sentence:

```text
Keep [primary] in relation to [companion] through [visible gesture]; let [color witness] carry the remembered emphasis.
```

If no primary-companion relation can be identified, use a different skill instead of drawing a generic centered object.

## Select One Scene Recipe

Choose exactly one recipe. Do not combine recipes.

### Held Moment

Use for a person with another person, pet, toy, tool, flower, meal, or carried object.

- Place the compact world in the lower-left, lower-middle, or lower-right region.
- Preserve the contact gesture and two to four identity cues; simplify faces unless likeness is explicitly requested.
- Let the companion overlap or sit within one gesture-length of the primary.
- Put the color witness on the point of contact or the companion.
- Place the caption just below or beside the cluster.

### Table Island

Use for food, tableware, flowers, tools, books, collections, and domestic still life.

- Render one small top-down or oblique island with a short partial table edge, cloth fold, tray, or shadow line.
- Keep one primary object and one companion; reduce all other objects to zero to three supporting marks.
- Use unequal scale and spacing; do not arrange a product flat lay.
- Concentrate the vivid hue in one edible, floral, paper, ceramic, or textile form.
- Leave at least 40% of the page as uninterrupted upper paper.

### Window Distance

Use for a subject looking through a window, gate, door, train frame, balcony, or architectural opening.

- Simplify the frame into two to four broken lines, never a full detailed facade.
- Keep the near subject or sill plus one distant companion mass.
- Preserve the actual near/far ordering and one recognizable opening shape.
- Use the color witness either on the near anchor or as one distant field, never both.
- Keep the surrounding page open so distance is carried by interval.

### Passing Trace

Use for walking, cycling, vehicles, wind, shoreline movement, or a fleeting street moment.

- Preserve one primary silhouette or gesture and one environmental companion such as a curb, rail, tree, shadow, or horizon.
- Extend one broken source-derived line behind or ahead of the cluster to show direction.
- Use no more than three small neutral rhythm marks; do not duplicate the subject.
- Place the color witness at the leading or trailing edge according to the source.
- Leave more open paper in the movement direction than behind it.

## Illustration Grammar

Choose one primary medium and at most one supporting medium:

- dry watercolor with graphite;
- colored pencil with flat gouache;
- broken ink wash with wax crayon;
- dry brush with soft pastel pencil;
- rough letterpress silhouette with sparse hand line.

Keep handmade pressure, imperfect registration, absorbed edges, and limited local texture. Use natural irregular contours that meet the paper directly. Avoid sticker outlines, fuzzy cutout halos, glossy digital rendering, and uniform full-page grain.

Preserve the primary-companion relation, gesture, and identity cues. Omit roughly 70-90% of descriptive detail. Do not copy the full photographic framing, realistic shadows, depth of field, or lens effects.

## Color Witness

Choose one exact vivid hue already present in the source or a close intensified version of it. Assign it to the source element that carried the hue; do not move it to an unrelated object.

Let the hue occupy roughly 18-40% of the active cluster while remaining below roughly 5% of the whole page. Use one opaque or richly pigmented area and at most one much smaller echo inside the same relation.

Keep other marks charcoal, graphite, warm gray, faded ink, or one low-chroma source-compatible wash. Do not make the entire illustration pastel or low saturation; the witness hue must remain clear at thumbnail size.

## Caption

Unless the user requests no text, include one exact handwritten caption:

- Chinese: two to ten characters; or
- English: one to five words.

If the user supplies text, reproduce it verbatim. Otherwise write a concrete phrase about the retained relation, not a generic mood. Do not invent dates, locations, signatures, or diary facts.

Use small graphite, colored pencil, or dry ink handwriting. Keep it adjacent to the cluster with generous space; do not use poster headlines or pseudo-writing.

## Prompt Compiler

Compile four compact paragraphs, normally 130-210 words:

1. **Page and recipe:** portrait 2:3, paper, quiet share, selected recipe, cluster size and placement.
2. **Small world:** primary, companion, relation, gesture, identity cues, omissions, and source-responsive recomposition.
3. **Medium, color, and caption:** exact medium, vivid source hue, its owner and area, exact caption, hierarchy, and eye path.
4. **Reproduction and exclusions:** flat scanned paper, natural edge, no-photo rule, and hard avoids.

Always include:

```text
Use the supplied photograph as a semantic and structural reference only. Do not reproduce, embed, crop, collage, trace, or retain photographic pixels or photorealistic regions from it.
The final image must contain original hand-rendered illustration, paper, and the exact caption only. Preserve the primary-companion relation and the listed identity cues, but discard most descriptive scenery.
```

Write only visible-pixel instructions. Do not mention analysis, skill names, API details, file paths, or checklist wording.

## Generate and Revise

Use the supplied image as the required semantic reference. If the user specifies an image provider, follow that provider's instructions for generation, credentials, output paths, and validation. Otherwise use the image-generation workflow available in the current environment.

Inspect normal and thumbnail views. Regenerate at most once for one observed defect:

- **Photo pixels or photorealism remain:** remove them and redraw only the small world in the selected medium.
- **Full scene was illustrated:** retain primary, companion, gesture, and identity cues; remove background detail.
- **Cluster is too large:** reduce it to the recipe range and restore continuous quiet paper.
- **Relationship is unclear:** move primary and companion closer or restore the source contact, gaze, frame, or shared line.
- **Result is generic:** restore two to four source-specific identity cues.
- **Color is weak or widespread:** intensify it on its source owner and neutralize the rest.
- **Result is cute or commercial:** simplify expression, remove polish and stickers, and restore dry handmade material.
- **Caption is false or illegible:** use the exact short caption, reduce decorative lettering, or remove it by request.

## Hard Avoids

Avoid photographic pixels, photo filters, photorealistic cutouts, full-scene redraws, realistic portraits without request, dense backgrounds, centered mascot poses, sticker outlines, fuzzy halos, cute cartoon, kawaii, anime, children's-book sweetness, product flat lays, many colorful objects, pastel wash across the page, arbitrary flowers or dots, scrapbook tape, floating paper, cast shadows, curled corners, 3D mockups, cinematic lighting, depth of field, neon, logos, watermarks, long text, and illegible pseudo-writing.

## Quality Gate

Verify:

- No photographic pixels or photorealistic regions remain.
- One primary, one companion, and their source-derived relation are immediately readable.
- Two to four identity cues make the result specific to this photograph.
- Quiet paper occupies at least roughly 72% of the page.
- One vivid source hue is localized and visible at thumbnail size.
- The caption is exact, small, legible, and truthful, or intentionally absent by request.
- The result feels intimate and authored rather than cute, generic, or commercially polished.

## Output

```markdown
![Photo Small World Revival](absolute-image-path-or-rendered-image)

**创作说明**

[用简短中文说明保留的主体关系、删去的现实、手绘材料和色彩见证。]

**场景配方**

[Held Moment / Table Island / Window Distance / Passing Trace]
```
