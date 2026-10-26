# 课程学习进度

来源：影视飓风（MediaStorm）付费剪映教学课程；非官方个人学习项目。

共 18 课，约 03:41:55。逐课元数据与实际证据状态见 [course-ledger.json](course-ledger.json)。

## 状态语义

- `subtitles`：助手是否实际读完每一条字幕；不等于听过音轨。
- `visual_samples`：助手实际查看的画面索引页；仅代表标记时间点的静态观察。
- `continuous_video`：连续运动和前后关系的实际复核；抽帧不能自动填入。
- `audio_dialogue_asr`：完整音轨提交本地识别以及转写比对情况；不代表感知音乐和音效。
- `audio_listening`：音轨实际听辨；当前会话的音频输入不支持，保持未完成。
- `notes`：原创学习归纳与来源证据的落盘状态。
- `complete_multimodal_review`：仅当所有所需模态实际复核完成才为 true。

## 阶段记录

### 2026-10-26：范围与读取链路

- 已确认组合 Skill、先课程后分类、有实质成果再本地提交。
- 已将具体执行计划写入 AGENTS.md。
- 图片读取探针成功：第 01 课 00:20，屏幕显示播放页面与课程烧录字幕。
- 音频读取探针失败：工具明确返回当前模型不支持音频输入；不是静音文件或课程缺音轨。
- 用户随后允许安装本地语音识别，用于补充全音轨对白核对；非对白听辨仍未完成。
- 原始素材与所有派生材料统一被 `/cheese/` 忽略。
- 子 Skill 的最终分类尚未确定，不能以课程标题直接宣称已学完。

### 2026-10-26：第一轮字幕研读完成

- 已实际读完 18 课全部 6,198 条字幕，分课原创归纳见 `notes/course-reading-01-07.md` 与 `notes/course-reading-08-18.md`。
- 第 07 课 00:10:38 导出表的 `KB/s` 单位存在歧义，暂不转为命令参数或平台现行要求。
- 已注意到字幕中的 A-roll / B-roll、混合模式、人名、文生视频和模型名等误识别；以画面或后续音轨证据核对，不把误字抄入 Skill。
- 已安装隔离 Python 3.12 / mlx-whisper 环境并启动完整音轨本地识别；Python 3.15 无匹配依赖，未更改系统 Python。
- 画面索引按 20 秒间隔生成，属于静态抽样；只有助手实际打开的页才记为已观察，生成不等于阅读。
- 所有 18 课的完整音画学习状态仍未完成；下一步继续画面观察、细节回查及转写比对。

## 本地分析工具

`scripts/course_audit.py` 用于维护清单、输出无遗漏字幕阅读稿、制作带真实时间戳的抽样画面索引和本地对白转写；输出原文和媒体均只留本地。

```sh
python3 scripts/course_audit.py inventory
python3 scripts/course_audit.py read 01 02
uv venv cheese/.analysis/.venv --python 3.12
uv pip install --python cheese/.analysis/.venv/bin/python -r scripts/course-analysis-requirements.txt
cheese/.analysis/.venv/bin/python scripts/course_audit.py sheets 01 --interval 20
TIKTOKEN_CACHE_DIR="$PWD/cheese/.analysis/tiktoken" cheese/.analysis/.venv/bin/python scripts/course_audit.py transcribe
python3 scripts/check_progress.py
```

本轮 ASR 使用 `mlx-community/whisper-small-mlx`，模型仓库 revision 为 `45f3915923c7a79a5a5b5a7d909d39aeb0e5630e`；所有音频推理在本机执行，模型下载不上传课程。完整处理与内容实际理解的状态分开维护。
