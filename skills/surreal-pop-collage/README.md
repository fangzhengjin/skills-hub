# 超现实波普拼贴 · Surreal Pop Collage

一个给 AI 编程/agent 工具用的图像生成 skill：把任意照片变成**超现实波普拼贴画**——照片去色保留为"现实锚"，背景换成巨大平涂色形，全图只有一个"不可能的巨物"。

> 黑白现实、平涂梦境、一物不对劲、元素源于图、色从图中来。

## 效果

（示例图见 `examples/`——风景、城市、人物三类示例。）

## 安装

**Kimi Code / Claude Code / Codex 等 agent 工具**：把本仓库的 `SKILL.md` 与 `agents/` 复制到你的 skills 目录（如 `~/.kimi-code/skills/surreal-pop-collage/`），agent 会在你说"把这张照片做成超现实拼贴"时自动调用。

**任何生图工具（ChatGPT / Midjourney / 即梦等）**：不用安装，直接按下面的配方手写 prompt。

## 用法（30 秒版）

1. 选一张照片，写下三行：主体是什么 / 主色是哪两个 / 它在哪
2. 定平涂色形：从主色出发——提纯、互补、或情绪反转，三选一，2–3 个大色形替换背景
3. 定巨物：**只能一个**，从场景里长出来——图里的小东西放大 / 语义最远的东西 / 尺度颠倒；文化地标就用它的典故
4. 按四段式拼 prompt：

```
surreal pop collage, vertical 3:4,
keep the [主体] clearly recognizable but desaturated to black and white,
the background replaced by huge flat matte color shapes: [色形与颜色],
one impossible giant element: [巨物],
[小元素群] in graduated sizes following an arc,
a few white hand-drawn graffiti strokes,
flat matte colors, no gradients, no text, no watermark
```

完整规则（决策优先级、色形推导、巨物选择、纠偏表、质量门）见 `SKILL.md`。

## 核心规则速览

- **一物不对劲**：巨物唯一。第二个不可能元素出现就删——超现实的力量全在"只有一处不对劲"
- **元素源于图**：巨物和色形都必须能从原图指出出处；禁止默认的红日/蓝天/海豚/鲸鱼
- **平涂无渐变**：色形不许有渐变和立体阴影，这是和照片真实感对撞的关键
- **典故巨物**：文化地标照片，巨物从典故里选，但先翻译成可见的物件或动作（例：白居易开凿山塘河→灯笼升空成月）
- **中文后期排**：生图模型写中文必乱码，prompt 里 `no text`，标题后期用代码排

## 示例图

见 `examples/`：

- 城市街景：黄色天空来自出租车的黄，巨物是吊在楼谷间的红绿灯
- 更多示例陆续补充（风景/人像/文化地标系列）

## License

MIT
