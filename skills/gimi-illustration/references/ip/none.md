# IP · 无角色模式（none）

> `$IP=none`：**无 Gimi 品牌 IP**，不是「画面禁止出现人」。

---

## 填入 `{IP_DESC}` 的内容

```
No branded IP character (NOT Gimi — no horse hood, cube pendant, or reference-character look).
Object- and scene-focused composition is default.

When shot-config assigns an information role to a user or AI, you MAY add 1-2 simple generic figures:
- generic stick-figure user (worry, action, at desk) — small, sketchy, no detailed portrait
- simple robot labeled AI — round, friendly, not a branded mascot
Figures are optional tools for information roles, not required in every image.
If figures are not needed, use objects and arrows only.
```

---

## 功能性简笔角色（按需，非强制）

| 何时用 | 画什么 | 禁什么 |
|--------|--------|--------|
| 信息分工需要「谁焦虑/谁操作/谁介入」 | 简笔用户、简笔机器人（标 AI） | Gimi 外貌、精细五官、品牌吉祥物 |
| 情绪状态 / 用户 vs 工具对比 | 同上，**小比例**，物件仍为主角 | 人物抢戏、占画面 >30% |
| 纯步骤/物件序列 | 通常不画人 | 为凑热闹加人 |

**原则：** none 省的是 **固定 IP 绑定**，不是省 **表意演员**。演员从当次 `信息分工` 来，不从灵感库盲套。

---

## 风格校准四件套

> 这是**运行时风格校准资产**，不是正式内容模板，也不是风格能力的完整测试题。每套已启用 `required style-single` 的风格，在 `assets/none/examples/{STYLE}/` 中提供同名 4 张；每次正式生成最多附 1 张。终端用户不上传图片，资产也不承担角色身份设定。

| 文件 | 固定校准题材 | 风格中立的微故事种子 | 何时选用 |
|------|--------------|------------------------|----------|
| `none-practice-loop.png` | 输入—实践—输出循环 | 工作台上的一张空白卡片经过试做、调整，成为完成品后又回到下一轮练习的起点 | 路径、步骤、循环 |
| `none-shareable-result.png` | 可交付成果与分享关系 | 一件完成的小作品从桌面被装进信封，沿着一条短路送到另一张桌面并被展开看见 | 成果、分享、部署、链接 |
| `none-change-chaos.png` | 变化、混乱与处理关系 | 一阵风把原本排好的卡片吹乱，卡片经过分拣和重新排列，恢复成可继续使用的顺序 | 问题、变化、协作处理 |
| `none-delivery-mainline.png` | 工具链到交付主线 | 材料从工具架出发，在装配台完成组合，沿着工作台进入明亮的交付门口 | 演示、工具链、交付、主线 |

### 微故事门槛（所有 required 无 IP 校准资产）

固定题材不是抽象流程图的四个标题，而是四个可复用的**风格中立微故事**。每张校准图必须能在 3 秒内复述出：

1. 一个具体场景；
2. 一个主行动者（可为物件、物件群，或本风格另行允许的极简通用人物）；
3. 一个看得见的动作或状态变化；
4. 一个能收束前后关系的结果。

可以用物件和路径讲故事，不要求出现人物、手、动物或长文字；但不得只堆叠装置、节点或抽象关系。故事种子只负责让风格校准图有可读事件，不引入品牌 IP、特定文章主题或正式业务语义。生成时仍须遵守当前风格的介质、色彩、疏密和文字规则；运行时仍不得复刻校准图的构图、标题、物件排列、标签或业务内容。

按 shot 主语义选择 1 张。人物、手势、文字密度、色彩和具体物件由当前 `styles/{STYLE}.md` 决定；四件套不强制所有风格画手或承载长文字。

运行时只学习当前风格声明允许的背景、线条、色彩、材质、空间和文字处理方式；不得复刻附件的构图、标题、物件排列、标签或业务语义。

---

## 物件 / 意象参考

困境、成长、焦虑、专注、选择等意象表见当次 **物件表意**；优先原文名词，物件表意不足且分工需要时再补简笔角色。

---

`v1.4` · 2026-08-01 · 四件套固定题材补充风格中立微故事门槛
