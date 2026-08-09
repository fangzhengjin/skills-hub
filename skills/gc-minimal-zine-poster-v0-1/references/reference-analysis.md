# Reference Analysis

Analyze the real files before extracting rules. The goal is a reusable system, not praise or imitation.

## Evidence Pass

For every usable image, record or inspect:

- filename and available dimensions;
- canvas ratio;
- estimated negative-space range;
- subject or cluster scale;
- background tone and paper texture;
- anchor type and material treatment;
- composition position and balance;
- typography family, scale, and distribution;
- main hue, support hue, and approximate color role;
- decorative marks;
- reproduction defects and lighting;
- mood;
- sample-specific text, brand, signature, date, location, object, or layout that must not be copied.

Use metadata for exact dimensions. Treat visual percentages as estimates unless measured.

## Synthesis Rules

- A trait repeated across most usable references may become a fixed rule.
- A trait that changes while family resemblance survives becomes a variable rule.
- A trait appearing in only one or two examples remains sample residue unless it is structurally necessary.
- With one reference, describe observed traits and confidence limits; do not claim collection-wide frequency.
- Separate `observed` from `inferred`. For example, “paper fibers are visible” is observed; “intended to feel nostalgic” is inferred.
- Do not reproduce source wording, brands, watermarks, signatures, dates, locations, or exact compositions in the reusable prompt.

## Output Structure

```markdown
## 风格名称
[Chinese and English]

## 一句话总结
[specific visual definition]

## 观察证据
- Canvas:
- Negative space:
- Subject and collage:
- Composition:
- Typography:
- Color:
- Texture and reproduction:
- Mood:

## 固定系统
[non-negotiable family traits]

## 可变系统
[safe axes of variation]

## 样本残留，不复用
[source-specific content and compositions]

## 可复用 Prompt
[base prompt]

## 随机化区块
[variables and layout families]

## 避免项
[negative prompt]

## 置信度与限制
[sample size, unreadable files, or uncertain inferences]
```

When analysis is followed by generation, use the fixed system as constraints and deliberately choose a new combination from the variable system.
