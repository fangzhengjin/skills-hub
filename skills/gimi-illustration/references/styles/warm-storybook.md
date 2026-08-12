# Style · Warm Storybook（暖调绘本）

> id: `warm-storybook`  
> display_name: 暖调绘本  
> tagline: 温暖丰润的水彩手绘，纸纹颗粒与淡淡晕染
> aliases: 暖色绘本, 纸纹风, 旅行手帐风, 暖调插画, 水彩手绘, 治愈水彩  
> preview: （可空）

> 定义「怎么画」，不定义「画谁」。

---

## 一句话

温暖丰润、仍然透亮的水彩旅行绘本：纸张颗粒、淡淡晕染与柔和自然光贯穿全图；暖意来自**可辨的日光与材质**，不是覆盖所有物体的黄褐滤镜。人物与环境必须是同一纸本水彩介质。

## 无 IP 校准策略

`$IP=none` 时采用 **required style-single**：按全局四个中立主题，从 `assets/none/examples/warm-storybook/` 选择 **1 张** 校准图。缺任一主题资产则停止正式生成，不得借用其他风格或仅靠文字补齐。

这四张发布包资产刻意使用无人物、无手、无动物、无品牌 IP 的静物/场景叙事，目的是只校准暖光、水彩纸纹、褐色软线、冷影和纸感呼吸；它们不规定正式无 IP 配图必须没有人物。正式图是否使用通用人物，仍由当次主题与 shot-config 决定。

## 画法

**线条** — 全图（含 IP 角色与场景物件）细软、略断续，偏水彩褐墨/铅笔；禁止粗黑均匀描边、赛璐璐硬边。角色不保留设定图的绝对线宽或源媒介，只有用户明确画法例外才覆盖本条。

**质感与光影** — 全图有可见纸张肌理与轻湿边晕染，人物衣褶/皮肤与环境同级；日光温柔而透亮，阴影浅、透明、偏冷。暖色落在阳光、木材、土路、陶器和局部植物上；白衬衫、屏幕、纸面仍保持中性浅色。

**背景与疏密** — 允许丰润完整的沉浸式场景；环境可比人物多一层水彩晕染。纸感呼吸按构图选择性出现在洗色边缘、亮部或局部空隙，不做固定四角留白框；完整场景不等于颜料死铺满画框，也不把多节点路线拼贴写成默认构图。

**内容与动线** — 具象可辨；标注可用褐笔嵌入场景。

**统一介质（硬）** — 人物必须与环境共享软线、纸纹和轻晕染；只锁当前 IP 的身份锚点，不锁「矢量立绘」画法。

## 颜色 / 色纪律

| 层 | 规则 |
|----|------|
| **IP 角色** | 身份锚点色、服装结构与比例完全跟随对应设定图；可用淡水彩铺色与轻晕边，但场景色不得改写角色身份色。 |
| **场景** | 透亮低饱和的暖土色形成丰润锚点：暖奶油纸、浅赭、雾金可用在日光与可见材质；淡雾蓝 / 海青绿承接天空、水面、远景和阴影。禁止 sepia 泥罩、全局黄罩与死黑暗角。 |
| **标注** | 褐 / 深棕软手写 + 细箭头；禁荧光便利贴底。 |

**配色密度：** 中到偏丰润；氛围是**低饱和 × 透亮 × 有来源的暖意**。暖色不必稀少，但必须能回指到光线或物体材质。

## 审美方向

要：温暖丰润、水彩手绘、纸纹、淡晕染、旅行绘本、暖光与冷影并存、柔和自然光、选择性纸感呼吸
不要：贴纸角色、粗黑描边赛璐璐、暗沉泥色、整图黄 / sepia 滤镜、白底线稿涂鸦、固定四角纸边框、塑料厚涂、PPT

## 绝对不要

- 人物粗黑硬描边 / 矢量贴纸感（与环境水彩分裂）
- 纯白底稀疏线稿（quirky）
- 暗沉泥褐整图罩色；旧照片式全局黄罩（白色物体被一并染黄）
- 四边顶死、无层次的颜料墙；或为了留白硬做四角相框
- quirky 软蓝橙点睛纪律
- 正式文案用 Ghibli / 吉卜力作商标名

## 疏密与背景指令（填入 `{SPACE_DESC}`）

> 满景页 shot-config 标 `density=scenic`，阅读动线见 `composition-patterns.md`「阅读动线语法」（T3′）；本风格只供介质与铺色呼吸，不写动线/多节点拼贴宪法。

```
warm watercolor storybook scene on softly cream paper with visible paper grain,
rich but translucent watercolor layers with soft wet-edge blooms;
warm sunlight and warm materials (wood, clay, sunlit stone paths, local foliage) create the rich warmth,
while mist-blue / sea-teal carry sky, water, distant depth and cast shadows;
keep white shirts, screens and paper light neutral rather than tinting them amber;
character and environment share ONE watercolor-on-paper medium, with the environment slightly more watery;
use selective paper breathing at wash edges, bright openings, or unpainted gaps according to the composition;
scenic pages may approach the frame edge with a soft wet-edge release — not a mandatory four-corner paper border;
avoid muddy sepia, global yellow filter, crushed dark corners, pure-white sparse doodle board, and edge-to-edge wallpaper fill
```

## 留白指令（填入 `{WHITESPACE_DESC}` · 别名）

```
warm watercolor storybook scene on softly cream paper with visible paper grain,
rich but translucent watercolor layers with soft wet-edge blooms;
warm sunlight and warm materials (wood, clay, sunlit stone paths, local foliage) create the rich warmth,
while mist-blue / sea-teal carry sky, water, distant depth and cast shadows;
keep white shirts, screens and paper light neutral rather than tinting them amber;
character and environment share ONE watercolor-on-paper medium, with the environment slightly more watery;
use selective paper breathing at wash edges, bright openings, or unpainted gaps according to the composition;
scenic pages may approach the frame edge with a soft wet-edge release — not a mandatory four-corner paper border;
avoid muddy sepia, global yellow filter, crushed dark corners, pure-white sparse doodle board, and edge-to-edge wallpaper fill
```

## 标注颜色指令（填入 `{LABEL_COLOR}`）

```
soft brown handwritten Chinese labels and thin arrows nested into the scene;
no sticky-note fills, no neon colors
```

## Prompt 风格段（填入 `{STYLE_DNA}`）

```
warm healing watercolor storybook illustration, visible paper grain and subtle wash blooms,
rich yet low-saturation warm palette with translucent layers and gentle natural light;
warm sunlight and warm materials (wood, clay, sunlit stone, local foliage) carry the rich warmth,
mist-blue / sea-teal balance sky, water and translucent cast shadows;
keep white shirts, screens and paper light neutral — warmth is material- and light-based, not a global yellow cast;
delicate graphite-brown lines, character and environment share ONE watercolor-on-paper medium,
gentle painterly fills with selective paper breathing at wet edges and bright openings;
scenic pages may approach frame edges with soft watercolor release, never a mandatory four-corner border;
nostalgic travel-journal mood without aged-photo treatment,
NO muddy sepia gloom, NO global yellow/amber wash over whites, NO cel-shade hard black contours,
NO pure-white sparse doodle board, NO edge-to-edge wallpaper fill, NO PPT infographic, NO neon accents
```

## 风格适配指令（填入 `{STYLE_ADAPT}`）

```
IMPORTANT style adaptation for the current character:
- Preserve ALL identity anchors, clothing structure, accessory placement, proportions, and palette exactly as defined by the attached character sheet and current IP file
- Apply warm-storybook line weight, soft brown ink or pencil treatment, paper grain, and watercolor medium to BOTH character and scene; do not preserve the character sheet's absolute stroke thickness or source medium
- Only an explicit {IP_STYLE_EXCEPTION} from the user may override a stated line or medium rule; do not infer an override from the reference image or ordinary IP description
- RENDER character and environment in the SAME watercolor-on-paper medium: soft brown ink lines, visible paper grain, gentle translucent fills, and light wet-edge blooms
- Keep identity anchors readable; soften only line quality and texture, never redesign the face, outfit, silhouette, or body proportion
- Let scene warmth stay on light and materials; do not bleed scene colors into identity-defining clothing or accessories
- Use selective paper breathing and watercolor edge release according to composition; a scenic page may remain rich and immersive
```

## Step 0.4 生成（自定义 IP · 本风格样板镜）

> 仅 Step 0 / lazy 校准用；**不是**配图 Step 3。  
> 对用户称「暖调绘本」；id 仍为 `warm-storybook`。

**必须载入：** 本节 `{STYLE_DNA}` + `{STYLE_ADAPT}` + `IP_DESC` / `{IP_STYLE_ADAPT}` + 仅用户明确指定时的 `{IP_STYLE_EXCEPTION}` + 设定图（全身）。
**可选：** 若该 IP 已有 `assets/ip/{$IP}/examples/warm-storybook/` 校准图，可再附 **1 张**作线稿/介质参考（与 quirky dual 一致；禁止使用或重建 `assets/styles/**`）。

**画面规格：**

- 比例 16:9；角色全身可见（可坐姿 / 侧身，不必站姿）
- 主题文案（固定）：vibe coding · IP 配图风格样板
- 场景物件从清单取 **2–4**：打开的笔记本电脑、杯子、绿植、简单木质桌面；可加亮暖窗景或露台远景
- 丰润透亮的水彩 + 纸纹；人物环境同介质；纸感在湿边、亮部或局部空隙自然呼吸，不做固定四角边框

**校准专用 prompt 骨架：**

```
{IP_DESC}
{STYLE_DNA}
{STYLE_ADAPT}
{IP_STYLE_ADAPT}
{IP_STYLE_EXCEPTION}
aspect ratio 16:9, landscape
Match character identity to the attached reference-character sheet; render figure AND scene as one watercolor-on-paper piece.
Full-body character visible (sitting or standing ok).
Canonical vibe-coding style mirror scene: 2-4 objects from {open laptop, mug, plant, simple wooden desk}; optional bright window or terrace depth.
Use rich warm sunlight on visible materials, with mist-blue / sea-teal in shadow or distant depth; keep white surfaces neutral.
Use selective paper breathing and soft wet-edge release, not a mandatory four-corner border.
NO labels, NO title, NO arrows, NO numbered steps, NO shot-config story objects, NO article theme.
NOT a formal illustration for an article, NOT a character sheet, NOT a cel-shade sticker character, NOT muddy sepia, NOT quirky white doodle board.
```

### 校准入库 QA（5 项）

- [ ] 16:9；全身
- [ ] canonical 场景物件 2–4；主题氛围是 `vibe coding`，非文章插图
- [ ] 丰润低饱和暖调 + 纸纹/淡晕染；暖意来自可见光或材质，白色物体不被染黄
- [ ] 无文章标注 / 标题 / shot 物件；人物与环境同水彩介质
- [ ] 身份像设定图；具体锚点按当前 IP 的 `ip.md` 检查；角色线条符合暖调绘本，只有用户明确画法例外才额外检查

## QA 检查项

> 仅当 `$STYLE=warm-storybook` 时加载。

**介质统一**

- 人物非粗黑赛璐璐贴纸；线软，有纸纹 / 轻晕染；身份锚点按当前 IP 文件保持清楚

**色与光**

- 丰润低饱和 × 透亮；暖色可见于日光和材质，雾蓝 / 海青绿可见于冷影、天空、水面或远景
- 白衬衫 / 屏幕 / 纸面保持中性浅色；**Warmth must come from visible light or materials**, never from a global yellow filter

**疏密呼吸**

- 纸纹始终可读；湿边、亮部或局部空隙出现**selective paper breathing**
- `scenic` 允许景物接近画幅边缘，但必须保有亮部、层次或水彩收口；不强制四角留白

**失败信号**

- 人物硬描边 / 与背景分裂
- 暗沉 sepia；全图黄滤镜 / 旧纸发黄罩色；白色物体被染成琥珀
- 为了“透气”硬做四角相框；或把场景涂成无层次的满屏颜料墙
- 当前 IP 的身份锚点被场景暖色改写、丢失或拉长

## 迭代 palette（颜色或介质失控时用）

```
unify character and environment into one watercolor paper medium: soft brown lines, visible paper grain, translucent light washes;
restore rich warm sunlight and warm materials (wood, clay, sunlit stone, foliage) without tinting white shirts, screens, or paper amber;
restore mist-blue / sea-teal in sky, water, distant depth, and cast shadows;
use selective paper breathing at wet edges or bright openings, not a forced four-corner border;
remove thick black cel outlines, sticker cutout look, muddy sepia gloom, global yellow/amber cast, and flat wallpaper fill
```

---

`v1.5` · 2026-07-25 · A 向：保留丰润暖意，以光与材质承载暖色；纸感呼吸改为选择性收口；风格层去除特定 IP 锚点；0.4 统一 vibe coding 样板主题
