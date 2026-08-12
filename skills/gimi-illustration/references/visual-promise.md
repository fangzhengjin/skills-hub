# Visual Promise · 视觉承诺闸门（SSOT）

> **单一真相源。** 结构 / 外参 / 域物件 / 意象 的细则只写本文件。  
> `SKILL.md` · `shot-config` · `prompt-template` · `qa-checklist` · `composition-patterns` **只许指针 + 字段名**，禁止再复制本章正文。  
> **不进** `styles/*.md`。新坏例默认：**归类进子型 → 实例池加一行**；禁止新开 Tn 并四文件各贴长文。

---

## 父规则（一句）

**本张图对观众做了什么可核验承诺？**  
有承诺 → 必须走对应真值路径 + QA；做不到 → **降级**并禁止假装（假地标真标签、错域万能隐喻、刚体错位当成品）。  
无承诺 → 意象/轻约束。

**身份一致性（批内人稳 / IP 锚点）不归本闸门** → 见 `ip/_template` + `qa-checklist` IP 条。

---

## 子型（只这四类）

| 子型 | 视觉承诺取值 | 真值路径 | 典型债编号（考古） |
|------|--------------|----------|-------------------|
| **结构** | 与其它并列；字段「硬物件结构」≠无 | 刚体几何自洽；可简化态 | T2 |
| **外参** | `外参参考`（旧称 `参考地标` 等同） | 主锚检索→特征 3–5；**默认不附图**；失败/超时→意象 | T4 |
| **域物件** | `域物件` | 域内物件池优先于万能隐喻；IP 后置导游 | T5 |
| **意象 / 无** | `意象` / `无` | 泛称氛围；禁贴真名/真品牌 | — |

一张 shot **可叠**结构 +（外参|域物件|意象|无）。例：桌面加班 = 结构 + 无；数学极限 = 域物件 + 或有结构；汕头小公园 = 外参 ± 结构。

---

## 写协议纪律（防膨胀 · Agent 自检）

改规则前自问：

1. 这是**新父规则**还是**已有子型的新例子**？例子 → 只改本文件「实例池」或当次 shot-config。  
2. 是否又要在 4 个文件各写一段？→ **停**。全文只进本文件；别处一行指针。  
3. QA「必过」与「失败信号」是否重复？→ 失败信号只列非显然反例，或写「见本文件 §QA」。  
4. 债编号 Tn 是否要变成永久模块名？→ **否**；过线后折叠进子型。

---

## A · 结构（硬物件）

**何时：** 物件表意含刚体/开合件（笔记本、翻盖、书本开合、手机/平板外框、杯、有腿家具等）。

**shot-config：**「硬物件结构」写开合态 · 铰链 · 视角一句。拿不准 → **简化态**（合上/侧视/清晰四分之三）。

**SUBJECT 追加：**

```
Rigid object structure lock: <硬物件结构>.
Laptop/book/clamshell: lid and base share ONE hinge axis and ONE perspective; keyboard plane aligned with body; no floating lid, no mismatched key grid.
Phone/tablet/monitor: readable rectangular bezel; cup: elliptical rim consistent with cylinder; chair legs plant on the ground plane.
Prefer simpler open state over broken complex hinge.
Do NOT fix structure by changing style DNA — redraw geometry.
```

**QA：** 盖/键/铰链一体可读；杯口椭圆与圆柱一致；不过 → 改 SUBJECT/简化态，禁改 DNA。

---

## B · 外参（方案 A · 非见词雷达）

**取值：** `外参参考`（可用旧词 `参考地标`）。

**产品张力（写死）：** 认得出地标 ↔ 手帐介质。治本是 **结构身份锁特征清单**，不是站站附图、也不是关外参。

**触发（须其一）：**

1. 具名地点/品牌/可核验对象是**本张场景主语**  
2. **唯一锚定**同时成立：（a）全文锁城市/行程等语境；（b）当地公认用法；（c）本张场景即该处  

**不触发 → 直接 `意象`（不搜、不问）：** 比喻；一笔带过非主语；通名；推断缺任一项。

### B1 · 批次主锚 + 检索预算（治「搜很久」）

多站/旅行/攻略类批次（≥2 个具名地点或路径序列）：

| 规则 | 硬上限 |
|------|--------|
| **外参主锚** | 全批最多 **2** 张 shot 标 `外参参考`（挑场景主语最强、最需要认得出的站） |
| **其余站** | 强制 `意象`（泛称标注）；**禁止**站站搜 |
| **同地复用** | 同一地点多 shot → 复用已有「地标特征」，**禁止**重复检索 |
| **单站检索** | 最多 **2** 张图；墙钟约 **15s**（到点即停） |
| **失败** | 超时 / 0 结果 / 特征写不满 3 条 → **静默降级 `意象`**（不问用户） |

单站文章（全文只有一个场景主语）→ 仍可 1 站外参，但单站预算同上。

### B2 · 执行路径（默认特征锁 · 治「太写实」）

不问用户，按序：

1. 仅对 **B1 主锚** 检索（预算内）  
2. 写出特征清单 3–5 条（**结构身份 / 剪影可读**，非「像某张网图」）→「地标特征」  
3. **默认：检索图只供 Agent 读图写特征，不附给生图工具**（IP 校准图照常附）  
4. **例外附图**（须同时满足）：用户当次明示「要认得出 / 攻略可辨 / 必须像真地标」→ shot-config「外参附图」= `是`，且仍走下方「附图」SUBJECT；仍禁抄 OCR  
5. 失败/超时/特征不足 → 降级 `意象`：标注改**泛称**（仍 2–5），**禁止**仍贴真名  

### B3 · SUBJECT

- **外参参考 · 默认（不附图）：**  
  `Landmark identity lock from feature list only (structure silhouette, not photo texture): <特征>. Stylize heavily into current style medium (watercolor sketch journal when warm-storybook); suppress photo micro-detail, brick/wave/metal texture, photoreal lighting. Do NOT imitate any web photo look. Prefer simplified readable landmark silhouette. STYLE medium outweighs realism. Do NOT copy photo/map OCR text; still include 2-5 handwritten scene labels from shot-config (feature words or generic place nouns).`
- **外参参考 · 例外附图（外参附图=是）：**  
  `Landmark identity lock (structure, not photo texture): <特征>. Attached landmark refs are silhouette/layout identity ONLY — stylize heavily into current style medium; suppress photo texture/detail; STYLE medium outweighs photo realism. Do NOT copy photo/map OCR text; still include 2-5 handwritten scene labels from shot-config.`
- **意象（含降级）：**  
  `Imagery channel: generic atmosphere; do NOT use real place/brand names as labels; DO still draw 2-5 handwritten Chinese labels + thin arrows from shot-config (generic nouns only).`

**介质门禁（外参成功后仍检）：** 角色与环境须同介质；禁「角色简笔 + 地景照片级纹理」分裂；边角仍须露纸/手绘简化，勿用 STYLE_DNA 改几何冒充。

**同类：** Logo、真实 UI、公众人物、正典形制、图内事实数字 — 同一闸门（预算与「默认不附图」同理；用户咬定可辨才附图）。

---

## C · 域物件（T5）

**何时：** 文章属明确知识/专业域（数学、医学示意、工程流程等），画面要「像在讲这个知识」，而非情绪万能隐喻。

**流程（合入 Step 2 创意生成法）：**

```
领域识别 → 专业对象提取（域内物件池）→ 场景化视觉表达 → 构图/动线 → 再叠加 IP
```

**硬规则：**

1. **域物件优先于万能隐喻**（禁默认钥匙/围栏/灯泡/机器替数学结构，除非原文就是该隐喻）  
2. 主载体从域物件池或原文专业名词派生；IP 只讲解/指点，不抢走专业物件  
3. 不做巨型领域分类器；池子可增行，不新开宪法节  

### 实例池（可增行，不改其它文件）

| 域 | 优先物件（示例） | 慎用/禁默认 |
|----|------------------|-------------|
| **数学** | 坐标系、函数曲线、数轴、离散点、上下界、误差距离、递推箭头 | 钥匙、围栏、齿轮、万能机器 |
| **职场工具** | 原文具名：文档、弹窗、分支、终端 | 放大镜/灯泡（无原文语义时） |
| **旅行外景** | 走 **B·外参**；非域物件池 | 假地标+真标签 |

**shot-config：** `视觉承诺=域物件`；「域物件」字段列 2–5 个专业名词（可与物件表意合并注明）。

**SUBJECT 追加：**  
`Domain objects first: <域物件列表>. Prefer these over generic metaphors (keys/fences/machines) unless source text uses that metaphor. IP character guides; domain objects carry the meaning.`

**QA：** 3 秒内能说出域内物件名；若只见万能隐喻而正文是专业概念 → 不过，回改物件表意。

---

## D · 意象 / 无

- `意象`：有场景氛围但无可核验专名义务（或外参已降级）  
- `无`：无外景/品牌/域教学义务（纯情绪、抽象选择等）  

标注禁止假装外参真名；**仍须有泛称标注**（见下节）。

---

## E · 标注纪律（禁真名 ≠ 禁标注）

> **治本：** 外参诚实 / 不抄地图 OCR / 后期叠字，都**不能**默认推成「图内零标注」。  
> 坏 case 根因：shot-config 写「标注词：无，文档外 caption」→ `{LABEL_DESC}` 走无字分支。

| 规则 | 内容 |
|------|------|
| **默认** | 每张 **2–5** 个短中文标注 + 细箭头，挂阅读动线节点（见 composition） |
| **外参参考** | 可用真地标名（当特征过线）；或特征词（骑楼、栈道、观景台） |
| **意象 / 降级** | **禁真地名/真品牌**；改用泛称（老城骑楼、小吃街、海岸步道）——**字数仍 2–5，不是 0** |
| **不抄参考图** | 禁止复制照片/地图上的 OCR 小字；**另写** shot-config 标注词 |
| **零标注例外** | **仅当用户明示**「图内不要字 / 后期自己叠字 / caption 在文档外」→ 标注词才可写「无（用户要求）」 |
| **禁止** | Agent 自行发明「文档外 caption 承担说明」而清空标注词 |

**SUBJECT（通用，接承诺锁后）：**  
`Keep 2-5 sparse handwritten Chinese labels with thin arrows on path nodes per shot-config; never drop all labels unless shot-config says user requested no in-image text.`

---

## shot-config 字段（汇总）

| 字段 | 填写 |
|------|------|
| **视觉承诺** | `外参参考` \| `域物件` \| `意象` \| `无`（旧 `参考地标`=`外参参考`） |
| **地标特征** | 仅外参参考：3–5 条；否则「无」 |
| **外参附图** | 默认 `无`；仅用户明示可辨时 `是`（见 §B2） |
| **域物件** | 仅域物件：2–5 个专业名词；否则「无」 |
| **硬物件结构** | 有刚体必填；否则「无」 |
| **标注词** | 默认 2–5；纪律见 §E |

---

## QA（一处写全 · 别处只指针）

**必过：** 视觉承诺已填且与画面一致；外参→特征可读（剪影身份，非照片复刻）；多站批外参数 ≤2；默认未附图；域物件→域内物件可见；结构→刚体可读；意象/降级→无真名标签但**仍有泛称标注**；未获用户免标许可时画面须有 2–5 标注+细箭；外参后无介质分裂/照片级微细节。  

**失败示例（非显然时才看）：** 假地标+真标签；见词误搜；站站检索拖死；特征清单空称外参；无用户可辨要求却附地标照片导致明信片写实；数学文只画钥匙围栏；笔记本铰链断裂却交付；**无用户免标却零标注/零箭头**；把「不抄地图字」执行成整图无字。

**迭代：** 改 shot-config / SUBJECT / 检索或降级；**禁止**改 STYLE_DNA 冒充承诺；缺标注 → 补标注词后重试，勿靠砍字「更干净」。

---

`v1.2` · 2026-07-22 · §B 主锚检索预算 + 默认特征锁不附图（治搜久/写实）
