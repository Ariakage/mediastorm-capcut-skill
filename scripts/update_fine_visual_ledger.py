#!/usr/bin/env python3
"""把已完成的 2 秒细抽帧解析写入课程账本的 fine_visual_samples 字段。

只登记同时满足以下条件的课程：
- `cheese/.analysis/fine/<课号>/manifest.json` 存在；
- 对应分课解析文档存在且不是空壳；
- manifest 的视频哈希与账本源哈希一致。

索引页 JPEG 是可复现的派生产物，账本只校验 manifest 哈希与计数，不要求图片长期保留。
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "progress" / "course-ledger.json"
FINE = ROOT / "cheese" / ".analysis" / "fine"
DOCS = ROOT / "notes" / "visual-analysis"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    data = json.loads(LEDGER.read_text())
    updated = 0
    skipped = []
    for row in data["lessons"]:
        lesson_id = row["id"]
        manifest_path = FINE / lesson_id / "manifest.json"
        doc_candidates = sorted(DOCS.glob(f"{lesson_id}-*.md"))
        doc = doc_candidates[0] if doc_candidates else None
        if not manifest_path.is_file() or doc is None:
            skipped.append(f"{lesson_id}: manifest/doc missing")
            continue
        text = doc.read_text()
        if len(text) < 2500 or "索引页" not in text:
            skipped.append(f"{lesson_id}: document too thin or lacks coverage note")
            continue
        manifest = json.loads(manifest_path.read_text())
        if manifest.get("video_sha256") != row["video_sha256"]:
            skipped.append(f"{lesson_id}: source hash mismatch")
            continue
        row["review"]["fine_visual_samples"] = {
            "state": "reviewed_fine_sheets",
            "mode": "sampled_stills",
            "method": "2s interval 2x2 sheets; targeted full-resolution grabs for UI parameters",
            "interval_seconds": manifest["interval_seconds"],
            "reviewed_sheet_count": len(manifest["sheets"]),
            "reviewed_frame_count": manifest["frame_count"],
            "manifest_sha256": digest(manifest_path),
            "document": str(doc.relative_to(ROOT)),
        }
        updated += 1
    LEDGER.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    print(f"更新 {updated} 课")
    for item in skipped:
        print("跳过", item)


if __name__ == "__main__":
    main()
