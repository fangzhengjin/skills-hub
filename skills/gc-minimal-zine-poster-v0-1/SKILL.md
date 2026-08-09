---
name: gc-minimal-zine-poster-v0-3
description: Generate or analyze poetic paper-texture minimal zine posters with large negative space, a small editorial collage or visual anchor, experimental typography, and one clear color accent. Use when the user gives a theme, sentence, article, mood, object, photo, content brief, reference images, or an image folder and wants a final poster image, a production-ready image prompt, reusable style rules, or varied layouts that stay in one visual family.
---

# Minimal Zine Poster v0.3

Turn content or visual references into a coherent paper-poster system. Preserve the original production contract: unless the user explicitly asks for analysis or prompt-only output, return both a final image-generation prompt and the generated raster image.

## Route The Request

Choose the smallest mode that satisfies the request:

- **Generate Mode — default:** theme, sentence, article, object, mood, photo, or brief → visual metaphor → prompt → generated image → inspection.
- **Photo Input Mode — Generate subflow:** a supplied photograph that should affect the output → classify its role and preservation level → pass the actual image into generation → inspect both poster quality and source preservation.
- **Reference Analysis Mode:** reference images or a folder plus a request to analyze, extract, or systematize the style → evidence-based style rules and reusable prompt. Do not generate an image unless requested.
- **Prompt-only Mode:** use only when the user explicitly asks for a prompt without image generation.
- **Analyze + Generate:** when the user asks to learn from references and make a new poster, run Reference Analysis first, then Generate Mode with the extracted system.

If the intent is ambiguous but clearly asks to “做一张”, use Generate Mode. Do not stop to ask about choices the skill can make safely.

## Load The Relevant References

- Read `references/style-system.md` for every mode.
- Read `references/prompt-compiler.md` for Generate and Prompt-only modes.
- Read `references/variation-engine.md` before choosing a generation recipe or batch plan.
- Read `references/reference-analysis.md` whenever reference images or folders are supplied for analysis.
- Read `references/quality-gate.md` before returning a generated image or style analysis.

## Source And Reference Boundaries

- Inspect actual supplied images before making claims about their dimensions, ratios, layout, color, or texture.
- Separate observed traits from interpretation. Use file metadata for dimension and ratio claims when possible.
- Do not copy source text, brands, watermarks, signatures, exact dates, exact locations, or an exact composition from reference-only images.
- User-supplied text may be placed in the new poster when the user explicitly asks for it. Keep it short because image models distort long text.
- For reference-only images, learn the visual grammar rather than copying the source identity, exact subject, wording, or composition. For edit targets, preserve the declared subject invariants and change only what the selected preservation level permits.
- If files are missing or unreadable, state the limitation instead of inventing an analysis.

## Photo Input Mode

Use this mode whenever a user-supplied photograph should materially affect the generated poster. Before compiling the prompt, assign every supplied image one role:

- **Edit target:** the photograph or its recognizable subject must appear in the final poster.
- **Reference image:** use only its style, color, composition, texture, or mood; do not preserve its exact subject or identity.
- **Supporting insert:** use one specified person, object, texture, or fragment from the photograph inside a new composition.

Classify from observable wording:

- “把这张照片做成海报”, “基于这张图改”, or “保留这个人、产品、宠物” → edit target.
- “参考这张图的风格、配色、构图” → reference image.
- “把照片里的这个人或物体放进去” → supporting insert.
- A supplied photograph plus only “做一张” → edit target, because silently discarding the supplied subject is the more destructive interpretation.

Ask only when two materially different roles remain equally plausible.

Choose and record one preservation level:

- **High:** preserve identity, facial structure, body proportions, pose when relevant, defining markings, product geometry, object count, silhouette, and recognizable colors, except traits the user explicitly lists as permitted changes. Prefer an original-photo crop, clipping, or printed fragment over redrawing the subject.
- **Medium:** preserve the main subject and defining characteristics while allowing crop, scale, palette, surface treatment, and surrounding composition to change.
- **Low:** reference-only; preserve visual grammar or mood, not the source subject or exact composition.

Use High preservation for identifiable people, pets, characters, artworks, and products unless the user explicitly permits reinterpretation.

Run the photo workflow:

1. Inspect every supplied image before describing or using it. Record available dimensions, ratio, main subject, important details, and visible text or branding.
2. List concrete preservation invariants for each edit target or supporting insert. Include only traits visible in the source or explicitly supplied by the user.
3. Pass the actual input image to the built-in image-generation tool. Use `referenced_image_paths` when every target image has a local path. Use `num_last_images_to_include` when at least one target exists only in the conversation, choosing the smallest number that includes every target, up to five. Never use both mechanisms in one call. If neither mechanism can include every target, ask the user to attach the missing images again.
4. Compile the prompt with three explicit parts: what must remain recognizable, what may change, and what new poster elements may be introduced.
5. Generate the sparse vertical paper poster and inspect it against both `references/quality-gate.md` and the preservation invariants.
6. If an edit target is no longer recognizable or a required invariant drifts, regenerate once with tighter invariants and fewer permitted changes. If the second result still fails, state the preservation limitation instead of presenting it as fully successful.

## Generate Mode Workflow

1. **Parse the content.** Identify the core subject, emotional temperature, supplied text, and every input image role. When a photograph is supplied, complete Photo Input Mode before choosing the metaphor. For an article or abstract idea, reduce it to one central imageable relation rather than illustrating the whole argument.
2. **Choose one visual metaphor.** Use one object, fragment, photo crop, specimen, silhouette, printed illustration, texture window, typographic object, or small conceptual relation. Avoid a full illustrated scene.
3. **Select a variation recipe.** Choose one layout family, anchor type, typography mode, texture mode, mood, paper tone, accent hue, and decorative-mark system from `references/variation-engine.md`. Randomness must change visual grammar, not only position.
4. **Compile the prompt.** Follow the field order and four-paragraph shape in `references/prompt-compiler.md`. State the anchor position and size, exact high-chroma hue, material form, and approximate visual share.
5. **Generate the image.** Use the built-in image-generation capability. For Photo Input Mode, include the actual supplied image through the mechanism defined above. Do not return prompt-only output unless the user requested it.
6. **Inspect the actual result.** Apply `references/quality-gate.md` at full view and thumbnail scale. For Photo Input Mode, also compare the result with the source image and declared preservation invariants. If the result clearly violates the chosen recipe, loses the color anchor, becomes commercial/full-bleed, collapses into an unrelated style, or breaks required preservation, tighten the prompt and regenerate once.
7. **Return the image, final prompt, recipe, one short interpretation note, and photo role/preservation details when applicable.**

## Reference Analysis Workflow

1. Resolve the supplied files and inspect every usable image; record dimensions and ratios when available.
2. Extract repeated traits across canvas, negative space, background, subject scale, collage method, composition, typography, color, texture, decorative marks, mood, and wrong directions.
3. Distinguish:
   - **fixed system:** traits required for family resemblance;
   - **variable system:** traits that may change without breaking the family;
   - **sample residue:** words, brands, objects, dates, or layouts that belong only to individual references and must not be reused.
4. Use measurable ranges only when the files support them. Do not present a single-image trait as a collection-wide rule.
5. Return the analysis format defined in `references/reference-analysis.md`.
6. If generation was also requested, select a new recipe and continue through Generate Mode without copying a source composition.

## Variation Discipline

- Do not default repeatedly to “tiny centered photo + blue dots + microtext.”
- When several outputs are requested, change at least the layout family, anchor structure, and typography distribution between adjacent images.
- Use recent outputs only when they are visible in the current conversation or supplied batch. Do not claim memory of images outside the available context.
- Preserve one visual family through paper surface, high negative space, restrained typography, print/scan reproduction, and one dominant chromatic anchor.
- If a recipe becomes dense, remove decorative marks or secondary text before weakening the main visual metaphor.

## Output Formats

### Generate Mode

````markdown
**生成图**

![Minimal Zine Poster v0.3](absolute-image-path-or-rendered-image)

**最终 Prompt**

```text
[final prompt used for image generation]
```

**说明**

- Mode: Generate
- Recipe: [layout / anchor / typography / accent / texture / mood]
- Photo role: [edit target / reference image / supporting insert, omit when no photo was supplied]
- Preservation: [high / medium + main invariants, or low + reference traits; omit when no photo was supplied]
- [one short note about the content interpretation and any regeneration]
````

### Reference Analysis Mode

Return:

- accurate style name;
- concise Chinese summary;
- evidence-based trait analysis;
- fixed rules, variable rules, and sample residue;
- reusable prompt template and randomization block;
- negative prompt / avoid list;
- confidence or limitations when the sample is small.

### Prompt-only Mode

Return the final four-paragraph prompt, selected recipe, and negative constraints. Do not imply that an image was generated.

## Non-negotiable Outcome

A successful generation must remain a sparse vertical paper poster with one clear visual event, not a commercial ad or a generic collage template. A successful analysis must explain what stays fixed and what can change, not merely label the references “minimalist” or “clean.”

## Example Requests

- “用 $gc-minimal-zine-poster-v0-3 做一张关于雨天的图。”
- “把这篇文章提炼成一个视觉隐喻，再生成海报。”
- “分析这个文件夹里的参考图，提炼同一套视觉系统，不要复制原图文字。”
- “参考这些图先分析，再做一张关于旧书的全新海报。”
- “用这张人物照片做海报，保留人物身份和服装，只改变排版与纸张质感。”
- “只给我最终生图 Prompt，不要生成图片。”
