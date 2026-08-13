# GC Minimal Zine Poster v0.3.1

[English](README.md) · **简体中文** · [日本語](README.ja.md)

Minimal Zine Poster v0.3.1 是一个 Codex Skill：它可以把主题、句子、文章构想、物件、情绪、照片或参考图集，转化为一张纸张质感的极简编辑海报、一条可直接使用的生图 Prompt，或一套可复用的视觉系统。

调用名称为 `gc-minimal-zine-poster-v0-3`。

## v0.3.1 更新内容

- 用明确的视觉重心与色彩强调语言，替代可能被按字面误解的抽象构图术语。
- 要求最终生图 Prompt 写清实际可见载体，例如照片裁切、纸片、墨块、标本、印刷插图、纹理窗口或字体。
- 质量检查新增无关船用符号与通用图标检查。
- 新增一条非海事主题、鲜红色视觉重心的回归评测。
- 保留 Generate、Reference Analysis、Prompt-only、Analyze + Generate 和 Photo Input 路线。
- 为了向后兼容，调用名称继续使用 `gc-minimal-zine-poster-v0-3`。

## 视觉方向

这个 Skill 会把请求编排成一张留白充足的竖版纸张海报，主要特征包括：

- 默认 3:5 比例的仿旧纸张画布
- 70%–90% 的留白
- 一个小型、可被清楚表现的主体或视觉事件
- 衬线、打字机、等宽或克制的小号无衬线字体
- 一个清晰可见的高饱和度色彩强调区域
- 复印、孔版印刷、网点、凸版印刷或扫描纸张的瑕疵与质感
- 安静的日式／韩式独立 ZINE 或极简编辑设计氛围

它会避开商业广告式布局、光亮样机、电影感布光、3D 渲染、霓虹、密集拼贴、复制参考图身份以及大段整齐文字。

## 示例

以下六张示例图均由仓库作者制作。

| Night Door | Yellow Step |
| --- | --- |
| ![Night Door](examples/night-door.jpeg) | ![Yellow Step](examples/yellow-step.jpeg) |

| Shore Pause | Pause Map |
| --- | --- |
| ![Shore Pause](examples/shore-pause.jpeg) | ![Pause Map](examples/pause-map.jpeg) |

| Typhoon Memory | Moon Tide |
| --- | --- |
| ![Typhoon Memory](examples/typhoon-memory.jpeg) | ![Moon Tide](examples/moon-tide.jpeg) |

## 使用要求

- Codex 或兼容的 Skill 运行环境。
- 参考图分析和质量检查需要图片读取能力。
- 生成模式与分析后生成模式需要运行环境提供图片生成能力。

Skill 包中不包含脚本、外部字体、API 密钥、私有路径或需要下载的运行资源。最终生图质量和照片保真程度仍取决于运行环境中的图片模型。

## 安装

把当前 v0.3.1 克隆到名称一致的 Skill 目录：

```bash
git clone https://github.com/LiamGvchi/gc-minimal-zine-poster.git \
  ~/.codex/skills/gc-minimal-zine-poster-v0-3
```

如果 Skill 没有立即出现，请重启 Codex。

## 从 v0.3.0 升级

调用名称和安装目录保持不变。如果现有 v0.3 安装是干净的 Git 仓库，可以执行：

```bash
git -C ~/.codex/skills/gc-minimal-zine-poster-v0-3 pull --ff-only
```

如果该目录不是 Git 仓库，或包含本地修改，请先安装一份全新副本并比较差异，不要直接覆盖自己的改动。

## 从 v0.1 升级

不要在已有的 `~/.codex/skills/gc-minimal-zine-poster-v0-1` 目录里直接拉取 v0.3.1。文件夹名必须与 Skill frontmatter 中的名称保持一致。

请使用上面的安装命令，把 v0.3.1 安装在旧版本旁边。确认 v0.3.1 可以正常调用后，你可以自行决定保留或删除旧目录。

如果仍然需要安装保留的 v0.1：

```bash
git clone --branch v0.1.0 \
  https://github.com/LiamGvchi/gc-minimal-zine-poster.git \
  ~/.codex/skills/gc-minimal-zine-poster-v0-1
```

## 使用方法

生成海报：

```text
用 $gc-minimal-zine-poster-v0-3 做一张关于雨天旧书店的海报。
```

只分析参考图，不生成图片：

```text
用 $gc-minimal-zine-poster-v0-3 分析这个图片文件夹，区分固定规则和可变规则，不要复制原图文字，并给我一条可复用 Prompt。
```

把用户照片作为编辑目标：

```text
用 $gc-minimal-zine-poster-v0-3 把这张人物照片做成海报，保留人物身份和服装，只改变排版与纸张质感。
```

只要最终 Prompt：

```text
用 $gc-minimal-zine-poster-v0-3 写一条关于旧书店夜晚关门的最终生图 Prompt，不要出图。
```

## 请求模式

- **Generate：**内容 → 视觉隐喻 → Prompt → 位图生成 → 结果检查。
- **Photo Input：**确定图片角色和保真等级，把真实目标图片传入生成，并检查主体保留情况。
- **Reference Analysis：**检查真实文件，返回观察证据、固定规则、可变规则、样本残留、可复用 Prompt 和限制。
- **Prompt-only：**只返回四段式最终 Prompt 与 Recipe，不声称已经生成图片。
- **Analyze + Generate：**先提取视觉系统，再生成不复制原图构图的新作品。

## 输出

生成请求会返回：

1. 生成的位图海报
2. 最终生图 Prompt
3. 所选 Recipe
4. 一段简短的内容解释
5. 提供照片时的图片角色和保真信息

参考图分析请求会返回基于证据的视觉系统和可复用 Prompt；除非用户同时要求生成，否则不会出图。

## 仓库结构

- `SKILL.md`：请求路由与执行工作流
- `references/style-system.md`：固定风格、可变项、色彩、主体逻辑和避免方向
- `references/prompt-compiler.md`：Prompt 字段顺序和四段式编译器
- `references/variation-engine.md`：布局与变化方案
- `references/reference-analysis.md`：参考图证据与综合协议
- `references/quality-gate.md`：生成、参考分析和仅 Prompt 的质量检查
- `agents/openai.yaml`：Codex 界面元数据
- `evals/evals.json`：可复用评测 Prompt
- `examples/`：六张由作者制作的海报示例
- `LICENSE`：MIT 许可证

## 致谢

感谢小红书用户 **@李李** 指出：提示词中的抽象构图术语可能被模型按字面理解，生成无关的船用图标。这条反馈直接促成了 v0.3.1 对术语、Prompt 编译器、质量检查和回归评测的系统修复。

## 许可证

MIT。详见 [LICENSE](LICENSE)。
