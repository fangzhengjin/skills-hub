---
name: street-photo-illustration
description: Transform people in uploaded street, travel, lifestyle, casual, or commercial-space photos into clean BLACK INK or colorful editorial-chibi illustrations while preserving the original photographic environment, pose, clothing, accessories, and scene relationships. Use when the user asks to illustrate, cartoonize, or create a photo-plus-character editorial treatment from real photos, with optional environment-aware typography and doodles.
---

# Street / Travel Photo Character Illustration Skill

For execution-ready prompt scaffolding, read the matching template in `prompts/black_ink_template.md` or `prompts/color_chibi_template.md` after selecting a mode.

## Purpose

Transform only the people in an uploaded street photo, travel photo, casual snapshot, lifestyle photo, or commercial-space photo into one of two illustration treatments while preserving the original photographic environment.

Core visual language:

> real photographic environment + illustrated person + optional environment-aware typography + light doodles

This is a **character-replacement workflow**, not a full-image illustration workflow.

Default output ratio: **3:4 vertical**, unless the user explicitly requests another ratio.

---

## 1. Highest-Priority Rules

1. **Transform people only.** The environment stays photographic.
2. **Replace, do not duplicate.** By default, the real person disappears and the illustrated person occupies the same position. Do not keep a real person plus a second illustrated copy unless explicitly requested.
3. **Preserve the source person without preserving realistic facial detail.** Maintain action, body direction, pose, hairstyle silhouette, clothing, clothing color, accessories, shoes, bags, glasses, hats, and handheld objects as faithfully as possible. In both modes, reduce the face to an abstract dot-eye language rather than drawing a portrait.
4. **Preserve the source environment.** Architecture, streets, interiors, furniture, landscape, sky, vegetation, vehicles, lighting, perspective, depth, and photographic relationships remain unchanged.
5. **References are style-language only.** Never reproduce a reference image's specific person, face, clothing, pose, location, composition, props, camera angle, title, or element placement.
6. **Typography is optional and secondary.** The first visual layer is always the original photographic environment plus the transformed person.
7. **Typography must respond to the environment.** When text is used, its lettering style, placement, scale, and copy should feel connected to the actual place rather than pasted on as a generic template.
8. **COLOR CHIBI is abstract, not babyish.** The face can be extremely simplified, but the body must still inherit the source photo's posture, silhouette, and length relationships.

---

## 2. Source Analysis

Before rendering, analyze the uploaded photo for:

- number of people
- exact person positions
- action and pose
- limb direction
- torso lean
- head direction
- hairstyle and hair color
- clothing silhouette and clothing color
- shoes
- bags, hats, glasses and key accessories
- handheld objects
- person-to-person spacing and interaction
- environment boundaries
- photographic lighting and perspective
- environment category and mood
- negative space suitable for typography
- whether typography is useful at all
- whether the subject reads as adult, teen, or child
- whether the person's appeal depends on long limbs, fashion attitude, or a specific pose silhouette

Recommended internal flow:

`photo_analysis -> character_lock -> mode_selection -> character_conversion -> text_mode -> typography_plan -> doodle_plan -> final_composition`

---

## 3. Mode A — BLACK INK

### Goal

Replace the source person with a **clean black-and-white hand-drawn illustration character** integrated into the unchanged real photo.

### Character Lock

Pose preservation is strict. Keep as closely as possible:

- body position
- hand position
- leg position
- torso angle
- head direction
- standing / sitting / walking / jumping state
- hairstyle
- clothing structure
- accessories and handheld objects
- spacing between multiple people

### Rendering Language

- clean black illustration linework
- visible but restrained hand-drawn quality
- strong structural clarity
- **pure white fill as the dominant interior base**
- minimal gray only when needed for form separation
- crisp silhouette
- clear white sticker-like outer separation from the photo
- natural hand-drawn warmth without messy sketch texture
- abstract editorial-character language rather than portrait sketching
- preserve the hairstyle through its outer silhouette and only a few structural hair lines
- use line economy: prioritize the outer silhouette and large clothing boundaries; keep internal description sparse
- retain only essential garment openings, cuffs, hems, pockets, and accessory contours; simplify folds into a few decisive marks

### Detail Budget — Mandatory

- render large shapes before small information
- use only a few internal structure lines per clothing region; do not trace every fold from the photo
- reduce hair to a solid or near-solid graphic mass with minimal directional marks
- simplify hands and shoes into clean readable shapes without knuckle, sole, lace, knit, or tread detail unless the held object or action would become unreadable
- preserve identity cues through silhouette and color/value placement, not surface description

### Facial Rule — Mandatory

The BLACK INK face must be as abstract as the COLOR CHIBI face:

- two small solid-dot eyes
- tiny simple mouth, or no mouth when the face is too small
- omit the nose by default; at most use one tiny dot or very short mark
- no realistic eye shape, eyelids, irises, pupils, lashes, nose bridge, nostrils, lip contours, cheek anatomy, or portrait shading
- no detailed face likeness; recognition comes from pose, hair silhouette, clothing, accessories, and context
- treat the internal face as a nearly blank symbolic surface; do not add ears, brows, smile creases, cheek curves, jaw modeling, or extra expression marks unless essential to the source silhouette
- when the source face is hidden, turned away, occluded, or too small to read, do not invent a face or facial marks

Even for close or three-quarter faces, do not increase facial detail. Keep the body silhouette faithful and adult when appropriate; an abstract face does not authorize toddler-like proportions.

### Proportion Lock — Mandatory

- match the source person's original head bounding box; do not enlarge the head
- match the original shoulder width, torso length, limb length, seated height, and overall occupied area
- adults and elderly people must retain adult or elderly body scale, posture, and weight distribution
- do not shorten legs, widen the head, round the torso, or soften the body into a generic cute mascot
- for multiple people, preserve each person's independent age impression, pose, scale, spacing, gaze direction, and interaction

### Prohibited

- dense crosshatching
- dirty pencil shading
- rough sketchbook texture
- chaotic overlapping lines
- comic-panel or manga-page treatment
- storyboard feeling
- heavy gray or black interior fill
- hyper-realistic pencil portrait rendering
- realistic or anime facial construction
- detailed eyes, noses, lips, facial planes, or individualized portrait features
- ears, eyebrows, smile creases, cheek curves, or other unnecessary internal face marks
- enlarged heads, shortened limbs, rounded mascot bodies, or age-flattened proportions
- strand-by-strand hair rendering
- stubble marks, hair-follicle dots, dense clothing folds, fabric texture, shoe tread, knit patterns, lace detail, or material hatching
- technically detailed fashion sketching or realistic garment rendering
- sterile icon/vector-only appearance

Target:

> dot-eye abstract face + clean black hand-drawn linework + white-filled figure + clear sticker integration + strict pose fidelity

---

## 4. Mode B — COLOR CHIBI

### Goal

Replace the source person with a **clear, colorful, lightly abstract editorial-chibi illustration character** integrated into the unchanged real photo.

### Core Interpretation

COLOR CHIBI does **not** mean a 2-head-tall baby cartoon.

It should feel like:

> simplified lifestyle character illustration + dot-eye facial reduction + preserved real-photo pose and body rhythm

### Allowed Abstraction

Moderate simplification is allowed:

- slightly larger head
- simplified hands and feet
- simplified facial features
- softer, cuter expression
- slightly stylized clothing shapes
- light paper / colored-pencil / printed texture when clean

Abstraction must not erase the source person's recognizable visual cues.

### Facial Rule — Mandatory

The face should be **more abstract than the body**.

Preferred facial language:

- two small dot eyes
- tiny simple mouth
- minimal or omitted nose
- light blush allowed
- no detailed iris rendering
- no glossy anime eyes
- no heavy lashes or realistic eye shading

### Body Proportion Rule — Mandatory

Q-style is **lightweight**.

Do **not** default to 2–3 head-tall proportions.

Recommended body proportions:

- adults: about **4.5–6 heads tall**
- teens: about **4–5 heads tall**
- children: about **3.5–4.5 heads tall**

Additional rules:

- head enlargement should usually stay within roughly **10%–25%** over a natural simplified proportion
- long-legged people must stay long-legged
- slim fashion-oriented subjects must remain slim and elongated
- crouching, leaning, sitting, stepping, walking, and turning poses must preserve their original silhouette logic
- limbs may be simplified but should not be obviously shortened into a doll-like shape

### Must Preserve

- action and pose logic
- body direction
- hairstyle and hair color
- clothing type and clothing colors
- bags, hats, glasses and shoes
- important accessories
- handheld objects
- relative spacing between people
- whether the person reads as elegant, sporty, outdoorsy, commercial, casual, etc.

### Rendering Language

- clear silhouette
- clean contours
- readable color blocks
- controlled simple shading
- warm friendly character design
- clear white sticker border
- a **light tactile illustration texture is allowed** if it remains clean and readable
- texture may feel softly printed, lightly colored-pencil, or paper-like, but must stay subtle
- abstract face + more faithful body silhouette

### Prohibited

- muddy watercolor wash
- thick painterly rendering
- excessive sketch lines
- rough scribble texture
- heavy crayon noise
- dirty brush buildup
- muddy colors
- blurry character edges
- oversized toddler-head proportions for adult subjects
- obviously compressed torsos or shortened legs
- so much handmade texture that clothing, pose, or face becomes unclear

Target:

> abstract dot-eye face + clean colorful character + lightly stylized but believable body proportion + preserved source-person cues

---

## 5. Environment Preservation

The following remain photographic and should not be redesigned:

- architecture
- streets and paving
- sky
- landscape
- water
- plants
- furniture
- vehicles
- stores
- interiors
- products and merchandise in commercial spaces
- objects not belonging to the transformed person
- lighting
- shadows
- depth of field
- perspective
- camera relationship

Do not beautify by replacing the location or inventing a new background.

Default principle:

> Change the person, not the world.

---

## 6. Replacement Logic

Default behavior:

`source real person -> illustrated replacement in the same location`

Do not output:

`source real person + illustrated duplicate`

unless explicitly requested as a comparison or companion-character concept.

---

## 7. Pose Fidelity

Priority order for pose matching:

1. overall body placement
2. hand positions
3. leg positions
4. torso direction and lean
5. head direction
6. action state
7. held objects
8. spacing and interaction between people
9. body-length impression (tall / petite / child / long-legged / crouched / stretched)

BLACK INK uses strict pose fidelity.

COLOR CHIBI may simplify anatomy, but must preserve the original motion, silhouette, and interaction logic.

---

## 8. Text Modes

Typography is **not mandatory**. Before adding any words, determine the active text mode.

### A. CUSTOM COPY

Use when the user provides copy.

Rules:

- preserve the user's wording as written
- do not rewrite or “improve” the copy unless asked
- the system only decides hierarchy, lettering style, scale, line breaks, placement, and integration
- user-specified Chinese, English, bilingual, punctuation, and casing take priority

### B. AUTO COPY

Use when the user wants text but does not provide copy.

Rules:

- generate copy from the actual environment, activity, mood, products, or travel context
- avoid generic repeated phrases when a more scene-specific idea is available
- title, secondary copy, and doodle notes should feel native to that place
- language follows the user's request; otherwise match the conversation language when sensible

### C. NO TEXT

Use when the user says no text / no title / clean version / pure image.

Rules:

- no main title
- no subtitle
- no decorative words
- no text stickers
- no pseudo-label copy
- only the transformed person and optional **non-text doodles** may remain

Do not force typography into NO TEXT mode.

---

## 9. Typography System — Mandatory Style Logic When Text Is Used

Typography should feel like part of the photographed environment, not a generic social-media preset.

### Visual Direction

Preferred lettering families:

- bold block lettering
- bold brush lettering
- confident hand-painted lettering
- casual marker handwriting
- simple editorial sans-serif
- compact sign-like lettering
- menu / storefront / wayfinding-inspired lettering when appropriate

Default text color is **white** for strong integration and readability. Black may be used on very light backgrounds. A small amount of environment-derived accent color may be used, but avoid decorative gradients.

### Environment-to-Type Matching

Choose typography from the scene:

- café / bakery / food: menu-board, storefront, warm hand-painted, chalk/marker feeling
- retail / boutique / commercial: bold brand-like block type, clean editorial type, window-display hierarchy
- city street / street photography: poster-like bold title, urban brush/marker lettering, restrained wayfinding cues
- travel / nature / seaside / mountain: travel-note, postcard, hand-journal, directional-note feel
- market / night market / food street: lively sign-like lettering, brush title, handwritten side notes
- gallery / museum / architecture: cleaner editorial hierarchy, restrained serif/sans or concise hand lettering
- music / record shop / skate / youth culture: stronger hand-painted, brush, sticker, label, or flyer-like energy

Do not use the exact same lettering treatment for every scene.

### Main Title Scale

The title must be visible but not overwhelm the person and environment.

Recommended:

- roughly **45%–70% of image width at most**
- roughly **10%–16% of total visual weight**
- use negative space whenever possible
- avoid covering faces or key environmental information
- do not default to a full-frame poster headline

### Secondary Decorative Copy

Decorative text should be **medium-small, clearly readable, and compositional**.

Recommended:

- each secondary text group about **2.5%–5% of visual weight**
- typically **2–4 groups** when useful
- place near relevant actions, products, signs, views, objects, or environmental features
- do not hide all notes in corners
- do not shrink text until it reads like a watermark

### Micro Notes

- about **1%–2.5% of visual weight**
- use sparingly
- optional, not required

### Hierarchy

1. real environment + illustrated character
2. main title
3. secondary decorative copy
4. micro notes
5. doodles

---

## 10. Doodles

Allowed non-text doodles include simple:

- stars
- hearts
- arrows
- lines
- circles
- waves
- sun / cloud motifs
- leaves / flowers
- sparkles
- motion marks
- underlines
- small frames
- activity-specific icons

Doodles should preferably relate to the environment or activity.

Rule:

> Doodles support mood and composition; they must not cover or clutter the photograph.

---

## 11. Decoration Intensity

### MINIMAL

- transformed character
- optional restrained title
- very few doodles

### EDITORIAL — Default

- transformed character
- environment-aware title when text mode allows
- 2–4 readable small annotations when useful
- restrained doodles

### SCRAPBOOK — Optional

May add small editorial collage elements such as:

- mini photo frame
- tape
- note paper
- small sticker shapes
- handwritten notes

Do not default to scrapbook treatment unless the photo benefits from it or the user asks for it.

NO TEXT mode overrides all text requirements in every decoration intensity.

---

## 12. Originality / Reference Safety

Style references may only communicate high-level visual grammar:

- real photo + illustrated person
- black-and-white or colorful character treatment
- typography families and hierarchy
- doodle accents
- sticker integration
- environment-aware graphic design logic

Never copy or reconstruct:

- a reference person's identity or facial design
- clothing
- pose
- environment
- architecture
- props
- camera angle
- exact composition
- exact title wording
- exact text placement
- exact doodle placement

Correct principle:

> learn the visual grammar, not the artwork content.

---

## 13. Final Quality Check

Before output, confirm:

- the original environment remains photographic
- only intended people are transformed
- no unwanted real-person duplicate remains
- pose and action still match the source
- hairstyle, clothing, colors, and accessories remain recognizable
- BLACK INK uses two dot eyes, a tiny or omitted mouth, an omitted/minimal nose, clean black lines, and mostly pure-white fill
- BLACK INK contains no portrait-style eyes, nose bridge, lips, facial planes, or detailed hair strands
- BLACK INK keeps the original head size and adult/elderly body proportions without cute enlargement or shortening
- hidden or rear-facing faces remain hidden; no face is invented
- BLACK INK uses sparse silhouette-led drawing; clothing, hair, hands, and shoes contain no dense surface detail
- COLOR CHIBI uses **dot-eye / ultra-simple facial logic** rather than detailed anime eyes
- COLOR CHIBI does not collapse adult subjects into oversized baby proportions
- COLOR CHIBI preserves long-limbed or fashion-oriented body rhythm when relevant
- COLOR CHIBI remains clear, readable, and not over-textured
- the active text mode is respected
- CUSTOM COPY has not been rewritten without permission
- NO TEXT contains no words
- if text is present, typography feels related to the environment
- title scale is controlled
- secondary text is readable but does not dominate
- doodles are restrained and context-aware
- no reference image content has been reproduced
- the final image still reads first as the user's original photograph

---

## Final Style Target

The intended result is not simply “a cartoon person on a photo.”

It should feel like:

> the user's original real-life photograph, carefully redesigned through character illustration and, when desired, environment-aware typography and light doodles — without changing the world captured by the camera.
