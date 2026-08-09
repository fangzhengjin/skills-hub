# Quality Gate

## Generated Image

Inspect the actual raster before returning it.

- The result is a vertical paper poster in the requested ratio; default is 3:5.
- Roughly 70%-90% reads as open paper.
- One main visual event occupies roughly 8%-25% of the canvas.
- The event expresses one metaphor or relation rather than a full scene.
- Paper fiber, scan, print, clipping, or specimen treatment is visibly present.
- Typography participates in the composition without becoming a commercial headline system.
- One main high-chroma anchor is visible at thumbnail scale.
- The main chromatic area is roughly 0.8%-2.5% of the canvas or 15%-35% of the visual cluster.
- The main color is not weakened by low-saturation language intended only for paper or photography.
- The chosen layout, anchor, typography, texture, and mood are recognizable in the result.
- The image avoids full-bleed, product-ad, logo, CTA, mockup, glossy, cinematic, 3D, neon, cartoon, fashion-drama, dense-scrapbook, and multicolor-template drift.
- The result does not copy source text, brand identity, watermark, signature, exact date/location, or exact composition from reference-only images.

### Input Photo Preservation

Apply these checks whenever Photo Input Mode was used:

- Every supplied image has an explicit role: edit target, reference image, or supporting insert.
- Every supplied image meant to affect the output was included in the generation call rather than used only as a textual description.
- The reported preservation level matches the user's request and the subject's identity sensitivity.
- For an edit target, the result preserves the declared visible invariants. At High preservation, identity, defining proportions, markings, product geometry, silhouette, object count, and recognizable colors do not drift materially except where the user explicitly permitted change.
- For a reference image, the result inherits only the requested visual traits and does not reproduce the source subject, wording, or exact composition.
- For a supporting insert, the requested person, object, texture, or fragment remains recognizable and occupies the intended role in the new composition.
- The final response reports photo role, preservation level, main invariants, and any remaining limitation.

If one of the central checks fails, revise the prompt and regenerate once. For edit targets and supporting inserts, prioritize preservation invariants before visual metaphor, attention geometry, main color visibility, typography, and texture. For reference-only generation, prioritize source separation before visual metaphor and the remaining style checks. If the second result still fails, return the better result and state the remaining limitation briefly; do not describe failed preservation as successful.

## Reference Analysis

- Every claimed visual trait comes from an inspected usable file.
- Exact dimension and ratio claims come from metadata when available.
- Observations and interpretations are distinguishable.
- Fixed rules are supported by repetition or clearly labeled as single-reference observations.
- Variable rules reflect real variation or are labeled as proposed safe variation.
- Sample-specific words, brands, dates, objects, and layouts are isolated as residue rather than generalized.
- The prompt names measurable visual behavior rather than only aesthetic adjectives.
- The randomization block changes composition grammar, not only subject position.
- Confidence and limitations match the number and quality of supplied references.

## Prompt-only Output

- The prompt follows the four-paragraph compiler shape.
- It includes a content-derived metaphor, not a randomly selected decorative object.
- It states cluster position and size, main hue and material form, and print/scan treatment.
- The response does not claim that an image was generated or inspected.
