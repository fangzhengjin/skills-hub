# IP · Gimi（马帽女孩）

> 气质：怪诞手绘里的马帽女孩，内容创作者化身  
> 只描述「长什么样 · 序列图怎么带读」。画风见 `styles/{$STYLE}.md`（默认 quirky-sketch；亦支持 warm-storybook / product-proposal）。
> 合约与 Step 0 见 `references/ip/_template.md`（本文件为已填实例）。

---

## 参考图（生图必传）

| 图 | 路径 | 作用 |
|----|------|------|
| **设定图** | `assets/ip/gimi/reference-character.png` | 锚点色、配饰、比例 |
| **校准图** | `assets/ip/gimi/examples/{$STYLE}/` 选 1 张 | 该风格下仍像同一人（见下） |

**双参考分工（$IP=gimi）：**

1. 正式配图传 **设定图 + 当前 `$STYLE` 校准图 1 张**（共 2 张）；当前风格校准尚未确认时，只能 lazy 补本风格校准，不得用 `examples/quirky-sketch/` 充当另一种风格的双参考桥，也不得降级交付
2. 设定图管锚点色与 **chibi 比例**；校准图管「本风格渲染下仍像同一人」
3. 校准图不抄场景或构图；场景规则只读当前 `styles/{$STYLE}.md`
4. prompt 开头：`Match Gimi to BOTH references — chibi proportions, same hood, VERTICAL vest with deep-blue + sky-blue + warm-brown stripes (NOT yellow/orange on vest, NOT horizontal), blush, cube pendant, skirt, boots.`

**按姿势 / 主题选校准图（全 `$STYLE` 共用）：**

> 下列文件名在每个已校准风格目录中保持一致：`assets/ip/gimi/examples/{$STYLE}/<file>`。新增风格只补同名图片，不新增本表行。拿不准时选 `gimi-writing-rules-checklist.png`。

| 选用时机 | 文件 |
|---------|------|
| 默认 / 需看清全身锚点 | `gimi-writing-rules-checklist.png` |
| 职场 / 久坐 / 痛点 / 环境类 | `gimi-desk-shoulder-fatigue.png` |
| 产品界面 / 弹窗 / 功能讲解 | `gimi-exercise-modal-focus.png` |
| AI 改文件 / 焦虑 / 有图内标题 | `gimi-ai-change-chaos.png` |

**批内一致性（全 `$STYLE` 必检）：** 同批多图时，头身比与脸龄须与**当次所选该风格校准图**同档；漂移 → 换更近姿势/主题的校准重试，不得只靠加 prompt 词糊弄。风格的背景、线条、色块、空间和文字处理仍以当前 style 文件为准，不从 Gimi 主题表推断。

---

## 锚点（5 个，丢任一个就不算 Gimi）

1. **棕色马帽兜帽**：尖马耳 + 额前白色毛簇（非猫耳、非全头套）
2. **深蓝 + 天蓝 + 暖棕竖条纹 V 领针织背心**（**VERTICAL**，非横条纹；见下「背心配色」）
3. **明显粉色腮红**（圆脸两侧）
4. **黑色厚底系带靴**
5. **棕色立方体吊坠项链**（胸前小方块）

**比例：** chibi，头身约 1:2～1:2.5，与设定图一致；**不因 sketch 风格拉长身体或改短裤裙。**

---

## 背心配色（`reference-character.png` 为准）

> 走形高发区。配色以设定图为准，**不**用场景软蓝 / 软橙替代背心条纹色。

| 部位 | 配色 |
|------|------|
| **竖条纹（3 色循环）** | **深蓝**（宽条）+ **天蓝/浅蓝**（细条）+ **暖棕/土褐**（细条） |
| **V 领边 + 袖窿罗纹** | 纯色 **深蓝** |
| **下摆罗纹边** | 纯色 **暖棕/土褐** |
| **内搭** | 白色翻领长袖衬衫（背心外可见领口与袖口） |

**禁止出现在背心上：** 黄色、橙色、金色、灰白单色背心、横条纹、场景点睛色「染」进条纹。

**走形典型：** 蓝黄竖条、蓝橙竖条、只剩两种色、条纹被线稿洗成灰白。

---

## 填入 `{IP_DESC}`

```
[Match BOTH attached reference images for Gimi's appearance]
Gimi: chibi girl, brown horse hood (pointed horse ears, white forelock tuft, NOT cat ears, NOT full horse mask),
short brown hair, round face, large brown eyes, prominent pink blush,
white collared shirt,
VERTICAL knit vest with DEEP BLUE + SKY BLUE + WARM BROWN/TAN stripes (wide deep-blue bands, thin sky-blue and warm-brown bands; NOT horizontal stripes),
dark-blue V-neck and armhole rib trim, warm-brown/tan hem band,
blue short skirt (NOT shorts), brown cube pendant necklace on cord,
black chunky lace-up platform boots.
Vest stripe colors must match character sheet exactly — NOT yellow, NOT orange, NOT gold, NOT gray on vest; scene accent colors must NOT bleed into clothing.
Keep exact colors and proportions from the character reference; render line quality, medium, and scene treatment according to the current style.
```

---

## 填入 `{IP_STYLE_ADAPT}`

> 任意 `$STYLE` 下、$IP=gimi 时追加在 `{STYLE_ADAPT}` 之后。其它 IP 若无此节则留空。

```
Gimi-specific color lock:
- VERTICAL knit vest stripes = DEEP BLUE + SKY BLUE + WARM BROWN/TAN (wide deep-blue bands, thin sky-blue and warm-brown bands)
- Dark-blue V-neck and armhole rib trim; warm-brown/tan hem band
- NOT yellow, NOT orange, NOT gold stripes on vest; NOT gray or washed-out vest
- Scene accent colors must NOT tint vest, skirt, hood, or boots
```

## 迭代 palette（背心配色走形时）

> 与 `styles/{$STYLE}.md` 通用 palette 叠加；仅 $IP=gimi 且背心走形时用。

```
LOCK Gimi vest to character sheet: VERTICAL deep-blue + sky-blue + warm-brown/tan stripes;
dark-blue V-neck trim; warm-brown hem band;
NO yellow/orange/gold on vest; NO gray washed-out vest;
scene orange and blue accents on objects ONLY, never on clothing
```

---

## QA · 走形失败信号（$IP=gimi）

**锚点走形**

- 横条纹替竖条纹 / 短裤替裙 / 无腮红 / 无立方体吊坠
- 猫耳或全头套替马帽 / 体型拉长、不像设定图 chibi 比例

**背心配色走形**

- 背心出现 **黄 / 橙 / 金** 色条纹（最常见：场景软橙渗入服装）
- 背心只剩蓝 + 黄两色，缺少 **暖棕/土褐** 第三色
- 背心偏灰白、偏棕橙，或深蓝 / 天蓝 / 暖棕三色竖条纹不全
- V 领边非深蓝、下摆边非暖棕

**流程**

- 双参考未传入即声称已走 gimi 流程

**迭代：** 确认双参考进上下文；prompt 须含 `{STYLE_ADAPT}` + `{IP_STYLE_ADAPT}`；重试时读上「迭代 palette（背心配色走形时）」。

---

## 操作规则

1. 双参考进上下文后再 `image_gen`
2. prompt 强调 **VERTICAL stripes** + **cube pendant**
3. 负向：`NOT horizontal stripes, NOT yellow/orange/gold vest stripes, NOT gray vest, NOT cat ears, NOT full horse costume, NOT shorts instead of skirt, NOT missing blush`
4. 单图只 1 个 Gimi

---

## 动作库（选与锚定句匹配的，禁默认放大镜）

推、拉、扛、塞、捞、撑、缝、检查、打开、递出、观察、按按钮、扶帽、指、站在…上、被困在…里、拉动…

---

## 序列图导游（结构轴 = 路径序列时）

> 管「站在动线哪、怎么带读」，不管长什么样（见锚点）或动作词表（见动作库）。

- 全图 **1 个 Gimi**，沿故事动线参与：递物 / 按按钮 / 指路 / 沿路径移动
- 站在**步骤之间或动线侧面**，不遮挡编号圈与关键物件
- shot-config「故事动线」须写明 Gimi 站位与引导动作

**禁止：** 每站复制多个 Gimi、角落站桩装饰、与锚定句无关的动作、身体挡住主路径节点

**非序列图**（单点澄清、物件特写、对比并置等）：Gimi 可不存在；存在时按信息分工即可，不适用本节

---

`v2.0` · 2026-07-07 · 新增 `{IP_STYLE_ADAPT}` + IP 层迭代 palette；背心锁色从 style 收层
