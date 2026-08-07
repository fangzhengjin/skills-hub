---
name: scene-distillation-zine-v1-3
description: "Transform a user-supplied photo into an expressive minimal zine poster made only from original source-derived illustration, an artistic proposition, emotional tension, visual metaphor, spacious negative space, art-directed high-chroma color, and unconstrained authorial typography. Let wording, language, amount, placement, type voices, scale, direction, legibility, and image interaction follow expression and aesthetic judgment rather than presets. Preserve source orientation by default with a 3:5 portrait output or 5:3 landscape output. Add source-derived distributed supporting accents and a natural isolated-contour option alongside adaptive paper-edge transitions. Support an exact `单色块模式` trigger for one contiguous saturated color field with all remaining forms in neutral ink. Use for authored abstract or editorial reinterpretations that communicate an emotion or idea without embedding, cropping, tracing, or preserving the original photographic material in the final image."
---

# 影像蒸馏 · Scene Distillation Zine v1.3

**作者 / Author：Zeejay0**

Turn a supplied photo into an independently compelling paper-poster artwork. Treat the photo as semantic evidence and creative stimulus, never as a visual layer in the final image.

Return:

1. the generated raster image;
2. a concise Chinese explanation of the creative idea;
3. concise art-direction notes.

Do not display the generation prompt. After generating, deliver directly without visual inspection, quality-gate review, or automatic regeneration, unless the user explicitly asks for a check or a revision.

## Decision Priority

Resolve conflicts in this order:

1. Establish one specific artistic proposition and embody it visibly.
2. Build one central emotional or conceptual tension from the source.
3. Create a complete artwork with an independent aesthetic voice.
4. Preserve the source's semantic nucleus and emotional provenance.
5. Recompose, simplify, exaggerate, and invent with purpose.
6. Establish figure–ground clarity, hierarchy, balance, and a deliberate eye path.
7. Make edge, material, color, space, and typography serve the proposition.
8. Preserve substantial quiet space and one interpretive opening.
9. Apply the requested color mode faithfully and use high chroma with purpose.
10. Keep the result tactile, flat, poetic, and non-commercial.

Do not treat this as photo filtering, style transfer, rotoscoping, or a literal illustrated copy.

## Consent and Source Handling

- Treat a supplied photo plus a request to transform or generate as consent to use image generation; do not ask again.
- Use the photo as a reference image for semantic and visual analysis only.
- Send only the final prompt and required reference image to the image-generation service.
- Do not browse, search, share, or upload the source elsewhere.
- Do not save the source into project files unless the user asks.
- State briefly after generation that the prompt and reference image were used by the generation service.

## Build the Distillation Card

Inspect the photo before composing. Resolve:

- **Semantic nucleus:** the smallest subject, relationship, or event that gives the source meaning.
- **Core subject:** one primary subject, or at most two inseparable subjects.
- **Supporting elements:** one to three elements that establish place, season, action, or atmosphere.
- **Dominant gesture:** the strongest gaze, lean, curve, diagonal, path, repetition, convergence, or movement.
- **Spatial cue:** one source relationship worth preserving, such as near/far, above/below, facing, overlap, enclosure, or direction.
- **Visual-weight map:** weight from area, darkness, saturation, faces, isolation, edge tension, and texture.
- **Native palette:** dominant hue family, temperature, value range, and any meaningful minor color.
- **Material and weather:** water, snow, haze, glass, foliage, stone, fabric, wind, rain, or light behavior.
- **Emotional residue:** the feeling that remains after factual description is removed.
- **Discard list:** background detail, clutter, redundant objects, and realistic information that should disappear.
- **Transformation opportunities:** forms that can be enlarged, merged, fragmented, repeated, displaced, or turned into negative space.

Preserve only two to four source anchors. Do not preserve the original composition by default.

## Expression Engine

Build the artwork through this chain:

```text
source fact → emotional residue → expressive proposition → central tension → visual metaphor → formal embodiment → interpretive opening
```

### Expressive Proposition

Write one internal sentence stating what the artwork asks the viewer to feel, notice, or reconsider. Make it relational and source-specific.

Prefer propositions such as:

- a small figure meets a scale too large to master, yet does not appear defeated;
- shelter and isolation exist in the same enclosing form;
- an ordinary object carries memory through a changing place;
- an opening promises freedom while also marking separation.

Avoid generic labels such as “quiet,” “healing,” “nostalgic,” “dreamy,” or “beautiful” unless the visible structure explains why that feeling exists.

### Central Tension

Choose one primary opposition that already exists or can credibly emerge from the source:

- intimacy / distance;
- shelter / confinement;
- movement / stillness;
- smallness / vastness;
- warmth / coldness;
- memory / disappearance;
- order / growth;
- visibility / concealment;
- permanence / fragility.

Optionally use one subordinate tension. Do not stack several unrelated themes. Express tension through scale, interval, direction, overlap, enclosure, interruption, temperature, value, or material contrast rather than explanatory copy.

### Visual Metaphor

Transform one source-derived object, spatial relationship, material behavior, or gesture into the central metaphor. Preserve enough specificity that the metaphor feels discovered in the photograph rather than imposed afterward.

Allow an object to shift function: a vessel may carry memory, a window may become a psychological boundary, snow may protect and erase, a mountain may become distance, a branch may become time, or a vehicle may become migration. Treat these as reasoning examples, never fixed symbol assignments.

Use one central metaphor only. Avoid universal-symbol clichés, over-symbolization, and arbitrary surreal additions.

### Formal Embodiment

Make every major formal choice perform part of the proposition:

- **Scale and space:** express power, vulnerability, distance, solitude, release, or duration.
- **Direction and rhythm:** express approach, resistance, drift, repetition, interruption, or return.
- **Boundary and edge:** express separation, rupture, accumulation, fading, passage, or breakthrough.
- **Color:** act as an emotional event such as warmth arriving, a wound opening, a signal calling, distance deepening, or life persisting.
- **Material:** let torn fiber, dry ink, grain, cut paper, and broken contour carry psychological meaning, not surface decoration.
- **Typography:** expand, redirect, or gently complicate the image; do not merely caption what is visible.

Remove any element whose only function is to make the image look artistic.

### Interpretive Opening

Resolve the artwork's emotional direction but leave one relationship unanswered. Give the viewer enough visual evidence to enter the work without fixing a single literal explanation. Let ambiguity arise from a meaningful omission, obstruction, scale shift, incomplete action, or text–image gap rather than random obscurity.

## Authorial Reinterpretation

Use the source as a starting point, not an answer.

Allow:

- changing scale, proportion, crop, spacing, orientation, and placement;
- reorganizing the original spatial relationship;
- merging several elements into one new visual mass;
- splitting, repeating, extending, or rhythmically compressing an element;
- deleting the realistic background and retaining only suggestive traces;
- exaggerating gesture, distance, direction, silhouette, or material behavior;
- letting forms cross, disappear behind, or break through torn-paper boundaries;
- turning wind, water, light, shadow, snow, or motion into abstract fields and marks;
- inventing source-consistent supporting forms that were not literally visible;
- redesigning the palette to improve hierarchy and emotional force;
- writing a short text from the image's concrete cues or emotional residue.

Every invented addition must do at least one job:

- extend the source emotion;
- clarify the subject relationship;
- establish rhythm;
- balance visual weight;
- guide the eye;
- strengthen the central metaphor.

Remove additions that exist only to make the result look "designed." Do not default to dots, grids, tape, stamps, coordinates, crosses, English fragments, or geometric ornaments.

The finished artwork must stand on its own without the source. When compared with the source, the connection should feel subtle, specific, and credible.

## Abstraction and Illustration Grammar

Use **editorial abstraction** by default:

- preserve the semantic nucleus, dominant gesture, and one source-specific cue;
- remove roughly 65–90% of descriptive detail;
- replace realistic rendering with simplified masses, broken contours, paper fragments, sparse marks, or print fields;
- generalize facial identity unless the user explicitly requests likeness;
- change anatomy or perspective when it improves the artwork without breaking the semantic nucleus.

Choose one primary grammar and at most one supporting grammar:

- **Cut-paper mass:** irregular flat shapes carry the subject and visual weight.
- **Dry-print silhouette:** one broad inked mass preserves gesture or profile.
- **Broken contour:** interrupted lines preserve direction, posture, or structure.
- **Rhythm field:** repeated marks compress crowds, leaves, waves, snow, windows, or movement.
- **Fragment stack:** two or three overlapping paper forms distribute subject and setting.
- **Orbit or drift:** selected forms leave a central cluster along a source-derived path.

Avoid complete outlines, evenly rendered detail, realistic shading, polished vector characters, cute cartoon, kawaii, anime, and children's-book sweetness unless explicitly requested.

## Composition Director

Preserve the source orientation unless the user requests another ratio:

- use a vertical 3:5 canvas for a portrait source;
- use a horizontal 5:3 canvas for a landscape source;
- use a vertical 3:5 canvas when the source is square, absent, or its orientation is ambiguous.

Treat orientation as part of the source's spatial logic, not merely an export setting. Recompose freely inside the selected canvas; do not retain the photographic framing or enlarge the illustration merely to fill a landscape format.

Start with:

- 68–85% quiet paper;
- one active illustration cluster occupying about 12–32% of the canvas;
- one dominant mass, one to three supporting forms, and one restrained texture field.

Correct these ranges by actual visual weight. A dark face-sized form may outweigh a much larger pale field.

Choose a composition family from the source geometry:

- **Asymmetric island:** a compact off-center cluster surrounded by breathing room.
- **Torn window:** an irregular paper boundary contains the main forms while one element escapes.
- **Directional drift:** forms extend along a gaze, path, wind, shoreline, or motion vector.
- **Rhythmic circulation:** repeated elements create an open loop or current without defaulting to a perfect circle.
- **Staggered fragments:** two or three separated paper pieces establish sequence and interval.
- **Vertical tension:** a low or high subject mass is counterbalanced by a distant light mark or strip.
- **Auxiliary constellation:** isolate one core subject, then disperse a source-derived supporting element around it as unequal visual beats that establish rhythm, scale, and eye path.

Apply:

- figure–ground clarity;
- asymmetric balance;
- dominant–subordinate hierarchy;
- optical rather than mechanical centering;
- Gestalt proximity, continuation, and closure;
- scale and interval contrast;
- directional breathing room;
- an eye path with a clear entry, focal encounter, movement, and quiet exit.

Choose and adjust the layout through visual weight, figure–ground tension, movement, rhythm, scale, interval, and color balance. Treat composition families as starting grammars, not templates. Do not center by habit or split the canvas evenly.

## Transition Edge Director

Choose one primary edge treatment from the source geometry, material mood, and expressive proposition. The primary choice may be an intentionally quiet natural isolation with no visible transition effect. Optionally add one subordinate treatment only when it clarifies depth, movement, or transition. Never apply every treatment in one image.

- **Torn-fiber edge:** use irregular exposed fibers and broken paper contours to divide active illustration from blank paper.
- **Layered grayscale edge:** place two or three very narrow, irregular neutral-value bands along a torn boundary—light gray, mid gray, and restrained charcoal—to create shallow material separation without a cast shadow.
- **Stippled dissolution:** let sparse dots, halftone flecks, or broken grain loosen the edge into the surrounding paper; derive density and direction from the source movement.
- **Irregular mark edge:** use one to three small, source-derived graphic shapes along the transition to continue rhythm or direction; keep them neutral and subordinate, never generic decoration.
- **Natural isolated contour:** retain only the originally illustrated subject and necessary supporting elements, with clean organic silhouettes that meet the paper directly. Use faint ink bite or paper grain at the contour only when needed. Do not add a torn boundary, grayscale rim, stipple field, halo, border, or other visible transition device.

For every treatment:

- align the transition with a source-derived horizon, gesture, path, pressure, material change, or directional break;
- use positive and negative shapes, and allow internal paper gaps;
- let zero to two selected forms cross the boundary when continuation helps;
- keep shallow depth tactile and flat-scanned;
- keep all boundary marks neutral in Solid Color-Block Mode.

Avoid a single generic ripped rectangle, using all edge treatments together, decorative symbol scattering, scrapbook layering, tape, floating paper, heavy cast shadows, curled paper, bevels, and realistic 3D depth.

Natural isolated contour borrows the visual logic of a clean cutout, not photographic pixels. Keep every retained form newly illustrated. Avoid sticker-like outlines, hard digital clipping, fuzzy selection halos, and photorealistic cutout fragments.

## Color Mode Policy

Use **Standard Accent Mode** by default.

Before selecting a hue, resolve a **Color Decision**:

- **Visual role:** focal entry, counterweight, bridge, spatial field, or directional cue.
- **Source relation:** resonance, analogous harmony, temperature counterpoint, or focused complement.
- **Value contrast:** how light or dark the color must be against paper and neutral ink.
- **Chroma:** how strongly it must separate from subdued or neutral forms.
- **Material form:** risograph ink, opaque cut paper, flat silhouette, dry-print block, or another paper-native treatment.
- **Area and adjacency:** how much color is needed and which form it must touch or oppose.

Do not default to blue or any fixed palette. Choose the hue that best serves the source, composition, emotional temperature, and eye path. Interpret “sophisticated color” as deliberate hue–value–chroma control and material fit, not as a fashionable color name.

Valid choices include, but are not limited to:

- fully saturated cobalt-blue risograph ink;
- opaque ultramarine cut paper;
- vivid pear-green flat silhouette;
- clean tomato-red printed block;
- lemon-yellow dry-print field;
- saturated magenta-pink paper mass;
- clear orange letterpress shape.

Switch to **Solid Color-Block Mode** only when the user's request contains the exact trigger:

```text
单色块模式
```

Example invocation:

```text
用 $scene-distillation-zine-v1-3 的单色块模式处理这张图片
```

Do not infer Solid Color-Block Mode merely because the source or desired poster is minimal. If the trigger is absent, remain in Standard Accent Mode.

## Standard Accent Mode

Analyze hue, value, and chroma separately. Keep the paper and most illustration inks subdued, then use one unmistakable high-chroma hue.

Choose the accent by function:

- **Source resonance:** intensify a meaningful minor source color.
- **Temperature counterpoint:** add warm color to a cool source or cool color to a warm source.
- **Focused complement:** use a complementary or near-complementary hue to sharpen the focal relationship.
- **Quiet harmony:** use a stronger analogous hue when unity matters more than tension.

Specify an exact hue and material form. Never choose a hue merely because it appeared in an example.

Give the accent one primary role:

- focal pin;
- counterweight;
- bridge between fragments;
- directional cue;
- rhythmic beat.

Keep the total high-chroma area around 0.8–3% of the full poster or 10–30% of the active cluster. Use one main accent and optionally one or two smaller echoes; keep all echoes together below 25% of the total accent area.

State the intended eye path through the accent. Do not add a bright shape without compositional reason. Do not weaken the accent with pale, muted, faded, pastel, or low-saturation wording unless requested.

### Distributed Supporting Accent

Use this Standard Accent strategy only when the source contains a meaningful repeatable supporting element such as flowers, leaves, fruit, birds, small lights, stones, windows, tools, or another recognizable motif whose color contributes to place, emotion, season, or narrative.

- Preserve the element's identity and color direction, then redraw it in the selected illustration grammar.
- Disperse several instances around the core subject with unequal scale, interval, orientation, and density.
- Use one exact high-chroma hue across the entire dispersed set so it reads as one color system, not multiple competing accents.
- Let the dispersed elements establish entry, circulation, counterweight, and exit; do not arrange them as an even decorative border or repeating pattern.
- Keep the combined saturated area within the Standard Accent allowance. A distributed set replaces the usual main accent plus echoes; it does not add another color system.
- Preserve meaningful absence. Leave some intervals open so the viewer completes the rhythm.

Do not invent a dispersed motif when the source lacks a credible supporting element. Avoid confetti, arbitrary petals, decorative scattering, equal spacing, identical copies, and color points unrelated to the expressive proposition.

## Solid Color-Block Mode

When `单色块模式` is triggered, use exactly three color categories:

1. the natural paper tone;
2. one unified achromatic or near-neutral ink system for every outline, object, texture, and text;
3. exactly one contiguous, fully saturated color field.

Apply these constraints:

- Render all non-accent forms with charcoal, graphite, warm gray, brown-black, or off-black ink only.
- Do not use subdued blue, green, red, yellow, violet, or other chromatic tints in supporting forms.
- Use one high-chroma hue in one connected filled shape; do not split it into echoes, dots, stripes, or separate colored objects.
- Let the color field occupy roughly 3–12% of the full poster or 25–65% of the active cluster.
- Keep the field visually solid and opaque. Allow paper grain, ink bite, and tiny print defects inside it, but preserve its continuous color read.
- Use the field as a subject, aperture, window, doorway, sun, body of water, silhouette, interior space, or other source-derived core form.
- Make the field the visual entry point or the central spatial idea, not a decorative rectangle placed beside the artwork.
- Derive its silhouette and placement from the source's semantic nucleus, dominant gesture, or strongest figure–ground opportunity.
- Typography, if present, may use the neutral ink system, the single saturated hue, or both; do not introduce any additional hue.

Choose the hue through the Color Decision above. It may be cobalt blue, ultramarine, pear green, tomato red, lemon yellow, magenta-pink, orange, or another exact high-chroma print hue when visual analysis justifies it.

In the final prompt, state:

```text
Color mode: Solid Color-Block Mode. Use exactly one contiguous [exact hue] field. Render every other printed form in neutral charcoal, graphite, warm gray, or off-black ink. Typography may use the neutral ink system and/or [exact hue], but no other chromatic color may appear anywhere.
```

Do not confuse this mode with monochrome illustration plus several small color accents. The defining feature is one whole saturated color mass against a unified neutral drawing system.

## Typography Director

Treat text as fully free authorial material.

Do not impose a preset language, word count, character count, copy length, font family, font consistency, alignment, hierarchy, baseline, direction, placement, color relationship, degree of completion, or legibility threshold. Use English, Chinese, bilingual material, invented language, marks, fragments, repeated words, long passages, or no text according to what gives the artwork its strongest expression and aesthetic character.

The text may become a caption, countervoice, title, interruption, visual rhythm, architectural form, surface texture, field, path, quotation, private notation, or the image's primary subject. It may be tiny, oversized, cropped, scattered, stacked, rotated, curved, obscured, fragmented, overwritten, or materially mixed. It may use one type voice or many, and may enter, leave, overlap, hide behind, or reshape the illustration.

Make the text emotionally and visually purposeful. The only decision rule is whether its wording, material presence, and arrangement deepen the artwork's proposition, tension, metaphor, or interpretive opening. Do not default to a neat caption simply because text is present.

## Prompt Compiler

Compile only instructions that can become visible pixels. Label the supplied photo as a **semantic reference only** and explicitly prohibit photographic material in the result.

Write the final prompt in five compact sections:

1. **Expression and visible consequence:** artistic proposition, central tension, visual metaphor, interpretive opening, and the visible formal decisions that embody them.
2. **Canvas and attention geometry:** source-responsive orientation, 3:5 portrait or 5:3 landscape ratio, paper, quiet-space share, cluster size, position, hierarchy, eye path.
3. **Distilled subject and creative rewrite:** semantic nucleus, preserved anchors, transformations, omissions, invented source-consistent forms, illustration grammar.
4. **Transition edge, color mode, and text:** selected edge treatment and its semantic role; exact hue, emotional action, form, position, and area; mode-specific exclusions; any authorial text material and its visual role, physical behavior, spatial movement, and relationship to the image.
5. **Reproduction and hard avoids:** print/scan texture, emotional temperature, no-photo rule, and prohibited aesthetics.

Use decisive language. Say what must disappear as clearly as what must remain.

Always include:

- `Do not reproduce, embed, crop, collage, trace, or retain photographic pixels or photorealistic regions from the reference.`
- `The final image must contain original illustration, paper, and typography only.`

## Generation Workflow

1. Inspect the supplied photo.
2. Detect source orientation and choose 3:5 portrait or 5:3 landscape unless the user requests another ratio.
3. Build the Distillation Card.
4. Write one expressive proposition from a specific source relationship.
5. Choose one central tension and one source-derived visual metaphor.
6. Define the interpretive opening: what remains deliberately unresolved.
7. Detect the exact `单色块模式` trigger; otherwise select Standard Accent Mode.
8. Select two to four source anchors and write the discard list.
9. Define one authorial transformation: what the artwork does that the photograph did not.
10. Choose the composition family and use scale, interval, enclosure, direction, and quiet space to embody the proposition. Use Auxiliary Constellation only when a source-derived supporting motif can carry rhythm or meaning.
11. Choose one primary illustration grammar and at most one supporting grammar.
12. Choose one primary transition-edge treatment by semantic function and, only if useful, one subordinate treatment. Allow Natural Isolated Contour when an unmarked boundary best serves the work.
13. Resolve the Color Decision and define the accent as an emotional action, not merely a hue. In Standard Accent Mode, decide whether the accent is concentrated or a source-derived Distributed Supporting Accent.
14. Resolve color by mode:
   - Standard: choose the accent hue, role, form, position, area, and restrained echoes.
   - Solid Color-Block: choose one connected saturated field and convert every other printed form to neutral ink.
15. Decide freely whether the work needs text. If it does, invent or use any language, amount, type voice, material treatment, scale, orientation, hierarchy, and placement that strengthens the work; do not default to a neat caption line or impose a preset textual format.
16. Compile the five-section prompt.
17. Generate using the supplied image as a semantic reference.
18. Return the image, the creative idea in Chinese, and concise art-direction notes directly.

Generate by default. Stop at prompt-only only when the user explicitly asks.

## Hard Avoids

Avoid original photo fragments, photorealistic regions, photo windows, tracing, rotoscoping, literal full-scene illustration, exact composition copying, generic mood labels without visible embodiment, decorative metaphors, universal-symbol clichés, random ambiguity, overly faithful anatomy, realistic shading, cute cartoon, kawaii, anime, children's-book styling, polished vector characters, generic abstract motifs, arbitrary dots or grids, unsupported decorative scattering, evenly repeated color motifs, sticker-like cutout outlines, fuzzy selection halos, decorative stamps, tape, multiple competing bright hues, dense scrapbooking, commercial advertising hierarchy, logos, CTA, glossy mockups, curled paper, hard shadows, 3D, cinematic lighting, depth of field, neon, fashion-editorial drama, and watermarks. In Solid Color-Block Mode, additionally avoid supporting color tints, multiple colored regions, accent echoes, and a color field that reads as a detached decorative swatch.

## Output Format

````markdown
**生成图**

![Scene Distillation Zine poster](absolute-image-path-or-rendered-image)

**创作想法**

[In concise Chinese, explain the expressive proposition, central tension, source-derived visual metaphor, the meaning carried by composition/color/material/text, and the deliberate interpretive opening. Describe the artwork rather than hidden generation instructions.]

**艺术指导**

- Distillation: [semantic nucleus / preserved anchors / discarded reality]
- Expression: [artistic proposition / central tension / interpretive opening]
- Authorship: [recomposition / visual metaphor / exaggeration / invention]
- Composition: [family / hierarchy / eye path / quiet-space share]
- Edge: [primary treatment / optional subordinate treatment / structural role / depth or dissolution behavior]
- Color: [mode / exact hue / form / role / position / approximate area / exclusions]
- Text: [authorial text material / visual role / type and material behavior / hierarchy or anti-hierarchy / image interaction / placement]

[After only the first or second successful generation by this skill in the current conversation:]
*若公开分享，欢迎标注：Visual Skill by @Zeejay0*
````

If the generated image renders without a local path, show it normally and still include the creative idea and notes. Do not reveal the generation prompt.

Count successful image generations made by this skill within the current conversation. Append the sharing credit only after the first and second successful generations; omit it from the third and all later generations. Start the count again in a new conversation because the skill has no persistent cross-conversation state. Use `若公开分享，欢迎标注：Visual Skill by @Zeejay0` for Chinese responses and `If shared publicly, credit is appreciated: Visual Skill by @Zeejay0` for English responses. Keep it as the final, visually quiet line outside the image. Do not turn it into a heading, call to action, repeated promotion, hyperlink, or image watermark. Omit it when the user explicitly asks for no credit line in the response.
