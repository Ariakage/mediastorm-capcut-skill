# AGENTS.md

本文件为 AI 助手与协作者提供本项目的背景、规范与工作约定。开始任何修改前请先阅读本文件。

## 项目概述

`mediastorm-capcut-skill`：基于影视飓风（MediaStorm）付费教学内容整理的剪映（CapCut）剪辑技巧 AI Skill / 个人学习笔记。

- 主要语言：Markdown（中文）
- 性质：个人学习项目，非官方、非商业

## 目录结构

- `cheese/`：本地课程素材目录（`视频/`、`字幕/`），**已被 .gitignore 排除，永不提交**。
- 其余文件（README、LICENSE、SECURITY、AGENTS 等）为可公开的项目文档。

## 内容红线（最高优先级）

1. 本项目部分视频素材来自 **影视飓风（MediaStorm）付费教学课程**，仅供学习交流使用。
2. **禁止** 将付费课程原始视频、完整录屏等素材提交进仓库；仓库中只保留个人整理的文字笔记与技巧总结。
3. 任何涉及课程内容的描述需注明来源，不得声称与影视飓风官方存在关联。
4. 发现侵权或敏感内容时，立即删除并更新 [SECURITY.md](SECURITY.md)。

## Git 提交规范（强制）

**所有提交必须使用规范的 Conventional Commits 格式：**

```
<type>(<scope>): <subject>

[body]

[footer]
```

### Type 白名单

| Type | 用途 |
| --- | --- |
| `feat` | 新增内容 / 新功能（如新增一篇技巧笔记） |
| `fix` | 修正错误内容（错别字、错误步骤、失效链接） |
| `docs` | 纯文档变更（README、SECURITY、AGENTS 等） |
| `style` | 格式调整，不改变内容含义（排版、空格、标点） |
| `refactor` | 内容重构（目录调整、笔记拆分合并） |
| `chore` | 杂项（配置、忽略文件、构建脚本等） |
| `revert` | 回退之前的提交 |

### 规则

- `subject`（标题）**必填**，使用简洁的祈使句，结尾不加句号。
- `scope` 可选，表示影响范围（如 `readme`、`security`、`notes`）。
- 标题建议不超过 50 个字符；body 每行不超过 72 个字符，用于说明"为什么"而非"做了什么"。
- 中英文混排时注意空格规范，保持全仓库一致。

### 示例

```
feat(notes): 新增剪映关键帧动画技巧笔记
fix(readme): 修正免责声明中的素材来源描述
docs(security): 补充敏感内容报告流程
chore: 添加 .gitignore
```

**不符合以上格式的提交信息一律视为无效，需通过 `git commit --amend` 或 rebase 修正后方可推送。**

## 文档维护约定

- 修改本文件涉及的任何规范、结构或流程时，必须同步更新本文件。
- 版权 / 免责声明相关变更需同步检查 [README.md](README.md) 与 [SECURITY.md](SECURITY.md) 保持一致。
- 许可证文件为 [LICENSE](LICENSE)（MIT），不得擅自更换协议；注意 MIT 仅覆盖本仓库原创内容，不覆盖影视飓风版权素材。
