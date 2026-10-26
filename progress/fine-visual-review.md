# 细粒度画面复核台账（2 秒抽帧）

来源：影视飓风（MediaStorm）付费剪映教学课程；个人学习、非官方。
本轮方法：每课按 **2 秒间隔**抽帧，组成带时间码的 2×2 索引页（单格 960×540），逐张查看；界面参数看不清时再用全分辨率定点抓帧裁剪放大。

## 证据边界

- 这是**静态抽样观察**，不是逐帧解码，也不是连续视频输入。
- 没有音轨听辨；音乐、音效、语气、混响、声道仍待完成。
- 索引页 JPEG 是可复现的派生产物，留在被忽略的 `cheese/.analysis/fine/`；账本校验 manifest 哈希与计数。
- 课程演示参数是案例值，不是通用预设。

## 逐课覆盖

| 课号 | 课程 | 时长（秒） | 间隔 | 帧数 | 索引页 | 解析文档 |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| 01 | 剪出和影视飓风一样的视频 | 112 | 2s | 56 | 14 | [01-课程定位与宣传片.md](../notes/visual-analysis/01-课程定位与宣传片.md) |
| 02 | 导学课：如何更好地学习这门课？ | 305 | 2s | 153 | 39 | [02-导学与学习方法.md](../notes/visual-analysis/02-导学与学习方法.md) |
| 03 | 初试成片：10分钟走通专业剪辑全流程 | 697 | 2s | 348 | 87 | [03-初试成片全流程.md](../notes/visual-analysis/03-初试成片全流程.md) |
| 04 | 高效起步：口播精剪与 A╱B-roll 协同 | 959 | 2s | 479 | 120 | [04-口播精剪与ABroll.md](../notes/visual-analysis/04-口播精剪与ABroll.md) |
| 05 | 节奏掌控：混剪视频与蒙太奇逻辑 | 694 | 2s | 347 | 87 | [05-混剪与蒙太奇.md](../notes/visual-analysis/05-混剪与蒙太奇.md) |
| 06 | 听觉塑造：音乐处理与音效设计思维 | 691 | 2s | 345 | 87 | [06-音乐处理与音效设计.md](../notes/visual-analysis/06-音乐处理与音效设计.md) |
| 07 | 最终交付：导出管理与发布规范 | 893 | 2s | 446 | 112 | [07-导出管理与发布.md](../notes/visual-analysis/07-导出管理与发布.md) |
| 08 | 运动控制：关键帧与曲线运动 | 654 | 2s | 327 | 82 | [08-关键帧与曲线运动.md](../notes/visual-analysis/08-关键帧与曲线运动.md) |
| 09 | 动态节奏：曲线变速与素材帧率 | 651 | 2s | 325 | 82 | [09-曲线变速与素材帧率.md](../notes/visual-analysis/09-曲线变速与素材帧率.md) |
| 10 | 空间重组：全能抠像与蒙版合成 | 730 | 2s | 365 | 92 | [10-抠像与蒙版合成.md](../notes/visual-analysis/10-抠像与蒙版合成.md) |
| 11 | 色彩科学：掌握一级调色工具 | 772 | 2s | 386 | 97 | [11-一级调色.md](../notes/visual-analysis/11-一级调色.md) |
| 12 | 飓多多实操：快速复刻综艺包装 | 1123 | 2s | 561 | 141 | [12-飓多多综艺包装.md](../notes/visual-analysis/12-飓多多综艺包装.md) |
| 13 | 影视飓风运镜实操：进阶平面跟踪 | 654 | 2s | 327 | 82 | [13-进阶平面跟踪.md](../notes/visual-analysis/13-进阶平面跟踪.md) |
| 14 | 采访实操：快速上手多机位剪辑 | 525 | 2s | 262 | 66 | [14-多机位采访.md](../notes/visual-analysis/14-多机位采访.md) |
| 15 | 亿点点不一样实操：时钟理论应用 | 1234 | 2s | 617 | 155 | [15-时钟理论实操.md](../notes/visual-analysis/15-时钟理论实操.md) |
| 16 | 样片日记实操：Vlog 的剪辑结构与色彩 | 889 | 2s | 445 | 112 | [16-Vlog结构与色彩.md](../notes/visual-analysis/16-Vlog结构与色彩.md) |
| 17 | DLC：剪映中常用的 AI 工具 | 870 | 2s | 435 | 109 | [17-剪映AI工具.md](../notes/visual-analysis/17-剪映AI工具.md) |
| 18 | DLC2：使用手机剪辑玩转社媒 | 864 | 2s | 432 | 108 | [18-手机剪辑与社媒.md](../notes/visual-analysis/18-手机剪辑与社媒.md) |

合计：18 课、6,656 帧、1,658 张索引页。

## 与既有“20 秒抽样”的关系

账本中的 `visual_samples` 仍指第一轮 20 秒间隔抽样；本轮 2 秒细抽帧单独记在 `fine_visual_samples`，两者不互相替代。`continuous_video` 与 `audio_listening` 仍为 `pending` / `unavailable`，不能因为本轮帧数增加就标为完整音画验收。

## 复现

```bash
cheese/.analysis/.venv/bin/python scripts/fine_frames.py sheets 03 --interval 2 --out cheese/.analysis/fine --clean
cheese/.analysis/.venv/bin/python scripts/fine_frames.py grab 03 05:12.5 --crop 1420:100:500:800 --scale 1600
```
