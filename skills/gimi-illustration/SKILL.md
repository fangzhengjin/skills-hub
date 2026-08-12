---
name: gimi-illustration
description: >
  Multi-style illustrations from Chinese article text (配图 / illustration):
  quirky sketch, warm storybook, product proposal; OR custom IP enrollment
  (自定义 IP / 录入 IP / 上传形象 / 新建 IP).
  When the user is enrolling a custom IP: do NOT generate a poster or illustration first —
  load references/ip/_template.md and run Step 0 (plan confirm before freeform image gen).
  Use for 配图, 给文章配图, 帮我配图, illustration, 自定义 IP, 录入 IP, 上传形象, 新建 IP,
  怪诞手绘, 暖调绘本, 产品方案.
---

# gimi-illustration · 配图 Skill

> **Public 3.0** = 产品 **v3.0**（多风格：怪诞手绘 / 暖调绘本 / 产品方案 + 自定义 IP）  


> 换窗口：有 `docs/` 时先读 `docs/INDEX.md` → `docs/roadmap.md`；执行以本文件 + `references/ip/_template.md` 为准

## ⚠ 路由分流（先读 · 防 ImageGen 抢跑）

触发含 **`自定义 IP` / `录入 IP` / `上传形象` / `新建 IP`**（可附图）时：

1. **立刻**加载 `references/ip/_template.md`，走 **Step 0**；**不要**先当「配图 / 海报」生图  
2. **本回合禁止**调用任何生图工具（`image_gen` / `GenerateImage` / ImageGen 等），直到用户已回答「按这个形象方案录入吗？」  
   - **半身/全身相同**：首轮**只**出形象方案 + 收尾问；**零例外**  
   - 确认后：半身才允许 0.2b 全身设定稿；再 0.4 校准  
3. **禁止**把录入理解成「生成一张 IP 主题海报 / 原创插画海报」  
4. 细则与话术以 `_template` 为准；本段与之冲突时，**以本段路由为准**（先拦抢跑）

触发仅为 **`配图` / `illustration`** 等、且非录入 IP → 走下方 Quick Mode / Step 1–5。

---

输入文章内容，生成配图。默认风格「怪诞手绘」（`quirky-sketch`），可切换已录入风格（如「暖调绘本」）；IP 为 `gimi` / `none` / 自定义实例，默认 16:9。

---

## 触发词

配图：`配图` / `给文章配图` / `帮我配图` / `illustration`  
自定义 IP：`自定义 IP` / `录入 IP` / `上传形象` / `新建 IP`

---

## 参考文件（按需加载）

| 文件 | 何时加载 |
|------|---------|
| `docs/INDEX.md` | 换窗口文档导航（先读） |
| `docs/roadmap.md` | 换窗口工作台 / 要改规则时 |
| `docs/spec.md` | 产品规划（防跑偏）；非执行协议 |
| `references/styles/{$STYLE}.md` | 生图 / 校准 / 风格 QA 时 |
| `references/styles/_template.md` | 批量录入新风格时（非配图热路径） |
| `references/composition-patterns.md` | 出策略时（**非** Step 0） |
| `references/visual-promise.md` | Step 2 判视觉承诺 / 结构·外参·域物件（**SSOT**；细则不抄进本文件） |
| `references/shot-config.md` | 出策略时（**非** Step 0） |
| `references/prompt-template.md` | 组装 prompt 时 |
| `references/qa-checklist.md` | 质检时 |
| `references/ip/_template.md` | **自定义 IP / Step 0（优先于生图）** |
| `references/ip/gimi/ip.md` | `$IP` = gimi |
| `references/ip/none.md` | `$IP` = none |
| `references/ip/{id}/ip.md` | `$IP` 为已存在的自定义 id |

---

## 生图能力

调用当前 AI 软件**内置的生图工具**（如 Codex `@Image Gen`、Cursor `GenerateImage` 等）。Skill 负责策略、prompt 组装、参考图附件、QA；生图由平台工具执行。接口语义：文本 prompt + 可选图片附件。

**Step 0 录入中：** 遵守文首「路由分流」；未满足允许条件前**不得**调用生图工具。

平台适配优先级：

1. 支持显式图片附件的平台：把参考图作为 image reference 附件传入。
2. Codex `image_gen`：已有 IP 的正式配图一律传「设定图 + 当前 `(IP, STYLE)` 校准图」；先跑 Step 1.5，缺任一张不得生正式图；再 `image_gen`
3. 不支持图片输入且无法把图片放入上下文时，暂停说明原因；已有 IP 不得降级为仅文字锚点的正式配图。

---

## 核心变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `$STYLE` | `quirky-sketch` | 默认怪诞手绘；可按主人语言切换为已录入风格（见 Step 1） |
| `$RATIO` | `16:9` | 宽高比；用户可指定任意比例 |
| `$IP` | `gimi` | `gimi` / `none` / 其他：若存在 `references/ip/{id}/`（非 `_template`）则加载该实例 |
| `$REF_MODE` | 解析得出 | `dual` / `style-single` / `none`；已有 IP 缺当前风格校准时为 `lazy` 门禁，不是可交付参考模式 |
| `$TITLE` | 无 | 用户要求时顶部手写标题 |
| `$COUNT` | 自动推断 | 配图张数 |
| `$OUTPUT_SIZE` | 无 | **可选**；仅用户明确要求具体像素时记录 |

**推荐像素（非强制）：** 16:9 → 建议 1920×1080；3:4 → 建议 1080×1440。

---

## 工作流

### Quick Mode

用户已给正文且变量可推断 → 不多问，直接生图。以下情况才确认：用户说「先别生图」、变量冲突、新 IP 尚无 `ip.md`（先走 Step 0）、或 Step 1.5 判为 `lazy`。
**Step 0 进行中：关闭 Quick Mode**（不得跳过确认话术）。  
**录入触发词出现时：不适用 Quick Mode 生图。**

### Step 0 · 自定义 IP（按需）

用户要新建/录入 IP 时：加载 `references/ip/_template.md`，严格按其中 Step 0 填槽（用户只需附图 +「录入 IP」，不必写 Step 编号）。  
**双层：** 协议走 0.1–0.5；对用户只用「用户层话术」（见 `_template`），称当前 `$STYLE` 的 `display_name`（录入默认多为「怪诞手绘」），不暴露 Step 编号。  

**硬门禁（0.5 完成前）——与文首路由分流一致：**

1. **入口（半身/全身相同）**：首轮只出形象方案 +「按这个形象方案录入吗？」；**一律禁生图**；禁海报式成稿  
2. **禁止配图抢跑**：不得进 Step 1–5；不得写 `shot-config.md`  
3. **出图后必须提问**：同轮追加收尾问；**图 ≠ 闭合**（仅 0.2 确认之后才允许生图）  
4. 半身：确认后 0.2b 须头到脚；落盘 `reference-character.png` 一律 full  
5. 0.4 标准风格样板镜（读 `styles/{$STYLE}.md`）；「像吗？」未闭合前不得进配图  

`examples/{$STYLE}/` 空且要用该风格配图时 → lazy 补 0.4（**已启用**，见 `_template` 多风格细则）。  
完成后才进入配图；配图时 `$IP={id}`。

### Step 1 · 意图确认

记录：`$RATIO` · `$IP` · `$STYLE` · `$TITLE` · `$COUNT` ·（可选）`$OUTPUT_SIZE`

Quick Mode 推断：竖版/小红书 → 3:4；否则 → 16:9。

**`$STYLE` 解析（主人语言，不要求用户写 id）：**

1. 扫描 `references/styles/*.md`（排除 `_template.md`）的 `display_name` / `aliases`
2. 明确命中 → 锁定对应 `id`
3. 软命中 → 一句确认（例：「你是说「暖调绘本」那种纸纹暖色吗？」）
4. 未命中或「换个风格」→ 人情味菜单：每项 `display_name` + `tagline`（默认可标「常用」）
5. 未提风格 → `quirky-sketch`；**本会话首次配图**追加一句轻提示（不打断）：  
   「这次先用怪诞手绘。若想换成暖调绘本（纸纹暖色、旅行手帐感），直接说就行。」
6. 用户描述未录入风格 → 不现场发明；说明目前仅已录入风格，问用默认或以后再录

口语优先；`$STYLE=…` 仅进阶。对用户称 `display_name`，不说路径。

### Step 1.5 · 当前参考解析（IP 与无 IP）

在进入 Step 2、写 `shot-config.md` 或生成正式图**之前**，对当前 `(IP, STYLE)` 只判一次：

1. `$IP=none` 且当前风格「无 IP 校准策略」为 `required style-single` → 必须按 `references/ip/none.md` 选择 `assets/none/examples/{$STYLE}/` 中 1 张，记为 `$REF_MODE=style-single`；缺目录 / 缺选图是发布包资产问题，停止并修复，不向用户索图、不降级为纯文本。
2. `$IP=none` 且当前风格没有 required 策略 → `$REF_MODE=none`，保持既有 none 行为；若该风格声明 optional 且有资产，可按 `none.md` 选 1 张作质量收敛。
3. 已有全身设定图且 `assets/ip/{$IP}/examples/{$STYLE}/` 至少有 1 张可用校准图 → `$REF_MODE=dual`，可进 Step 2。
4. 已有全身设定图但当前风格校准目录为空 / 缺文件 → `$REF_MODE=lazy`；只按当前风格 0.4 生成样板，QA 后问「像吗？」；**禁止**写 `shot-config.md`、生成正式图、或附其他风格校准图充当双参考。用户催图也不降级；应说明「这个风格的样板还没定，确认样板后才能正式配图」。
5. 设定图缺失或不可用 → 路由到现有 IP 录入；不得 single 降级或生成正式图。

用户确认「像」后才将该样板落盘到当前 `$STYLE` 目录；后续正式请求重新解析为 `dual`。**已有 IP 的正式配图不允许 single，必须 dual。** IP 文件不维护全局 `ref_mode`；当前风格的目录事实是唯一依据。

### Step 2 · 消化内容 + 出策略

> 仅 `$REF_MODE` 已被 Step 1.5 判为 `dual` / `style-single` / `none` 时可进入。策略：`composition-patterns.md` · 视觉承诺：**必载** `visual-promise.md`（SSOT）· 落盘：`shot-config.md`。

1. 加载 composition + shot-config + **visual-promise**
2. 按 composition **Step 2 决策流程**（二轴 → 创意生成法八步 → 构图库）
3. **每张 shot** 填视觉承诺全家桶（`visual-promise.md`）+ **density / 阅读顺序**（composition「阅读动线语法」；`scenic` 强制）
4. `外参参考`：按 visual-promise §B（主锚预算 + 默认特征锁不附图）；失败/超时静默降级 `意象`（不问用户）
5. Quick Mode：默认落盘进 Step 3；用户说「先看策略」时先展示摘要

### Step 3 · 组装 Prompt + 生图

1. 加载 `styles/{$STYLE}.md`、`prompt-template.md`、对应 `ip/*.md`
2. 只消费 Step 1.5 已解析的 `$REF_MODE`：
   - `dual` → 设定图 + `examples/{$STYLE}/` 中 1 张校准图（两张都存在才可组装）
   - `style-single` → `$IP=none`，必传 `assets/none/examples/{$STYLE}/` 中按 `none.md` 选定的 1 张；prompt 明示只匹配画法，不复制构图、标题、物件排列或业务内容
   - `none` → 仍按 none 规则（无角色设定图，也无 required 风格资产）
   - 参考图未进上下文，不得声称已执行有 IP 流程
3. 按 `visual-promise.md` / `prompt-template`：追加承诺锁；`外参参考` **默认不附**地标图（特征进 SUBJECT）；仅「外参附图=是」才附；`scenic` 追加阅读动线意涵（composition SSOT）
4. 填充变量槽，调用生图工具（`IP_DESC` 在 `STYLE_DNA` 之前，见 `prompt-template.md`）

### Step 4 · QA 质检

加载 `qa-checklist.md`（承诺 → `visual-promise`；动线 → composition「阅读动线语法」）。`$OUTPUT_SIZE` 有值时 → 等比缩放 + 白底留白，禁止裁切。不通过 → 重试，最多 2 次。

### Step 5 · 交付

```
outputs/{YYYYMMDD}-{slug}/
  shot-config.md      ← 配图策略 + 插入位置（与图片同时交付）
  01-{slug}.png
  02-{slug}.png       ← 多张时继续编号
```

---

## 版本

Public / 产品 `3.0` · 三风格可选 + 自定义 IP · visual-promise SSOT
