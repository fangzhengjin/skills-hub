# Changelog

本文件记录面向用户的 **Release 版本**。

## [3.0.0] — 2026-08-03

### Added

- **多风格**：正式公开三套可选风格
  - 怪诞手绘（`quirky-sketch`，默认）
  - 暖调绘本（`warm-storybook`）
  - 产品方案（`product-proposal`）
- 公开 `references/visual-promise.md`（视觉承诺 SSOT）
- `gimi` / `none` 三风格校准样板进入发布包
- README：自然语言选风格说明与三风格效果预览

### Changed

- 配图协议同步：prompt / shot-config / QA / IP 合约适配多风格与双参考 / 无 IP style-single
- 无角色样板文件名统一为四件套命名（`none-change-chaos` 等）

### Security / Publish

- 仍不公开 `references/styles/_template.md`（不承诺用户自建风格）
- 公开发布线仅含演示资产 `gimi` / `none`；测试用自定义 IP **不**进入公开仓

## [2.0.0] — 2026-07-17

### Added

- **自定义 IP**：触发词 `录入 IP` / `自定义 IP` / `上传形象` / `新建 IP`
- 公开 `references/ip/_template.md`（合约 + Step 0 录入流程）
- SKILL 文首路由分流：录入时防 ImageGen 抢跑；半身/全身首轮统一零生图
- 双参考协议（`ref_mode: dual | single`）、设定图全身落盘、16:9 风格样板镜校准

### Changed

- 配图协议层同步：prompt / quirky-sketch / gimi IP 合约字段（动作库、序列图导游等）
- README：补充「录入 IP + 附图」onboarding

### Security / Publish

- 公开发布线仅含演示资产 `gimi` / `none`；测试用自定义 IP **不**进入公开仓

## [1.1.0] — 2026-07-08

### Added

- README 效果预览：6 张示例图（Gimi IP ×3 / 无角色 ×3）
- README 关于作者：GitHub + 小红书链接

### Changed

- IP-NOTICE 精简著作权说明
- README 效果预览：纵向大图展示（无角色在前），非表格排版
- README 预览图改用 jsDelivr CDN，修复国内加载失败

## [1.0.0] — 2026-07-08

> 工作流架构受开源配图 Skill 生态启发；本仓库角色与资产均为独立创作。

### Added

- 开源发布：怪诞手绘单风格（`quirky-sketch`）
- Gimi IP / 无角色（`none`）双模式
- 默认 16:9，支持用户指定比例
- 配图策略落盘（`shot-config.md`）+ QA 质检流程
- Codex `@Image Gen` 双参考图协议（Gimi IP）
