# Street Photo Illustration

**FANTASY / 梵想美学 · 摄影与照片转译**

把照片中的人物转成黑白线稿或彩色插画，保留真实环境、姿态、服装与人物关系。

**[快速开始](#start)** · **[下载与安装](#install)** · **[完整规则](SKILL.md)** · **[全部视觉 Skills](https://github.com/dacnay816y62-hub?tab=repositories)**

| 视觉示例 01 | 视觉示例 02 |
| :---: | :---: |
| ![Street Photo Illustration · 示例 1](examples/black-ink-fishing.png) | ![Street Photo Illustration · 示例 2](examples/color-picnic.png) |

<a id="start"></a>

## 一分钟开始

| 你提供 | 这套 Skill 组织的交付 |
| --- | --- |
| 街拍、旅行或生活场景照片 | 真实摄影环境与插画人物组合，可选少量文字 |

```text
用 $street-photo-illustration 处理这张街拍，选择 BLACK INK。把人物替换成清爽黑白线稿，保留动作、衣服与手持物，环境继续保持照片质感，不加文字。
```

**生成说明：** Skill 组织设计判断、提示词与执行流程；图片由当前环境中可用的图像工具生成或编辑。示例用于理解视觉方向，具体来源以本仓库记录为准，不能据此保证每次得到相同效果。

<a id="install"></a>

## 下载与安装

**[下载当前分支 ZIP](https://github.com/dacnay816y62-hub/street-photo-illustration-skill/archive/refs/heads/main.zip)** · **[阅读 Skill 规则](SKILL.md)**

1. 下载并解压仓库。
2. 将仓库根目录（包含 `SKILL.md`）放入当前助手支持的技能目录。
3. 安装文件夹命名为 **`street-photo-illustration`**，确保入口是 `street-photo-illustration/SKILL.md`。
4. 在支持技能调用的会话中使用 **`$street-photo-illustration`**。如果列表未刷新，新开一个任务。

Codex CLI / IDE 的用户级目录是 `~/.agents/skills/`，项目级目录是 `.agents/skills/`；Windows 用户目录可写为 `%USERPROFILE%\.agents\skills\`。以 [OpenAI 官方安装说明](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) 为准。ChatGPT 与其他宿主请按各自的技能加载方式使用。

仓库名与调用名可能不同，以上以 `SKILL.md` 中的名称为准。安装不包含图像服务、账户或生成额度；实际出图取决于你使用的环境。

---

## What it does

- 只改人，不改环境
- 支持两种人物风格：`BLACK INK` 和 `COLOR CHIBI`
- 适合街景、河边、公园、夜市、杂货店、地铁、机场、书店、洗衣房、咖啡店等真实照片
- 保留姿势、服装轮廓、配饰、手持物与场景透视
- 可选环境感文案与轻量涂鸦

## How to use

Use `$street-photo-illustration` to transform the people in this photo while keeping the real environment unchanged.

Templates:

- `prompts/black_ink_template.md`
- `prompts/color_chibi_template.md`

## Modes

### BLACK INK

黑白手绘、线条清爽、人物更像贴进照片里的纸感角色。

### COLOR CHIBI

彩色、轻松、编辑感更强，适合生活方式、旅行、商业空间和社交内容。

## Examples

### BLACK INK

<table>
  <tr>
    <td width="50%">
      <img src="examples/black-ink-fishing.png" alt="Black ink fishing" width="100%" />
      <br><strong>River / fishing</strong>
    </td>
    <td width="50%">
      <img src="examples/laundry-queue.png" alt="Black ink laundry" width="100%" />
      <br><strong>Laundry scene</strong>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="examples/market-signage.png" alt="Black ink market" width="100%" />
      <br><strong>Market browsing</strong>
    </td>
    <td width="50%">
      <img src="examples/stationery-shop.png" alt="Black ink stationery" width="100%" />
      <br><strong>Stationery shop</strong>
    </td>
  </tr>
</table>

### COLOR CHIBI

<table>
  <tr>
    <td width="50%">
      <img src="examples/color-picnic.png" alt="Color picnic" width="100%" />
      <br><strong>Picnic / lake side</strong>
    </td>
    <td width="50%">
      <img src="examples/night-market-couple.png" alt="Night market couple" width="100%" />
      <br><strong>Night market</strong>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="examples/record-store.png" alt="Record store" width="100%" />
      <br><strong>Record store</strong>
    </td>
    <td width="50%">
      <img src="examples/morning-baozi.png" alt="Breakfast street" width="100%" />
      <br><strong>Breakfast street</strong>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="examples/new-drop-beauty.png" alt="Beauty store" width="100%" />
      <br><strong>Beauty / retail</strong>
    </td>
    <td width="50%">
      <img src="examples/boarding-mood.png" alt="Airport mood" width="100%" />
      <br><strong>Airport / boarding</strong>
    </td>
  </tr>
</table>

## Repository layout

- `SKILL.md`: core skill instructions
- `agents/openai.yaml`: UI metadata
- `prompts/`: mode-specific prompt templates
- `assets/icon.svg`: skill icon
- `examples/`: sample outputs for the README

## FANTASY / 梵想美学

**让想象先被看见。** 将视觉判断与创作流程整理成可以继续使用的方法。

**[浏览全部视觉 Skills](https://github.com/dacnay816y62-hub?tab=repositories)** · [废片焕新 · Photo Revival](https://github.com/dacnay816y62-hub/photo-revival) · [FANTASY 奇奇怪怪](https://github.com/dacnay816y62-hub/fantasy-qiqiguaiguai-skill)
