# PATCH v4 | Anti-AI Film Frame And Triptych Rhythm

Use this patch when generated images feel oily, over-detailed, too clean, too dirty in an artificial way, lens-poor, or conventionally stacked.

## 1. Anti-AI Image Discipline

The output should look like captured frames with optical, production, and editorial limits. It should not look like a prompt showing off all of its nouns.

Rules:
- One primary story clue, one secondary clue, and the rest can be mundane, dark, soft, occluded, or empty.
- Cap each shot at 2-3 concrete scene details plus camera position and light source.
- Reduce decorative debris, smoke everywhere, equally sharp details, shiny highlights, glossy wet surfaces, and over-designed props.
- Prefer ordinary practical locations and human timing: waiting, missing, half-turning, leaving, hesitating, looking through glass, arriving too late.
- Never use "rich detail", "highly detailed", "intricate", "epic", "dramatic", "volumetric", "beautiful", or "masterpiece" in final image prompts.

## 2. Lens-Texture Calibration

Pick one capture substrate per set:
- 35mm release print: soft gate, print density, mild color breathing, medium-low microcontrast, fine uneven grain.
- 16mm television transfer: softer resolution, chunkier natural grain, slight color bleed, imperfect exposure, documentary immediacy.
- VHS / old broadcast capture: lower fidelity, scan softness, luma noise, color bleed, unstable blacks.
- MiniDV / early digital video: small-sensor practical light, limited dynamic range, slight edge harshness.
- Surveillance / CRT / monitor rephotograph: geometry distortion, screen texture, glare, black crush.
- Long-lens film compression: restrained shallow focus, compressed figures, window or heat distortion.
- Wide/fisheye witness POV: distortion justified by camera placement inside a vehicle, doorway, crowd, checkpoint, locker room, corridor, or hiding place.

## 3. Controlled Dirt

Dirty realism means selective imperfection. Use only one dominant imperfection family per set:
- dust and dry scratches
- rain and wet reflection
- smoke and low-output lamps
- fluorescent institutional grime
- broadcast/video noise
- fogged glass or condensation
- sun-faded fabric and chipped paint

Do not combine every dirt mode in one frame.

## 4. Unconventional Triptych Rhythm

Generate three separate 2.39:1 frames, then stitch externally. Layout may be uneven:
- Classic equal stack: 1:1:1.
- Held opening: 1.25:0.9:0.85.
- Impact middle: 0.85:1.3:0.85.
- Aftertaste ending: 0.85:0.9:1.25.
- Uneven memory strip: 0.7:1.2:0.75 with 6-16px black breathing gaps.
- Broken surveillance strip: equal stack with one softer or lower-contrast mediated frame.

Use black spacing as edit rhythm, not decoration. Never ask the image model to create the collage.

## 5. Reference-Learned Frame Grammar

Useful patterns:
- Mix distant room, face fragment, mediated view, object, and nearly empty frame without explaining everything.
- Include one "boring" transitional shot when it makes the others feel real.
- Low-fi or imperfect media frames can feel more cinematic than polished film-still prompts.
- Color may shift across shots if motivated by place or medium.
- Controlled awkwardness is allowed: too much headroom, subject cut by window edge, figure far on a margin, low horizon, partial action.
- A sequence may contain one motivated special camera or light event: fisheye witness POV, water caustics, projector beam, venetian-blind shadows, car headlights sweeping through a room, surgical lamp falloff, sodium-vapor tunnel light, or mirror distortion.

## 5.1 Special Lens And Light Inserts

Use special lens or light only when it changes narrative pressure, not as visual decoration.

Rules:
- Default rhythm: two stable shots plus one special insert. Do not make all three shots visually distorted or theatrical.
- A fisheye/wide witness POV must be physically justified: camera trapped inside a car, elevator, locker room, checkpoint booth, kitchen pass, closet, bus, surveillance corner, or crowded doorway.
- Caustics must come from real water, glass, aquarium walls, flooded floor, swimming pool, wet ceiling, or moving reflections. Keep it local and soft, not fantasy light.
- Strong shadows must come from explainable objects: blinds, fan blades, railings, projector gate, train windows, tree branches, medical lamps, headlights, or rotating signage.
- The special image should still contain foreground, middle ground, and background. It cannot replace staging with an abstract light effect.
- Keep the color system unified. Special light can introduce an accent, but not a new unrelated palette.

Good uses:
- Shot 1 stable world, Shot 2 fisheye witness view at the moment of pressure, Shot 3 quiet aftermath.
- Shot 1 stable room, Shot 2 water caustics reveal an object, Shot 3 empty reflected space.
- Shot 1 establishing architecture, Shot 2 projector or blind shadow cuts across the subject, Shot 3 the room after the light is gone.

Avoid:
- Random fisheye distortion on a normal exterior.
- Global rainbow caustics or decorative light everywhere.
- Horror-style shadow gimmicks when the story is not horror.
- Music-video lighting, neon beams, laser lines, spotlight spectacle, or glossy commercial lighting.
- Special effects that make the image look like a game, poster, or concept art.

## 6. V4 Self-Check

Reject or revise when:
- Every frame is equally detailed, expensive, beautiful, or complete.
- The sequence would still read if shuffled.
- Dirt is uniform.
- The lens substrate is invisible.
- Every frame uses the same standard 21:9 composition.
- The result feels like prompt illustration rather than captured footage.
- The special lens or light has no physical camera/light-source reason.

## 7. Validated V4 Defaults

When testing quickly, do not generate many variants with maximal descriptive prompts. Use fewer, shorter, better-constrained prompts.

Prompt density:
- One capture substrate.
- One color body.
- One story clue.
- One secondary clue.
- One camera position.
- One light source.
- No more than 2-3 concrete scene details per shot.

Preferred triptych layouts:
- Hotel / room looking out: held opening `1.25:0.9:0.85`.
- Sea / departure / loss: aftertaste ending `0.85:0.9:1.25`.
- Ritual / refusal / ceremony: impact middle `0.85:1.3:0.85`.

Validated recipes:

### Hotel Interior Looking At African Savanna

Use:
- Yellow ochre afternoon window light.
- Dark underplayed hotel interior.
- Distant off-road vehicle and animals as the story clue.
- One object left behind, such as binoculars, glass, or key.
- Large window as the main frame, not a safari postcard.

Avoid:
- Tourism photography.
- Luxury lodge advertising.
- Over-detailed wildlife spectacle.
- Golden glossy highlights.

### Very Blue Sea With Large Ship

Use:
- Blue as the whole color body, with ship shadow as support.
- Long-lens compression or scratched terminal glass.
- Missed departure as the story action.
- Plain pier, folded ticket, floating paper, or empty railing as the story clue.
- A larger final frame when the loss/aftertaste is the point.

Avoid:
- Travel-ad sky and water.
- Clean postcard horizon.
- Heroic ship beauty.
- Too many nautical props.

### Eastern Ritual Symmetry

Use:
- Strict axial staging and a strong ceremonial floor field.
- Saffron/yellow ground, deep red accent, black ceremonial shadows.
- Refused seal, unopened box, empty corridor, or turned-away crowd as the story clue.
- Larger middle frame when the refusal is the impact.

Avoid:
- Costume-poster gloss.
- Palace tourism.
- Fantasy glow.
- Decorative crowds without a moral action.

### Refined Go Master And Boy

Use:
- 35mm release print, refined ink-gray body, bone-white screen support, deep black stones as the only accent.
- When the user references Zhang Yimou's `Shadow`, translate it into stable ink-wash monochrome, rain on silk screens, strict central axis, heavy black robes against pale gray, and restrained power geometry.
- Keep all three shots in the same room, same light source, same gray scale, same table axis, and same costumes. Do not let Shot 3 jump to another location or color temperature.
- Quiet Eastern room, rain-bright screens, low Go table, negative space, and solemn stillness.
- Story action should be small but irreversible: a wrong stone placed outside the board, a still hand, an empty cushion, a cooling tea cup.
- Shot 1 should keep both players small inside the room; Shot 2 should stay steady at table distance, not macro; Shot 3 should leave the stone, empty cushion, or solitary master as residue.
- The board can be sparse. A crowded Go board is not automatically more advanced.

Avoid:
- Luxury tea-room advertising.
- Costume-drama polish.
- Decorative ink props everywhere.
- Macro stone close-ups that erase room, relation, or consequence.
- Glossy wooden surfaces and waxy faces.
- Changing the visual system between shots: no warm tea-house frame followed by blue rain frame, no painterly third shot, no extra bamboo scenery as decoration.

### Real F1 Track Rain

Use:
- Real motorsport documentary still, long-lens film compression, overcast daylight, wet asphalt black, desaturated racing white, tiny red marshal or tire-marker accent.
- Real panning blur, tire spray, safety fence, pit wall, marshals, and imperfect focus as the speed language.
- Story action should be physical but not explosive: a near miss, a damaged marker, a car already gone, a quiet track aftermath.
- Use fence bars, pit-wall edges, rain glass, or trackside compression as justified foreground.

Avoid:
- Neon, cyberpunk, showroom lighting, sponsor-poster gloss, heroic car beauty, perfect CGI surfaces.
- Fake speed trails, glowing wheels, sparks, explosions, and fantasy track lighting.
- Over-clean cars and hyper-sharp advertising-style motorsport photography.

### Chinese County Absurd Realism

Use:
- 16mm television transfer or old broadcast capture, static observational camera, imperfect exposure, slight color bleed, uneven grain.
- Cement gray or rainy concrete as the color body, with one or two lived-in color accents: bus-stop blue, plastic red, faded wedding pink, weak shop-sign red, cold white tube light.
- Ordinary county-town locations: bus station, mall atrium, dance hall, clinic, market corridor, empty banquet room, roadside shop, tiled waiting hall.
- One mundane absurd object treated seriously: red basin with fish, oversized wedding arch, karaoke light in daylight, abandoned ceremonial prop, plastic chair row, wet ticket.
- Make the absurdity social and quiet. Shot 3 should leave an object, reflection, or absence rather than explain the joke.

Avoid:
- Random grime everywhere, horror lighting, nightclub ruin, surreal VFX, dreamcore poster gloss, comedy staging, and over-saturated neon.
- Making every frame green/pink. Color should come from real objects and weak practical signs, not from a global filter.
