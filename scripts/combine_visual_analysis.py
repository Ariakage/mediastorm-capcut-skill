#!/usr/bin/env python3
"""把 notes/visual-analysis/NN-*.md 按课号合并为一份可检索的总文档。

不修改分课文档，只读取并拼接；输出仍是原创归纳与时间码，不含课程视频或字幕全文。
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "notes" / "visual-analysis"
TARGET = SOURCE / "全课程细粒度画面解析.md"


def main() -> None:
    files = sorted(
        (p for p in SOURCE.glob("[0-9][0-9]-*.md") if p.name != TARGET.name),
        key=lambda p: int(p.name[:2]),
    )
    if not files:
        raise SystemExit("没有找到分课解析文档")

    parts = [
        "# 全课程细粒度画面解析（合并版）",
        "",
        "来源：影视飓风（MediaStorm）付费剪映教学课程，个人学习整理，非官方。",
        "",
        "本文件由 `scripts/combine_visual_analysis.py` 从分课文档合并生成，便于全文检索；"
        "分课文档才是维护入口。所有内容为原创归纳与时间码，不含课程视频、截图或完整讲稿。",
        "",
        "证据边界：按 2 秒间隔抽帧并逐张查看画面索引页，界面细节另用全分辨率定点抓帧核对；"
        "不是逐帧解码，也没有音轨听辨。课程演示参数是案例值，不是通用预设。",
        "",
        "## 目录",
        "",
    ]
    for path in files:
        title = path.stem
        anchor = re.sub(r"[^\w一-鿿-]+", "-", title).strip("-").lower()
        parts.append(f"- [{title}](#{anchor})")
    parts.append("")

    for path in files:
        body = path.read_text().strip()
        parts.extend(["---", "", body, ""])

    TARGET.write_text("\n".join(parts))
    print(f"合并 {len(files)} 篇文档 -> {TARGET.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
