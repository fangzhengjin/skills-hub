## Skills Hub

本仓库将分散在独立 GitHub 仓库中的 Skills 同步为 `skills/` 下的真实文件，便于只识别统一 Skills 目录的工具安装和读取。

## 技能清单

<!-- skills:start -->
| Skill | 用途 | 上游仓库 | 最近同步时间 |
|---|---|---|---|
| `gc-minimal-zine-poster-v0-1` | 根据主题、语句、物件、情绪或内容简报，生成留白克制、带旧纸质感的极简 Zine 编辑海报提示词与位图图像 | [LiamGvchi/gc-minimal-zine-poster](https://github.com/LiamGvchi/gc-minimal-zine-poster) | — |
| `photo-abstract-editorial` | 保留上传照片原貌，并组合从照片提炼的抽象记忆面板与诗意英文标题，生成竖版编辑作品 | [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial) | — |
| `scene-distillation-zine-v1-3` | 将上传照片蒸馏为不保留原始摄影像素的极简艺术纸刊插画，以情绪张力、视觉隐喻、留白、结构性色彩和自由文字重构场景 | [Zeejay0/gathered-scenes-zine-skill/skills/scene-distillation-zine-v1-3](https://github.com/Zeejay0/gathered-scenes-zine-skill/tree/HEAD/skills/scene-distillation-zine-v1-3) | — |
| `scenes-gathered-zine-v1-3` | 保留真实摄影作为锚点，并以简化插画、结构性色彩、主动留白和手撕纤维边缘重组为竖版纸像海报 | [Zeejay0/gathered-scenes-zine-skill/skills/scenes-gathered-zine-v1-3](https://github.com/Zeejay0/gathered-scenes-zine-skill/tree/HEAD/skills/scenes-gathered-zine-v1-3) | — |
| `photo-revival` | 将普通照片或日常随手拍重新绘制成大面积白纸留白、局部鲜明色彩和微小手写文字的诗性手绘插画 | [dacnay816y62-hub/photo-revival](https://github.com/dacnay816y62-hub/photo-revival) | — |
<!-- skills:end -->

技能来源、目录名和用途统一维护在 `skills.json`，上表由同步脚本自动生成。各 Skill 的权利和许可仍归对应上游项目及作者所有。

配置中的 `path` 用于指定仓库内的 Skill 子目录；省略时同步仓库根目录。

单个上游仓库不可用或 Skill 被删除时，同步会保留该 Skill 上次成功同步的版本，并继续处理其他来源。

“最近同步时间”由同步脚本按 `UTC+8` 自动维护，仅在对应 Skill 内容成功更新时变化。

## 使用

克隆本仓库后，将 `skills/` 下所需目录复制到目标工具的 Skills 目录，或在工具支持时直接使用本仓库的 `skills/` 目录。

`skills/` 是同步产物，不应直接修改。如需新增或调整来源，请编辑 `skills.json` 后手动运行 GitHub Actions，或等待每日自动同步。

本地同步无需安装第三方 Python 包：

```bash
python3 .github/scripts/sync_skills.py
```

GitHub Actions 从东八区时间 `00:00` 开始，每隔 6 小时运行一次，也支持手动触发。只有上游内容发生变化时才会产生同步提交。
