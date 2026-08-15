---
name: photo-evidence-ledger
description: "Turn a user-supplied photograph into a restrained editorial evidence ledger: preserve one truthful photo window, then extract exactly three traceable visual facts as labeled geometric, interval, and color specimens on quiet paper. Use for architecture, travel, landscape, street, object, food, and documentary photos when the user wants a clean archival poster, visual field note, source-derived index, or photo-plus-analysis composition without redrawing or filtering the original image."
---

# Photo Evidence Ledger

Generate a finished raster poster by default. Treat the source as a record and the added marks as a compact visual index, not as decorative abstraction.

Return the image, selected layout, and a short Chinese rationale. Reveal the final prompt only when requested.

## Non-Negotiable Identity

Every result must contain:

1. One portrait 2:3 flat paper canvas.
2. One recognizable, naturally colored photographic window occupying roughly 34-56% of the canvas.
3. Exactly three evidence entries labeled `E1`, `E2`, and `E3`.
4. One geometry specimen, one interval specimen, and one color specimen, all visibly traceable to the source.
5. One source-derived chromatic ink and a neutral charcoal/gray support system.
6. A compact title and one short factual descriptor line.
7. Roughly 42-62% quiet paper with no decorative filler.

The poster must read as:

```text
source photograph -> selected fact -> reduced mark -> indexed evidence
```

It must not read as an infographic, mood board, scrapbook, or generic abstract-art diptych.

## Read the Photograph

Build an Evidence Card:

- **Subject fact:** the element that makes this photograph identifiable.
- **Spatial axis:** one horizon, lean, edge, route, silhouette, or framing line.
- **Interval fact:** a real rhythm such as windows, posts, figures, waves, lights, gaps, rooflines, or object spacing.
- **Color fact:** one meaningful hue and the exact source element carrying it.
- **Scale cue:** one relation that reveals near/far, large/small, or object/context.
- **Source facts:** three photographic details that must remain unchanged.
- **Discard:** texture and objects that do not belong in the ledger.

Reject a candidate evidence mark if it cannot be pointed back to a visible source fact.

## Build Exactly Three Entries

### E1 - Geometry

Reduce one source axis or silhouette into one to three flat neutral marks. Preserve its direction, proportion, and one identity cue. Do not trace a complete object or draw a miniature scene.

Examples: a roof pitch plus doorway gap; a shoreline bend; a bridge deck and one pier; a figure lean and one arm angle.

### E2 - Interval

Translate one real rhythm into three to seven unequal marks. Preserve the source ordering and relative spacing; remove surface detail. Leave at least one conspicuous gap so the entry does not become a pattern.

Examples: window spacing, people heights, posts, lights, waves, tree clusters, dumplings, or table objects.

### E3 - Color

Use one exact source hue as one opaque swatch, short band, or filled source-derived shape. Add at most two tiny neutral adjacency marks to show what the color touched or opposed in the photograph.

The color entry must be clearly larger than a registration dot but smaller than E1. Do not create a palette row with several hues.

## Select One Layout

Choose exactly one layout from source orientation and visual weight.

### Horizon Ledger

Use for landscapes, streets, bridges, skylines, crowds, and horizontal movement.

- Place the photograph across the upper 40-50%.
- Arrange E1-E3 as three unequal horizontal entries below it.
- Align only one evidence edge with the source horizon; offset the others.
- Keep a quiet lower or side margin for the title and descriptor.

### Vertical Specimen

Use for towers, people, trees, doors, signs, and strong upright forms.

- Place a tall photo window on the left or right, occupying 42-56% of the canvas.
- Stack E1-E3 on the opposite side with unequal heights and generous separation.
- Let E1 carry the vertical direction; keep E2 and E3 subordinate.
- Place the title near the lowest quiet interval, not above the photo as a headline.

### Object Register

Use for food, tools, flowers, domestic objects, vehicles, pets, and compact scenes.

- Place one compact photo window off-center, occupying 34-44%.
- Arrange E1-E3 around one or two sides, never as a symmetrical grid.
- Keep the object identity entirely photographic; evidence entries may simplify relations but may not redraw the whole object.
- Preserve one large continuous paper field of at least 30% of the canvas.

## Photo Integrity

Keep the source photograph recognizable and factual. Preserve perspective, subject identity, natural colors, and the three selected source facts.

Use one clean rectangular crop or one gently torn crop with restrained fibers. Never apply a full-image filter, repaint the photo, create a photorealistic duplicate, place photo pixels inside evidence marks, or repeat the photo in thumbnails.

The evidence entries are newly rendered flat marks. They must not contain photographic texture.

## Color and Material

Use warm white, cool white, pale gray, or a source-compatible neutral paper. Keep paper texture faint and continuous.

Use charcoal, graphite gray, or brown-black for E1, E2, labels, and most text. Select one exact high-chroma source hue for E3 and optionally the title or one short rule. The added chromatic area should occupy roughly 1-3% of the poster.

Render entries as dry letterpress, flat gouache, risograph ink, or clean cut paper. Choose one primary material. Keep the poster orthographic and flat scanned, without cast shadows or floating layers.

## Type System

Unless the user requests no text, include exact text for:

- a one-to-four-word title;
- one descriptor line of three to eight short tokens;
- the labels `E1`, `E2`, and `E3`.

If the user supplies wording, reproduce it verbatim. Otherwise author a concrete title from the source relation and a descriptor such as `shape / interval / color`. Do not invent dates, coordinates, brands, scientific measurements, or provenance claims.

Use small book serif, typewriter, or monospaced type. Keep labels legible and consistent. Do not add paragraphs, legends, axes, charts, logos, or a large headline.

## Prompt Compiler

Compile four compact paragraphs, normally 150-230 words:

1. **Canvas and layout:** portrait 2:3, paper, selected layout, photo share, and quiet-space structure.
2. **Photographic record:** crop, subject fact, and three source facts that must remain accurate.
3. **Evidence ledger:** exact E1 geometry, E2 interval, E3 hue/form, title, descriptor, labels, hierarchy, and eye path.
4. **Reproduction and exclusions:** one material process, flat scan, and hard avoids.

Always include:

```text
Keep the supplied photograph as one recognizable, naturally colored photographic window. Do not repaint, stylize, duplicate, or place photographic pixels inside the evidence entries.
Create exactly three labeled entries: E1 geometry, E2 interval, and E3 color. Every mark must be traceable to a visible source fact; no arbitrary abstract decoration.
```

Write only visible-pixel instructions. Do not mention analysis, skill names, API details, file paths, or checklist wording.

## Generate and Revise

Use the supplied photograph as the required edit reference. If the user specifies an image provider, follow that provider's instructions for generation, credentials, output paths, and validation. Otherwise use the image-generation workflow available in the current environment.

Inspect normal and thumbnail views. Regenerate at most once for one observed defect:

- **Photo changed or duplicated:** restore one factual photo window and remove all photographic copies.
- **Entries are generic decoration:** replace each with the exact selected source fact.
- **Too many entries or marks:** restore exactly E1-E3 and simplify each to its allowed count.
- **Poster looks like an infographic:** remove legends, axes, charts, and boxed modules; restore uneven editorial spacing.
- **Color became a palette:** keep one source hue in E3 only.
- **No hierarchy:** make the photo primary, E1 secondary, and E2/E3 subordinate.
- **Text is dominant or false:** reduce scale and remove invented metadata.

## Hard Avoids

Avoid photo filters, photo duplication, grids of thumbnails, photo-filled shapes, complete traced drawings, four or more evidence groups, charts, axes, arrows, legends, fake measurements, arbitrary geometry, multiple color chips, detached swatches, dense labels, large headlines, scrapbook layers, tape, stickers, cast shadows, curled paper, 3D mockups, cinematic grading, neon, logos, watermarks, and illegible pseudo-writing.

## Quality Gate

Verify:

- The photograph remains recognizable, natural, and singular.
- Exactly E1, E2, and E3 are present and legible.
- E1 is geometry, E2 is interval, and E3 is one source hue.
- Every evidence mark maps to a visible source fact.
- Photo, evidence, type, and quiet paper form a clear hierarchy.
- The result feels like an authored editorial record, not a template or infographic.

## Output

```markdown
![Photo Evidence Ledger](absolute-image-path-or-rendered-image)

**编排说明**

[用简短中文说明照片证据、E1 几何、E2 间隔、E3 色彩及其版式关系。]

**布局**

[Horizon Ledger / Vertical Specimen / Object Register]
```
