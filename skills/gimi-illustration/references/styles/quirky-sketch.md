# Style · Quirky Sketch（怪诞手绘）

> id: `quirky-sketch`  
> display_name: 怪诞手绘  
> tagline: 白底线稿，软蓝点睛，像编辑部手绘涂鸦  
> aliases: 怪诞手绘, quirky, 线稿涂鸦  
> preview: （可空）

> 当前默认风格预设。定义「怎么画」，不定义「画谁」。

---

## 一句话

怪诞手绘，隐喻叙事，留白透气，不说明书。物件具体、有故事动线，靠线稿和大小区分，不靠铺满色块。

## 画法

**线条** — 全图（含 IP 角色与场景物件）粗细不均、带抖动感、可不封口；不矢量、不厚重描边。角色可以因构图层级略有轻重差，但不保留设定图的绝对线宽；只有用户明确的画法例外才覆盖本条。

**背景与留白**

- 白底：白色或轻微米白；无纹理 / 噪点 / 渐变 / 深色背景
- 主体占 50–75%，至少 25% 空白
- **留白 ≠ 少画**：同屏可 **4–8** 个具名物件；靠大小、线稿粗细、前后层次区分，不靠铺色填密

**内容与动线**（字段详则见 shot-config / composition-patterns）

- **具象优先**：画可辨认的具体物件（优先原文名词）；纯抽象象征不能替代
- **故事动线**：箭头 / 路径 / 视线 / 动作连成可读顺序，一眼跟完「发生了什么」

**双色层** — IP 角色跟参考图全色；场景物件线稿为主 + 少量点色（见「颜色」）

## 颜色

| 层 | 规则 |
|----|------|
| **IP 角色** | 锚点色跟 **当次 IP 设定图**（读 `ip/{$IP}/ip.md`）；线条粗细、笔触与闭合方式跟随本风格，**颜色不减、不被场景色染色**；仅用户明确画法例外才覆盖 |
| **场景物件** | 线稿为主；**软蓝主强调** + **软橙可选 ≤2 处点睛**（见「场景色纪律」） |

**场景色纪律**

> 场景以线稿为主；颜色只强调关键信息，不替代物件表意和故事动线。

**软蓝（主强调）** — 路径、按钮、关键物件

- 有填色的场景物件 **≤ 4**（IP 不算）；单物件填色 **≤ 30%**
- 禁止文件夹 / 屏幕 / 标签底大面积填色；不得每个元素都上色

**软橙（点睛）** — **≤ 2 处**

- 仅用于：问句引线、警示线、编号圈、小箭头
- 禁止：橙物件填色、橙标签底

**标注** — 黑色手写 + 黑色箭头

- 禁止：便利贴底色、标签背景色块、彩色下划线

**改动 / 对比** — 删除线、波浪线等线稿符号

- 禁止：红绿 diff 填色；强调优先蓝，橙只作上述点睛

## 审美方向

要：怪诞、创意、有意思、简洁清爽、有故事动线  
不要：可爱、幼稚、死板、彩虹色

## 绝对不要

> 视觉体裁禁令；颜色细则见「场景色纪律」。

- 商业插画 / PPT 信息图 / 正式流程图 / 课程课件
- 儿童插画 / 精致扁平插画 / 科技感 UI
- 复杂背景、渐变、阴影、纹理
- 在图上写结构类型名称

## 疏密与背景指令（填入 `{SPACE_DESC}`）

## 留白指令（填入 `{WHITESPACE_DESC}` · 别名）

> 以下英文块同时填入 `{SPACE_DESC}` 与 `{WHITESPACE_DESC}`。

```
subject occupies 50-75% of frame, at least 25% white space,
preferably one continuous empty block, not filled edge to edge;
whitespace does not mean fewer objects — allow 4-8 named objects when the message needs it;
use size, line weight, and depth layering instead of color blocks to create hierarchy
```

## 标注颜色指令（填入 `{LABEL_COLOR}`）

```
black handwritten Chinese labels and black arrows only;
no colored sticky notes, no label background fills, no colorful underlines;
character keeps full reference colors; scene objects stay mostly black line art;
soft blue as the main scene accent (paths, buttons, key object fills);
soft orange for at most 2 small highlights only (question cues, warning lines, step numbers) — no orange object fills or label backgrounds;
blue fills on at most 1-4 key scene objects maximum
```

## Prompt 风格段（填入 `{STYLE_DNA}`）

```
quirky hand-drawn illustration, wobbly ink lines, expressive rough sketch,
naive art style, black hand-drawn line structure for scene objects,
soft blue as main scene accent color,
soft orange on at most 2 small highlight touches (not object fills),
blue local accent fills on at most 1-4 key scene objects;
recognizable concrete objects connected by clear story flow arrows or path;
multiple named objects allowed (typically 4-8) — hierarchy via size and line weight, not more color fills;
changes shown with line marks not red-green color fills;
white background, editorial doodle feeling,
no photorealistic, no smooth vector, no 3D render, no PPT infographic,
no gradient, no cute cartoon, no colored label backgrounds, no large color-filled shapes
```

## 风格适配指令（填入 `{STYLE_ADAPT}`）

当有 IP 角色时（**通用层**，不写死具体锚点名称）：

```
IMPORTANT style adaptation for character:
- Keep ALL identity anchors (clothing, accessories, colors, proportions) exactly as defined in the IP file and reference images
- Apply quirky-sketch line weight, wobbly texture, open-contour behavior, and black ink treatment to BOTH character and scene; do not preserve the character sheet's absolute stroke thickness or source medium
- Only an explicit {IP_STYLE_EXCEPTION} from the user may override a stated line or medium rule; do not infer an override from the reference image or ordinary IP description
- Scene soft-blue and soft-orange accents apply to OBJECTS ONLY — must NOT tint, replace, or bleed into character clothing or accessories
- Scene objects: black line art; soft blue main accents on 1-4 objects; soft orange at most 2 small highlights only
```

> IP 专属锁色等补充 → 读 `ip/{$IP}/ip.md` 的 `{IP_STYLE_ADAPT}`；仅用户明确指定时再读「用户指定画法例外」，组装在 `{STYLE_ADAPT}` 之后。

## Step 0.4 生成（自定义 IP · 标准风格样板镜）

> 仅 Step 0 校准用；**不是**配图 Step 3。细则见 `ip/_template.md`「0.4 门禁」。  
> 对用户称「怪诞手绘」；本文件 id 仍为 `quirky-sketch`。

**必须载入：** 本节 `{STYLE_DNA}` + `{STYLE_ADAPT}` + `IP_DESC` / `{IP_STYLE_ADAPT}` + 仅用户明确指定时的 `{IP_STYLE_EXCEPTION}` + 已确认的 `reference-character.png`（全身）。

**画面规格（所有自定义 IP 共用 · 写死）：**

- 比例 16:9；角色全身可见（可坐姿/侧身，不必站姿）
- 主题文案（固定）：vibe coding · IP 配图风格样板
- 场景物件从清单取 **2–4**：笔记本电脑、杯子、绿植、简单桌面线稿
- 白底留白 ≥ 25%；场景色纪律：软蓝主强调、橙 ≤2 点睛

**校准专用 prompt 骨架：**

```
{IP_DESC}
{STYLE_DNA}
{STYLE_ADAPT}
{IP_STYLE_ADAPT}
{IP_STYLE_EXCEPTION}
aspect ratio 16:9, landscape
Match character identity to reference-character.png: <锚点关键词>
Full-body character visible (sitting or standing ok), quirky-sketch style sample — wobbly ink lines, expressive rough sketch.
Canonical vibe-coding style mirror scene: 2-4 objects from {laptop, mug, plant, simple desk line art}; soft blue accents, soft orange at most 2 small highlights.
White background with generous whitespace.
NO Chinese/English labels, NO title, NO arrows, NO numbered steps, NO shot-config story objects, NO article theme.
NOT a writing-rules checklist, NOT a formal illustration for an article, NOT clean vector anime character sheet.
```

**Tier 提醒：** 带标注场景的主题校准图属于 **Tier 2 主题校准**，**不是**自定义 IP 默认模板；自定义 IP 0.4 用本样板镜学 **线稿 + 色纪律**，不学避坑叙事标注。

### 校准入库 QA（5 项）

- [ ] 16:9；角色全身可见
- [ ] canonical 场景物件 2–4；色纪律合格
- [ ] 无标注 / 标题 / 文章主题 / shot 物件
- [ ] 线稿质感符合本节 STYLE_DNA（非干净矢量立绘）
- [ ] 身份像 `reference-character.png`；角色线条符合怪诞手绘，只有用户明确画法例外才额外检查

五项全过才展示，并用用户层话术问「像吗？」；任一项不过 → 重生成，不得展示/入库。

## QA 检查项

> 仅当 `$STYLE=quirky-sketch` 时加载本节。

**构图与留白**

- 主体 50–75%，空白 ≥ 25%；白底，无纹理 / 渐变 / 深色背景

**场景色** — 逐项对照「场景色纪律」

**内容与动线**

- 物件具体可辨认；不像 PPT
- 故事动线可读（箭头 / 路径能跟完）
- 需要信息密度时：具名物件够、层次清，**不等于**过满或铺色

**失败信号（本风格）**

- 填色物件 > 4；单物件填色 > 30%
- 橙 > 2 处，或橙用于物件填底 / 标签底
- **场景点睛色渗入角色服装**（读 `ip/{$IP}/ip.md` 判断具体走形项）
- 红绿 diff 色块；标签 / 便利贴有底色

## 迭代 palette（颜色过多时用）

```
keep character reference colors; scene stays black line art;
soft blue main accent on 1-4 objects max; soft orange at most 2 small highlights;
remove orange object fills, colored label backgrounds, red-green diff fills
```

---

`v2.1` · 2026-07-27 · 角色与场景共同遵循怪诞手绘线条；仅用户明确例外覆盖
