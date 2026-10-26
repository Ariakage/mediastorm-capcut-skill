# mediastorm-capcut-skill

基于影视飓风（MediaStorm）付费教学内容整理的剪映（CapCut）剪辑技巧 AI Skill / 个人学习笔记。

## 📖 简介

本项目将影视飓风（MediaStorm）付费教学课程中涉及的剪辑判断、操作技巧与制作发布流程，整理为组合 Skill / 笔记，支持 capcut-cli、剪映界面及其他视频工具。入口与子 Skill 的分类在课程研读后确定。

> ⚠️ **重要提示**：本项目仅供个人学习与交流使用，请勿用于任何商业用途。详见 [SECURITY.md](SECURITY.md)。

## 📂 内容

- 项目接入、素材与代理准备
- 叙事结构、镜头组接与节奏判断
- 口播、采访、多机位与字幕
- 音乐裁切、声音桥与音效设计
- 变速、慢放与源帧率判断
- 关键帧、点跟踪标签与数字包装
- 抠像、蒙版、混合模式与平面跟踪
- Log 还原、示波器与跨镜头调色
- 生成式 B-roll 的授权与真实性检查
- 导出、版本、归档与跨端交付

## 🚀 使用入口

Skill 源码位于 [skills/](skills/)，已安装到 `~/.codex/skills/mediastorm-*`。在 Codex 中显式调用：

```text
Use $mediastorm-capcut to route this CapCut editing task.
```

入口会按任务组合 10 个子 Skill。通用 CapCut 草稿读写仍使用现有 `capcut-edit`，本组合 Skill 侧重剪辑判断、路由、证据边界和验收。

> 当前为未验收草稿版：连续视频与原声听辨尚未完成。调用时不要把课程案例参数当作固定预设，也不要跳过剪映重开与最终视听检查。

## 当前建设状态

- [执行计划与验收标准](AGENTS.md#详细执行计划与验收标准)
- [逐课进度与证据含义](progress/README.md)
- [逐课证据状态表](progress/status.md)
- [01–07 课初轮笔记](notes/course-reading-01-07.md)
- [08–18 课初轮笔记](notes/course-reading-08-18.md)
- [音画理解接口方案调查](notes/multimodal-options.md)
- [完整音画待验清单](progress/remaining-review.md)
- [组合 Skill 源码](skills/)（草稿版，未完成音画验收）

18 课共 03:41:55，全部 6,198 条字幕已研读；全音轨本地 ASR 与 453 个分窗比对已完成，36 页索引中的 674 个静态抽样画面已查看。上述证据仍不包含完整原声听辨与连续视频理解，18 课的完整音画验收均待完成。

2026-10-26 后续会话已按用户指示暂缓视频读取，并建立 `skills/` 组合 Skill 草稿：1 个入口 Skill 与 10 个按任务边界划分的子 Skill。用户两次以 `@` 引用本地 MP4 时，当前上下文只提供路径，Read 接口返回二进制不可显示；Kimi API 的 Base64/video_url 路线尚未获授权执行。因此该 Skill 是未验收草稿，不表示课程已经完整学完。

课程原始视频、完整字幕、抽帧、音频、全文转写和分析缓存仅保存在本地 `cheese/`，不纳入仓库或 Skill 分发包。仓库只保留原创总结、时间码引用、进度及工具脚本。

## ⚠️ 免责声明

- 本项目使用的部分视频素材来源于 **影视飓风（MediaStorm）的付费教学课程**，版权归原作者所有。
- 本项目与影视飓风（MediaStorm）无任何官方关联，仅为个人学习笔记性质的整理。
- 内容 **仅供学习交流，禁止商用、禁止二次分发付费课程内容**。
- 如有侵权请联系删除（请通过 GitHub Issues 联系）。

完整的版权与免责声明请查看 [SECURITY.md](SECURITY.md)。

## 📄 许可证

本项目的原创整理内容采用 [MIT License](LICENSE) 开源。

> 注意：MIT 许可证仅适用于本仓库中作者原创的代码与文字整理内容，**不适用于** 影视飓风（MediaStorm）享有版权的课程素材。
