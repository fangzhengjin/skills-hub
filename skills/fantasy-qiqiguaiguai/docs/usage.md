# Usage Guide

## Default Workflow

When the user says "帮我做", "整理一下", "直接出图", or provides life fragments, run:

```text
fragment_intake
fragment_inventory
privacy_check
moment_discovery
posting_intent
content_angle
template_select
humor_mechanism_select
headline_generation
supporting_copy
image_curation
visual_direction_compile
visual_generation_or_edit
quality_review
publish_package
```

Do not skip:

- `moment_discovery`
- `template_select`
- `visual_direction_compile`
- `quality_review`

## Output Format For Planning

```markdown
## 内容核心
一句话说明真正值得发的内容。

## 推荐模板
T1 / T2 / T3 + 简短原因。

## 主标题
最终主标题。

## 辅助文字
3-8 条真正有用的标签或补刀文字。

## 图片使用
首图、保留图、删除图、排序建议。

## 朋友圈正文
可直接发布的正文。

## 视觉简报
短版 visual_direction_compile。
```

## Direct Image Generation

For direct image generation, keep the prompt short and specific:

```text
【模板】T2 杂物拼贴版
【核心】把早餐碎片做成一份早高峰事故档案
【主标题】淡淡早饭，加重我淡淡的迟到
【画面】三明治、牛奶、闹钟、打车截图组成高密度拼贴
【排版】蓝黄黑白，撕纸、箭头、票据，主标题最大
【保护】隐藏聊天隐私，不新增无关主体
【比例】3:4
```

## Style Notes

- Use only one main joke per output.
- Do not explain what is already visible.
- Prefer a strong title over many decorative elements.
- Use outlines sparingly: sticker outlines, object cutout edges, red stamps, route arrows, label boxes.
- Keep small text functional, not decorative filler.

## Native 3:4 Testing Note

In testing, `gpt-image-2` through a Maliang-compatible `/images/generations` endpoint accepted:

```text
size: 768x1024
```

and returned native 3:4 images. Prefer this over square generation plus cropping when the user requires direct 3:4 output.
