# 接手说明：MediaStorm 课程学习与组合 Skill

更新时间：2026-10-26 17:05（Asia/Shanghai）。本文保存当前会话的决定、进度、产物和真实验收边界，不包含课程全文或媒体。

来源为影视飓风（MediaStorm）付费剪映课程的个人学习整理，与影视飓风官方无关联，也未获得官方授权或背书。

## 1. 当前结论

项目目录：

```text
/Users/ariakage/Documents/New project 10/cc/mediastorm-capcut-skill
```

**当前状态：组合 Skill 草稿已经建立、验证并安装到 Codex；完整课程音画学习仍未完成。**

- 已完成：18 课全部字幕阅读、全音轨本地 ASR、抽样画面查看、部分局部回查、原创笔记、逐课证据账本。
- 已完成：1 个入口 Skill + 10 个按任务边界划分的子 Skill，源码在 `skills/`，已安装到 `~/.codex/skills/mediastorm-*`。
- 已完成：Skill 结构、命名、Markdown 链接、界面 YAML、源码与安装副本一致性验证。
- 已完成：capcut-cli 0.31.1 的运行时契约检查脚本；实测 24 个相关命令契约齐全。
- 未完成：18 课连续视频理解、原声听辨、音乐/音效/语气/节奏感知、快速动作和音画同步验收。
- 因此：当前 Skill 是 **provisional / 未验收草稿版**，不得宣称课程已完整学完或 Skill 已通过最终音画验收。

最新用户决定：

1. 暂不继续读取课程视频，先制作 Skill。
2. 明确记录：本轮视频**没有**完成多模态读取。
3. Skill 名称和安装目录恢复为 `mediastorm-*`。
4. 用户已自行检查并确认技能注入成功。

## 2. 接手阅读顺序

1. [AGENTS.md](AGENTS.md)：项目规范、五阶段计划、内容红线和验收要求。
2. 本文件：当前状态、Skill 交付、视频输入限制、提交记录。
3. [逐课状态表](progress/status.md) 与 [证据账本](progress/course-ledger.json)。
4. [完整音画待验清单](progress/remaining-review.md)。
5. [01–07 课笔记](notes/course-reading-01-07.md)、[08–18 课笔记](notes/course-reading-08-18.md)。
6. [工具观察](notes/tool-observations.md)、[音画接口方案调查](notes/multimodal-options.md)。
7. Skill 入口：[skills/mediastorm-capcut/SKILL.md](skills/mediastorm-capcut/SKILL.md)。

不要重新批量转写、抽帧或重装已经可用的环境，先核对现有产物和缺口。

## 3. 原始目标与授权边界

原始目标：安装 [capcut-cli](https://github.com/renezander030/capcut-cli)，完整学习 `./cheese` 中的 MediaStorm 课程，并把剪辑判断、经验、手法、制作、交付和发布知识组织为支持 capcut-cli 及其他流程的组合 Skill。

用户已确认：

- 允许助手使用多模态能力。
- 采用“入口 Skill → 分类路由 → 具体 Skill”，不按课号或 CLI 命令硬分。
- 完整学习应包含音频、画面和字幕，不能以转写或抽样静帧替代。
- 允许本地 ASR，用于补充对白证据。
- 只对实质阶段成果做本地 Conventional Commits 提交，不逐课提交，不自动推送。
- 原始课程只读，所有媒体、字幕、抽帧、音频、全文转写和分析缓存留在被忽略的 `cheese/`。

当前授权状态：

| 操作 | 状态 |
| --- | --- |
| 本地读取字幕/图片、运行本地 ASR、整理笔记 | 已授权且已执行 |
| 制作、验证、安装本地 Skill | 已授权且已执行 |
| 本地 Git 提交 | 已授权且已执行 |
| 将课程上传第三方 API | 未授权，未执行 |
| 云端模型费用、剪映积分、会员功能消费 | 未授权，未执行 |
| 下载/试装新的 Omni 模型 | 未授权，未执行 |
| Git 远程推送、发布视频、分发付费素材 | 未授权，未执行 |
| 清理缓存、删除个人文件或其他项目资料 | 未授权，未执行 |

## 4. 证据覆盖与层级

| 项目 | 实际结果 | 不代表什么 |
| --- | --- | --- |
| 素材盘点 | 18 个视频、18 份 AI 中文字幕，共 13,315.178668 秒（03:41:55） | 不代表理解全部音画 |
| 字幕研读 | 6,198 条字幕全部实际读完，形成两份分课原创笔记 | 不代表听过原声 |
| 静态画面 | 20 秒间隔、36 页索引、674 个抽样画面实际查看，并有局部回查 | 不代表连续视频、运动或每帧验收 |
| 本地 ASR | 18 课完整音轨均提交本地识别 | 不代表音乐、音效、语气、声道、节奏感知 |
| 文本比对 | 453 个 30 秒窗口；10 个低相似度窗口的两份文本已回查 | 文本相似不证明正确，低相似也不自动证明字幕错误 |
| 局部重识别 | 第 06、09、11、15 课各一段；原始全轨结果保留 | 减少重复幻觉不等于原声已确认 |
| 原件保护 | 36 个视频/字幕 SHA256 与初始清单一致 | 后续操作仍需避免改写原件 |
| 连续视频 | 18 课均为 `pending` | 不能以静态帧或“提交成功”替代 |
| 原声听辨 | 18 课均未完成 | ASR 不能替代听感 |
| 完整音画验收 | 18 课均为 `false` | 不可宣布全课程学完 |

### 4.1 当前视频/音频输入事实

- 本地图片输入成功，曾实际查看第 01 课 00:20 等画面。
- 8 秒本地 WAV 经工具提交，返回 `audio content omitted because you do not support audio input`。
- 用户把 18 个 MP4 以 `@` 本地路径形式加入对话；系统上下文只提供路径，明确不是已上传的视频内容。
- 对第 01 课 MP4 再次调用 Read，返回 `Cannot display content of binary file`。
- 对 MP4 调用图片查看接口，返回 `unsupported format: .mp4`。
- 因此当前 WorkBuddy 会话**没有完成原生连续视频输入**，也没有完成原声听辨。
- 视频编码为 AV1 1080p / AAC；第 01 课约 112.17 秒、12.93 MB。
- 当前磁盘仅约 179 MiB 可用，任何模型下载或大体积转码都必须先评估空间。

### 4.2 Kimi/外部接口调查

公开文档核对结果：

- Kimi K3.1 Pro 文档支持视频视觉理解。
- Chat Completions 支持 `video_url`：可用 `data:video/mp4;base64,...` 或 `ms://<file-id>`。
- 文件上传支持 `purpose="video"`；文件接口单文件上限 100 MiB。
- Base64 适合较小文件；大文件应使用文件上传。
- 视频理解仍属于关键帧/采样理解，不应自动宣称覆盖每一帧和完整音轨。
- 文档主要说明视觉理解，不能据此确认音乐、音效、语气、声道等听觉验收。

本地发现：

- `kimi` CLI 存在。
- `hermes` 启动器存在，但其目标 `~/.hermes/hermes-agent/venv/bin/hermes` 不存在，当前不可用。
- 没有执行外部 API 调用、Base64 上传或费用消费。

如果未来恢复视频验收，需要重新取得：

1. 明确的提供商、模型、账户地区。
2. 上传范围与数据处理/保留条款确认。
3. 费用上限或预算授权。
4. 小型合成素材能力探针。
5. 课内短片试点，再覆盖全部课程。

## 5. 组合 Skill 交付

### 5.1 架构

源码目录：`skills/`。安装目录：`~/.codex/skills/mediastorm-*`。

入口：

```text
$mediastorm-capcut
```

部署形态：入口路由 + 10 个按编辑意图和验收对象划分的子 Skill。一个复杂任务可以按顺序调用多个子 Skill。

| 子 Skill | 适用任务 |
| --- | --- |
| `mediastorm-project-prep` | 素材盘点、编码/帧率、目录、重链接、代理、接入门 |
| `mediastorm-story-structure` | 叙事结构、信息密度、镜头组接、B-roll 意义、长短片节奏 |
| `mediastorm-dialogue-interview` | 口播、take、气口、字幕、A/B-roll、多机位与采访 |
| `mediastorm-music-sound` | 音乐裁切、尾音、J/L-cut、环境声、设计音效、响度 |
| `mediastorm-speed-time` | 常速变速、慢放、曲线变速、源帧率与补帧风险 |
| `mediastorm-motion-graphics` | 缩放/位置关键帧、缓动、点跟踪标签、数字闪变、计时器 |
| `mediastorm-compositing-tracking` | 抠像、蒙版、混合模式、图层合成、平面跟踪与失效 |
| `mediastorm-color-grading` | Log 还原、示波器、曲线、肤色、镜头匹配与风格 |
| `mediastorm-generative-broll` | 生成 B-roll、成本授权、提示词、真实性与审看 |
| `mediastorm-delivery-handoff` | 封面、版本、导出、归档、AI 超分补帧、跨端与发布检查 |

### 5.2 设计原则

- 入口只负责识别目标、检查前提、写出路由顺序、汇总验收和全局安全边界。
- 每个子 Skill 自带最小 references，不依赖仓库内 `notes/` 或 `cheese/.analysis/`。
- 通用 CapCut 草稿读写继续使用现有 `capcut-edit`，本组合 Skill 不复制命令手册。
- 课程知识以原创归纳为主，不复制完整讲稿。
- 证据标签：
  - `[课程]`：课程字幕、抽样画面、局部回查支持的归纳。
  - `[推论]`：助手推导，不冒充讲师原话。
  - `[工具]`：CLI 契约或本机实验，不自动外推到剪映界面。
  - `[待验]`：仍需连续音画或界面确认。
- 所有具体数值默认是案例参数，不是通用预设，包括 2–3 秒、0.3×/0.1×、约 2 帧、0.4 秒、45%、1080p/30fps、4K/60fps 等。
- 所有 Skill 的 metadata 标记 `status: provisional-unverified-audiovisual`。

### 5.3 确定性工具

`skills/mediastorm-capcut/scripts/check_capcut_contract.py`：

- 只读检查 CLI 版本与契约。
- 先运行 `describe --compact`，再按命令运行 `describe --command`。
- 不使用裸 `capcut describe`；本机 0.31.1 观察到此输出在 65,536 字节处截断。
- 默认验证 24 个命令，支持用 `--command` 缩小或扩展。
- 解析 JSON，检查 schema 2 和命令缺失。
- 不调用写入命令、渲染或草稿修改。

## 6. Skill 验证与安装状态

已完成：

- 11 个源码 Skill 和 11 个安装副本通过官方 `quick_validate.py`。
- 11 个前端目录名与 SKILL.md `name` 完全一致。
- 所有 Markdown 相对链接存在。
- 11 个 `agents/openai.yaml` 可被 YAML 解析。
- 源码与安装副本逐目录 `diff -qr` 一致。
- 入口契约脚本从源码和安装目录均可运行。
- 完整契约脚本验证：CLI 0.31.1、schema 2、88 个命令、24 个所需契约全部存在。
- 用户检查确认技能注入成功。
- 命名最终恢复为 `mediastorm-*`。

未完成：

- 两个独立前向测试子任务都因 429 频率限制失败，不能算通过。
- 没有在真实剪映工程中完成本 Skill 的端到端任务验收。
- 没有完成课程连续音画学习，因此内容层仍是草稿。

### 6.1 Codex 技能清单注意事项

本机 Codex 0.144.1 的初始技能目录受上下文预算限制，`codex debug prompt-input` 曾观察到只展示前 154 条技能，后面的名称被省略。

曾尝试把名称改为 `capcut-mediastorm-*` 以进入可见区间；用户随后要求恢复 `mediastorm-*`，并确认技能注入实际成功。

因此：

- 不要因为某次初始清单未显示全部 `mediastorm-*` 就再次自动改名。
- 精确名调用以用户当前环境和验证结果为准。
- 如需再次排查，使用 `$mediastorm-capcut` 显式调用并检查实际加载，而不是只看目录列表长度。

## 7. 本机环境

当前实测：

| 项目 | 当前值 |
| --- | --- |
| OS | macOS / Apple Silicon |
| `capcut` / `capcut-cli` | `0.31.1`，schema 2，88 个命令 |
| `node` | `v22.22.2`，由 fnm 管理；路径会变化，运行时用 `command -v` |
| `codex` | `codex-cli 0.144.1` |
| Skill 源码 | 11 个目录，35 个文件 |
| Skill 安装 | `~/.codex/skills/mediastorm-*`，11 个目录 |
| 可用磁盘 | 约 179 MiB（会变化，当前非常紧张） |
| ASR Python | `cheese/.analysis/.venv/bin/python`，Python 3.12 |
| ASR 模型 | `mlx-community/whisper-small-mlx`，revision `45f3915923c7a79a5a5b5a7d909d39aeb0e5630e` |
| 验证依赖 | ASR 环境已含 PyYAML；系统 Python 3 当前缺 `yaml` |

其他环境事实：

- `ffmpeg` / `ffprobe` 可用。
- 此前隔离临时新草稿 `init / info / lint` 冒烟通过。
- 既有加密剪映草稿不能直接用 CLI 读改；不要修改或清理它们。
- `render` 是 FFmpeg 代理预览，不是剪映最终渲染。
- `matting` 写智能抠像配置，不等于像素抠像已经完成。
- `detect-silence`、`detect-scenes`、`detect-retakes` 只产生候选。
- 当前 CLI 支持 `keyframe` 的 `linear / ease-in / ease-out / ease-in-out / hold`，但不等于完整曲线变速或平面跟踪。
- `loudness` 默认只测量，只有 `--apply` 才写入音量；命令级 `mutates` 不能完整表示选项副作用。
- 使用任何写命令前继续读取对应 `capcut describe --command <name>` 完整契约。

## 8. 文件位置

公开可提交：

| 路径 | 作用 |
| --- | --- |
| `AGENTS.md` | 规范、计划、内容红线和验收标准 |
| `README.md` | 项目简介、当前状态和使用入口 |
| `HANDOFF.md` | 本文，完整接手快照 |
| `progress/README.md` | 时间线、状态语义、分析命令 |
| `progress/course-ledger.json` | 逐课源哈希、模态状态、ASR/比对指标 |
| `progress/status.md` | 由账本生成的状态表 |
| `progress/remaining-review.md` | 连续音画缺口和优先回查段落 |
| `notes/course-reading-01-07.md` | 01–07 课原创归纳与时间码 |
| `notes/course-reading-08-18.md` | 08–18 课原创归纳与时间码 |
| `notes/tool-observations.md` | CLI、混合模式和 ASR 局限 |
| `notes/multimodal-options.md` | 音画接口调查 |
| `skills/mediastorm-capcut/` | 入口 Skill、路由、证据边界、契约脚本 |
| `skills/mediastorm-*/` | 10 个任务子 Skill 与各自 references |
| `scripts/course_audit.py` | 清单、字幕阅读稿、抽帧、ASR |
| `scripts/compare_dialogue.py` | 本地转写比对 |
| `scripts/check_progress.py` | 账本一致性、原件哈希和 Git 媒体排除 |
| `scripts/course-analysis-requirements.txt` | 分析环境依赖 |

本地私有、被 `/cheese/` 忽略：

```text
cheese/
├── 视频/                         # 18 个 AV1 1080p / AAC MP4
├── 字幕/                         # 18 份 .ai-zh.srt
└── .analysis/
    ├── .venv/                    # Python 3.12 + MLX/ASR/验证依赖
    ├── models/                   # Whisper 权重缓存
    ├── tiktoken/
    ├── asr/01.json ... 18.json
    ├── asr-checks/
    ├── dialogue-comparison/
    ├── visual/01 ... 18/
    ├── details/
    ├── cli-command-index.json
    ├── asr-run.log
    └── sheets-run.log
```

局部 ASR 原课程秒数：06 `[488,520]`、09 `[86,108]`、11 `[75,96]`、15 `[74,96]`。完整文本不得进入提交或 Skill 包。

## 9. 已确认的重要纠偏

- 课程采用 Final Cut Pro 快捷键预设，不能写成剪映通用默认快捷键。
- 第 06 课 07:06 烧录字幕为 `Drone`，不是 SRT 中的 `drum`；尚未直接听原声。
- 第 07 课 10:38 码率表印为 `KB/s`，单位和数值含义仍有歧义，不能直接生成 FFmpeg 参数或平台规则。
- 第 10 课画面确实把“强光”放在变亮相关分组；FFmpeg 实验只证明本机 `hardlight` 对灰底加纯黑覆盖会压黑，不证明剪映同名模式。
- 第 11 课 03:05 的 Apple Log2 / C-Log3 同屏是错误 LUT 匹配示范。
- 第 12 课跟踪面板、字幕阴影等单帧可能处于调整过程；中间值不是最终预设，两帧数字动画不能用低采样验收。
- 第 15 课时长和“时钟理论”是频道经验，不是生理学定律或平台保证。
- 第 16 课音乐段 ASR 有幻觉；两份识别相同也不证明真的有那些对白。
- 第 17 课 10:05 的 `Seedance 2.0 Fast` 只是录课界面记录，不保证当前可用或价格不变。
- 桌面 4K/60fps 与手机 1080p/30fps 是不同条件的示例，不能合并为统一平台规则。
- 已还原素材不能重复套技术 LUT。
- `matting` 配置写入不等于抠像像素完成。
- `render` 代理预览不等于剪映最终导出。

## 10. 后续执行顺序

### A. 如果继续完成课程音画验收

1. 明确可用的视频/音频输入接口和授权边界。
2. 用自制合成素材验证闪帧、连续运动、提示音、混响尾音和左右声道。
3. 做课内短片试点，先不提供字幕和笔记答案。
4. 记录源哈希、时间范围、音轨传入、采样/分辨率、模型、用量和截断情况。
5. 分段覆盖 18 课，边界重叠，核对并集无遗漏。
6. 对音乐、音效、语气、快速动作、变速和运镜做实际听视觉复核。
7. 只有所有模态和疑点完成，才把 `complete_multimodal_review` 更新为 true。
8. 依据新证据修正 Skill references 中标注 `[待验]` 的内容。

### B. 如果继续完善 Skill 而不重看视频

1. 用真实但隔离的剪映草稿测试技能路由和 capcut-cli 写入。
2. 对每个子 Skill 做真实任务前向测试，记录误路由和缺失判断。
3. 完成一次剪映界面重开、保存、听视觉验收。
4. 把“结构成功、代理预览成功、界面成功、最终听视觉成功”分别记录。
5. 继续保留 provisional 标记，直到课程和工具两层都达到验收。

### C. 任何时候都不要

- 把字幕、抽帧、ASR 或技能注入成功当成完整音画理解。
- 把课程案例数值写成所有项目固定预设。
- 把 `capcut render` 当成最终渲染。
- 把 `matting` 的 JSON 配置当成像素结果。
- 未授权上传课程、花积分、调用外部 API 或发布内容。
- 修改、删除或强制写入既有加密剪映草稿。

## 11. 快速复核命令

```sh
git status --short
git log -5 --oneline
python3 scripts/check_progress.py
```

更新账本后生成状态表：

```sh
python3 scripts/check_progress.py --write-summary
```

验证全部 Skill：

```sh
PY="cheese/.analysis/.venv/bin/python"
for dir in skills/mediastorm-*; do
  "$PY" "$HOME/.codex/skills/.system/skill-creator/scripts/quick_validate.py" "$dir"
done
```

验证 CLI 契约：

```sh
skills/mediastorm-capcut/scripts/check_capcut_contract.py
```

验证安装副本：

```sh
for dir in skills/mediastorm-*; do
  diff -qr "$dir" "$HOME/.codex/skills/$(basename "$dir")"
done
```

课程缓存需要复核时：

```sh
python3 scripts/course_audit.py inventory
cheese/.analysis/.venv/bin/python scripts/compare_dialogue.py --limit 0
cheese/.analysis/.venv/bin/python scripts/course_audit.py sheets 01 --interval 20
cheese/.analysis/.venv/bin/python scripts/course_audit.py transcribe 01
```

`inventory` 会复算源哈希并保留 review；`sheets` / `transcribe` 在匹配缓存时复用，不会自动提升已读状态。

## 12. Git 与收尾状态

生成本文前工作区干净，最近 5 个提交：

| 提交 | 内容 |
| --- | --- |
| `eec5a7c` | `refactor(skills): 恢复 mediastorm 前缀命名` |
| `d2e1fae` | `feat(skills): 新增影视飓风剪映组合 Skill 草稿` |
| `a14fc25` | `docs(handoff): 保存当前上下文与接手说明` |
| `01dd5d2` | `docs(course): 补充音画证据与接口方案评估` |
| `1979ed4` | `docs(course): 建立全课程研读计划与首轮笔记` |

本文这次更新会在提交后进入 `docs(handoff)` 记录；实际哈希以 `git log` 为准，本文不自引用未来哈希。

状态：

- 没有执行远程推送。
- 没有安排自动后台任务、定时任务或自动上传。
- 没有课程媒体进入 Git 索引，`check_progress.py` 已通过。
- 当前磁盘空间非常紧张，不要在未确认空间前下载模型或生成大量转码副本。
- 交接完成后必须继续保留两项事实：**视频没有完成多模态读取；完整课程音画学习和 Skill 最终视听验收仍未完成。**

## 13. 2026-10-26 细粒度画面解析（本次新增）

用户要求不再停留在“视频无法理解”，而是把视频切细、逐张识图并输出详细文档。本轮已完成：

- 18 课全部按 **2 秒间隔**抽帧，共 **6,656 帧 / 1,658 张 2×2 时间码索引页**（单格 960×540）；索引页逐张查看，界面参数用全分辨率定点抓帧和局部裁剪复核。
- 18 篇分课文档：`notes/visual-analysis/01-*.md` … `18-*.md`，合计约 4,600 行；索引见 `notes/visual-analysis/README.md`。
- 合并全文：`notes/visual-analysis/全课程细粒度画面解析.md`；跨课总览：`notes/visual-analysis/全课程关键发现与差异修正.md`。
- 逐课覆盖台账：`progress/fine-visual-review.md`；账本新增 `fine_visual_samples`，`python3 scripts/check_progress.py --write-summary` 已通过。
- 新增工具：
  - `scripts/fine_frames.py`：2 秒索引页 + 定点抓帧（`--crop x:y:w:h` 已修正为 ffmpeg 的 `w:h:x:y`）。
  - `scripts/update_fine_visual_ledger.py`：把完成的细抽帧写入账本。
  - `scripts/combine_visual_analysis.py`：合并 18 篇分课文档。
- 重要发现：第 06 课 `Drone` 非 `drum`；第 10 课“变亮组/辅轨”纠正 SRT；第 15 课动画面板 0.5s 与口播 0.3s 冲突、时钟指针与 3 点卡片不一致；第 16 课“往上拖变亮”结案；第 17 课 `Seedance`/“文生视频”；第 08 课不含点跟踪标签/数字闪变/计时器，这些在第 12、15 课。
- **边界不变**：2 秒抽样不是连续视频，未听音轨；`continuous_video` 与 `audio_listening` 仍为未完成，Skill 仍是 provisional。下一轮若继续，应优先听辨音乐/音效/语气/声道，并对快速动作、变速、跟踪、动画做连续视频复核。

## 14. 2026-10-26 Skill 回写（本次新增）

已把第二轮画面复核中确认的内容回写到组合 Skill：

- 入口新增 `skills/mediastorm-capcut/references/visual-evidence-2026-10.md`：方法边界、字幕/旧笔记纠偏、课程内部矛盾、跨课归属修正、可复算关键数值。
- 10 个子 Skill 的 reference 补入精确时间码与参数：02/03/16 项目接入、05/12/15/16 结构、04/14/17 口播与多机位、06 声音、09 变速、08/12/15 动效、10/13 合成与跟踪、11/16 调色、17/18 生成、03/07/12/16/18 交付。
- 重要归属修正：第 08 课只讲关键帧/缓动，不含点跟踪标签、数字闪变、计时器；这些在第 12、15 课，平面跟踪在第 13 课。
- 已同步到 `~/.codex/skills/mediastorm-*`：11 个安装副本与源码 `diff -qr` 零差异，全部通过 `quick_validate.py`。
- 所有 Skill 仍保留 `status: provisional-unverified-audiovisual`；本轮只回写静态画面可确认的内容，没有把听辨或连续视频结论写进去。

## 15. 2026-10-26 Remotion 适配与 README 重做

- README 重写为 CapCut + Remotion 双路径：新增 SVG 头图、安装方式、10 个子 Skill 的 TypeScript 工具表、剪辑/调色技巧地图、Star History。
- 新增 `assets/readme-header.svg`（1280×320，时间线/波形/关键帧/色卡主题）。
- 入口新增 `skills/mediastorm-capcut/references/remotion-adapter.md`：官方包映射、代码骨架、不能直接映射的边界。
- 10 个子 Skill 各增加“Remotion / TypeScript 适配”段；安装副本已同步并通过 quick_validate。
- **未创建 Remotion 工程、未运行 Studio、未渲染成片**；该路径是基于官方文档的 API 建议，不是本仓库的已验收产物。
- 项目主路径仍是 CapCut；Remotion 适配不改变现有课程证据边界，也不把 Skill 标为最终版。

## 16. 2026-10-26 Remotion 示例与 Skill 细化

- 新增 `remotion/` 可运行工程：Remotion 4.0.538 + React 19 + TypeScript，合成素材，无课程原片。
- 合成演示 `SkillAtlas`：1920×1080、30fps、720 帧（24 秒），六个场景——标题、10 个 Skill 卡片、时间线与字幕、Log→调色、关键帧/曲线、渲染交付。
- 渲染成片在 `assets/demo/skill-atlas.mp4`（约 5.9MB），海报在 `assets/demo/skill-atlas-poster.jpg`；`remotion/out/` 与 `node_modules/` 被忽略。
- 工程说明与场景表在 `remotion/README.md`；合成素材可由 `remotion/scripts/make-assets.sh` 重新生成。
- 11 个 SKILL.md 已充分细化（合计约 1,080 行）：新增 When to use / Inputs / detailed Workflow / Decision rules / CapCut notes / Remotion Adapter / Failure conditions / Acceptance checklist / Output contract。
- 全部 Skill references 已翻译为英文；证据标签统一为 `[course evidence]`、`[sampled stills]`、`[course narration]`、`[inference]`、`[tool boundary]`、`[pending verification]`。中文 UI 标签只作为界面证据保留并附英文释义。
- 11 个源码 Skill 通过 `quick_validate.py`；安装副本已同步，`diff -qr` 为零。
- 边界：示例视频是 Remotion 实现路径的视觉冒烟测试，不含课程媒体，也没有经过听辨或平台验收；Skill 仍是 provisional。
