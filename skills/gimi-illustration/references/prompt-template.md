# Prompt Template（组装器）

> 本文件只定义组装逻辑。风格词从 `styles/{当前风格}.md` 获取，
> IP 从 `ip/{当前IP}/ip.md` 获取。不硬编码任何风格/IP 词。

每张图单独生成，不要把多张图拼在一张里。

---

## 组装顺序

```
{REF_IMAGE}
{IP_DESC}              ← $IP=gimi 时紧接参考图，先于风格段
{STYLE_DNA}
{SPACE_DESC}            ← 来自 styles/{$STYLE}.md；若无则回退 {WHITESPACE_DESC}
{STYLE_ADAPT}          ← 来自 styles/{$STYLE}.md，通用层
{IP_STYLE_ADAPT}       ← 来自 ip/{$IP}/ip.md（有则填，无则留空）
{IP_STYLE_EXCEPTION}   ← 仅用户明确指定时，来自 ip/{$IP}/ip.md 的「用户指定画法例外」
{COMPOSITION_DESC}
{MESSAGE_DESC}
{SUBJECT_DESC}
{TITLE_DESC}
{MOOD_DESC}
{RATIO_DESC}
{OUTPUT_SIZE_DESC}
{LABEL_DESC}
{NEGATIVE_DESC}
```

---

## 变量来源

| 变量 | 来源文件 | 说明 |
|------|----------|------|
| `{REF_IMAGE}` | `assets/ip/` 或 `assets/none/` | 作为 image reference 附件传入（见下方） |
| `{STYLE_DNA}` | `styles/{$STYLE}.md` → "Prompt 风格段" | 纯风格描述，不含 IP |
| `{SPACE_DESC}` | `styles/{$STYLE}.md` → 「疏密与背景指令」；若无该节则读「留白指令 / `{WHITESPACE_DESC}`」 | 疏密、背景、透气策略（不默认白底） |
| `{WHITESPACE_DESC}` | 同上节别名（兼容旧风格文件） | 与 SPACE_DESC 同义回退 |
| `{STYLE_ADAPT}` | `styles/{$STYLE}.md` → "风格适配指令" | 有 IP 时才加；**通用层**，不写死具体锚点 |
| `{IP_STYLE_ADAPT}` | `ip/{$IP}/ip.md` → "填入 `{IP_STYLE_ADAPT}`" | 有 IP 且该文件有此节时追加；无则留空 |
| `{IP_STYLE_EXCEPTION}` | `ip/{$IP}/ip.md` →「用户指定画法例外」 | **仅**用户明确指定时填入；未声明则留空，不从设定图或普通 IP 描述推断 |
| `{IP_DESC}` | 见下方 | 按角色选择读取 |
| `{COMPOSITION_DESC}` | `shot-config.md` → Shot「构图」 | 从构图库选择或自定义 |
| `{MESSAGE_DESC}` | `shot-config.md` → Shot「核心信息」 | 先定义内容表意，再决定画面 |
| `{SUBJECT_DESC}` | `shot-config.md` → Shot「隐喻」 | 具象物件 + 结构；见下方填法 |
| `{MOOD_DESC}` | 可选 | 如不确定留空 |
| `{RATIO_DESC}` | 见下方 | 按 `$RATIO` 填入，**核心比例约束** |
| `{OUTPUT_SIZE_DESC}` | 见下方 | **可选**；仅 `$OUTPUT_SIZE` 有值时填入 |
| `{TITLE_DESC}` | 见下方 | 有标题时填 |
| `{LABEL_DESC}` | 见下方 | 文字标注（颜色从 style 文件读取） |
| `{NEGATIVE_DESC}` | `styles/{$STYLE}.md` → "绝对不要" + IP 负向约束 | 合并输出 |

---

## 各变量填法

### `{REF_IMAGE}`

**解析顺序：** 先由 `SKILL.md` Step 1.5 按当前 `(IP, STYLE)` 解析 `$REF_MODE`；IP 文件不维护全局 `ref_mode`（`none` 见下）。设定图落盘后一律全身 full。

**`$REF_MODE=dual`（含 gimi）：**

1. **必传** `assets/ip/{$IP}/reference-character.png`（全身身份锚）
2. **必传** `assets/ip/{$IP}/examples/{$STYLE}/` 中 **1 张**校准图（只锁该 IP 在 $STYLE 里仍像同一角色；不抄场景叙事、背景、色块、构图或标注）
3. 两张都进上下文后再生图；prompt 开头强调 Match BOTH references + 该 IP 锚点关键词
4. 校准目录为空或文件缺失 → 这是 Step 1.5 的 `lazy`，不得在本阶段降级；用户催图也必须先完成当前风格样板确认

**`$IP` = gimi 时校准图选用**（实例细则，其它 IP 无主题表则任选/仅有一张则用那张）：

- 默认 / 拿不准 → `gimi-writing-rules-checklist.png`
- 职场 / 久坐 / 痛点 / 环境类 → `gimi-desk-shoulder-fatigue.png`
- 产品界面 / 弹窗 / 功能讲解 → `gimi-exercise-modal-focus.png`
- AI 改文件 / 焦虑 / 有图内标题 → `gimi-ai-change-chaos.png`

gimi prompt 开头示例：

```
Match Gimi to BOTH reference images (character sheet + current-style calibration example): same horse hood, VERTICAL vest with deep-blue + sky-blue + warm-brown/tan stripes (NOT yellow/orange/gold on vest), pink blush, cube pendant, blue skirt, black chunky boots. Use the calibration example only for Gimi's recognizable appearance; render the scene strictly with the current style's STYLE_DNA and STYLE_ADAPT.
```

**`$REF_MODE=style-single`（`$IP=none`）：** 不传角色图；必须从 `assets/none/examples/{$STYLE}/` 按 `ip/none.md` 主题矩阵传入 **1 张**风格参考。prompt 开头追加：

```
Use the attached no-IP calibration image ONLY for the current style's declared visual grammar: background treatment, line character, color discipline, whitespace, material treatment, and any style-specific text or figure treatment explicitly requested below. Do NOT copy its composition, title, object arrangement, labels, or business content.
```

**`$REF_MODE=none`（`$IP=none`）：** 当前风格没有 required 无 IP 校准资产时，不传角色图；质量不稳时可选 `assets/none/examples/{$STYLE}/` **1 张**风格参考：
- 路径/步骤/循环类 → `none-practice-loop.png`
- 成果/分享/链接类 → `none-shareable-result.png`
- 变化/混乱/协作处理类 → `none-change-chaos.png`
- 演示/工具链/交付主线类 → `none-delivery-mainline.png`

**分工**：设定图 + 校准图 → IP；风格词 → 场景线稿与色纪律。禁止在 dual 下只传一张却声称完成。

### `{IP_DESC}`

- `$IP=none` → 读 `ip/none.md`
- 其它 → 读 `ip/{$IP}/ip.md`「填入 `{IP_DESC}`」（含 gimi 与自定义）

### `{IP_STYLE_ADAPT}`

- 读 `ip/{$IP}/ip.md`「填入 `{IP_STYLE_ADAPT}`」— **有则填，无则留空**
- gimi → 背心三色锁色等 IP 专属约束
- none → 留空

### `{IP_STYLE_EXCEPTION}`

- 读 `ip/{$IP}/ip.md`「用户指定画法例外」— **仅用户明确指定时填入，未声明则留空**。
- 例外只覆盖用户说清的项目，例如“任何风格下保留粗黑马克笔轮廓”；参考图或普通 IP 描述里的描边粗细、笔触、媒介都不构成例外。
- 默认情况下，角色与场景共同遵循当前 `$STYLE` 的线条粗细、笔触、闭合方式、线色与媒介；角色可以因构图层级略有轻重差，但不保留设定图的绝对线宽。

> **锚点优先**：外貌/配饰/比例/配色以参考图和 IP 文件为准；`{STYLE_ADAPT}` 管角色与场景共同的风格画法；`{IP_STYLE_ADAPT}` 管 IP 专属身份锁；只有 `{IP_STYLE_EXCEPTION}` 覆盖已明确指定的画法项目。

### `{COMPOSITION_DESC}`

从 `composition-patterns.md` 构图库选择（或根据核心信息自定义），转英文：

| 构图 | 填入内容 |
|------|---------|
| 单主体居中 | `single centered subject, generous negative space on all sides` |
| 对比并置 | `two contrasting elements side by side, visual tension` |
| 行动中人物 | `character in mid-action, dynamic pose` |
| 物件特写 | `close-up single object, exaggerated scale` |
| 环境暗示 | `tiny figure in vast environment, scale contrast` |
| 图标级单主体 | `ultra-simple visual symbol, large whitespace, room for sparse labels` |
| 隐喻场景 mini | `minimal scene with 3 elements or fewer, one complete metaphor` |
| 序列逻辑 | `2-4 numbered main steps in left-to-right order; failure/rollback nested inside the last step, not as an extra equal station; rollback arrow from broken state to save point or clean file` |
| 信息聚焦 | `one clear visual focus, supporting elements are smaller and only serve the main message` |
| 情绪面孔 | `expressive face close-up, exaggerated emotion` |

### `{MESSAGE_DESC}`

`Reader takeaway: <one sentence describing the key idea this image must communicate>.`

### `{SUBJECT_DESC}`

从 shot-config「物件表意」+「隐喻」填入，包一层英文引导：

```
Draw these specific named objects from the source text: <物件表意>.
Scene layout: <隐喻内容，含信息分工>.
Clear story flow: <故事动线>, connected by arrows or path in reading order.
Each main object has a clear information role (problem source / action entry / result / state).
Allow 4-6 named objects when needed; use size and line weight for hierarchy, not extra color fills.
For sequential diagrams: exactly N numbered main steps if title says N steps;
nest failure/broken state inside the last step (before → action → after), not as a fourth equal station;
rollback arrow must go from broken state or rollback button TO save box or clean file, never back to broken state.
Viewer can name 2-3 concrete objects in 3 seconds.
Do not use magnifying glass, lightbulb, or generic file icons unless listed in source nouns.
Use soft blue as main scene accent on at most 1-4 objects.
Soft orange on at most 2 small highlights only (not object fills).
Show changes with line marks, not red-green color fills.
No colored sticky notes or label background fills.
```

**视觉承诺 SUBJECT 锁（接在段末）：**  
按 shot-config 字段，从 **`visual-promise.md`** 复制对应子型英文段（§A 结构 / §B 外参·意象 / §C 域物件）+ **§E 标注纪律**通用句（默认保留 2–5 标注）。本文件不维护第二份正文。

**阅读动线（T3′ · `density=scenic` 时追加）：**  
意涵见 `composition-patterns.md`「阅读动线语法」SUBJECT 提示；填入当次「阅读顺序」。

### `{COMPOSITION_DESC}` 补充

序列逻辑构图时，在 `{COMPOSITION_DESC}` 末尾加：`numbered main steps with clear left-to-right story flow; failure state nested inside final step`

`density=scenic` 时追加焦点/阅读序意涵（同上 composition SSOT），勿在此复制长文。

### `{RATIO_DESC}`

按 `$RATIO` 填入（**默认 16:9**）：

| `$RATIO` | 填入内容 |
|----------|---------|
| 16:9 | `aspect ratio 16:9, horizontal composition, landscape orientation, wide frame, NOT portrait, NOT square` |
| 3:4 | `aspect ratio 3:4, vertical composition, portrait orientation, tall frame, NOT landscape` |
| 1:1 | `aspect ratio 1:1, square composition, balanced framing` |
| 9:16 | `aspect ratio 9:16, vertical composition, tall mobile frame` |
| 其它 | 按用户给定比例动态生成，写明 `aspect ratio W:H` 及横/竖/方构图方向 |

推荐像素（16:9 → 1920×1080；3:4 → 1080×1440）**仅作参考**，不写入 `{RATIO_DESC}`，除非用户同时指定了 `$OUTPUT_SIZE`。

### `{OUTPUT_SIZE_DESC}`（可选）

**仅当用户明确要求具体像素（`$OUTPUT_SIZE` 有值）时填入，否则整段留空。**

示例（16:9 + 1920×1080）：
```
CRITICAL: target output 1920x1080 pixels, landscape 16:9 frame
```

示例（3:4 + 1080×1440）：
```
CRITICAL: target output 1080x1440 pixels, portrait 3:4 frame
```

### `{TITLE_DESC}`

- 有标题 → `centered handwritten Chinese title at top: "标题内容"`
- 无标题 → 留空

### `{LABEL_DESC}`

- **默认（标注词有 2–5 个时，必填此段，不得省略）：**  
  `sparse handwritten Chinese labels with thin arrows, 2-5 labels total: "锚点词1", "锚点词2"; exact labels from shot-config; attach to reading-path nodes; {LABEL_COLOR}; no English except product names; do NOT omit labels; do NOT copy photo/map OCR`
- `{LABEL_COLOR}` 从 `styles/{$STYLE}.md` → "标注颜色指令" 读取
- **仅当** shot-config 标注词 = `无（用户要求）`：`no text, no letters, no words, no watermark`  
- 标注词空/「无」但无「用户要求」字样 → **先回 shot-config 补 2–5 词**，禁止直接走无字分支（见 `visual-promise.md` §E）

### `{NEGATIVE_DESC}`

从 `styles/{$STYLE}.md`「绝对不要」段落提取，加上 IP 负向约束（如有）。默认附加：

```
avoid equal-weight process diagrams unless the core idea is truly a process;
avoid formal workflow chart or dense tutorial page;
do not optimize for fewer words at the expense of meaning;
no colored sticky notes, no label background fills, no red-green diff color blocks;
soft blue main scene accent; soft orange at most 2 small highlights only; no orange object fills or label backgrounds
```

**`$IP` = gimi 时追加：**

```
NOT yellow/orange/gold stripes on Gimi vest; NOT gray or monochrome vest;
NOT horizontal vest stripes; scene accent colors must NOT tint Gimi clothing;
vest must keep deep-blue + sky-blue + warm-brown/tan vertical stripes from character sheet
```

---

`v1.14` · 2026-07-27 · 角色线条默认跟随当前风格；仅用户明确指定时覆盖
