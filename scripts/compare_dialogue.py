#!/usr/bin/env python3
"""Compare two machine transcripts locally; disagreement is not an error verdict."""
import argparse
import difflib
import json
import math
import re
from pathlib import Path

from opencc import OpenCC
from course_audit import ROOT, PRIVATE, clock, cues, digest, load, save

CONVERTER=OpenCC("t2s")


def normalized(text):
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", CONVERTER.convert(text).lower())


def compare(row, result, window):
    if result["audit"]["video_sha256"] != row["video_sha256"]:
        raise ValueError(f"ASR/source hash mismatch for {row['id']}")
    provided=cues(ROOT/row["subtitle"])
    recognized=result["segments"]
    windows=[]
    for index in range(math.ceil(row["duration_seconds"]/window)):
        start=index*window
        end=min((index+1)*window,row["duration_seconds"])
        a="".join(c["text"] for c in provided if start <= (c["start"]+c["end"])/2 < end)
        b="".join(c["text"] for c in recognized if start <= (c["start"]+c["end"])/2 < end)
        na,nb=normalized(a),normalized(b)
        similarity=difflib.SequenceMatcher(None,na,nb,autojunk=False).ratio()
        windows.append({"start":start,"end":end,"similarity":round(similarity,4),
                        "provided":a,"asr":b,"has_provided_dialogue":bool(na),"has_asr_dialogue":bool(nb)})
    return {"id":row["id"],"window_seconds":window,"windows":windows,
            "warning":"Two imperfect ASR sources; timing, script variation and music hallucinations can all lower similarity. Not a listening verdict."}


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ids",nargs="*")
    parser.add_argument("--window",type=float,default=30)
    parser.add_argument("--limit",type=int,default=2)
    args=parser.parse_args()
    if args.window<=0 or args.limit<0:parser.error("window must be positive and limit nonnegative")
    selected={f"{int(x):02}" for x in args.ids} if args.ids else None
    ledger=load()
    destination=PRIVATE/"dialogue-comparison"
    destination.mkdir(parents=True,exist_ok=True)
    for row in ledger["lessons"]:
        if selected and row["id"] not in selected:continue
        source=PRIVATE/"asr"/f"{row['id']}.json"
        if not source.is_file():continue
        result=json.loads(source.read_text())
        report=compare(row,result,args.window)
        (destination/f"{row['id']}.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
        suspicious=[w for w in report["windows"] if w["similarity"]<.7 and (w["provided"] or w["asr"])]
        old=row["review"]["audio_dialogue_asr"]
        old.update({"state":"transcribed_full_input", "model":result["audit"]["model"],
                    "segments":len(result["segments"]),"asr_sha256":digest(source),
                    "comparison_windows":len(report["windows"]),"low_similarity_windows":len(suspicious),
                    "comparison":"completed_full_window_comparison; not listening",
                    "automatic_comparison":"completed; not human review", "actual_listening":False})
        print(f"L{row['id']} windows={len(report['windows'])} low-similarity={len(suspicious)}")
        for w in sorted(suspicious,key=lambda w:w["similarity"])[:args.limit]:
            print(f"  [{clock(w['start'])}-{clock(w['end'])}] similarity={w['similarity']}")
            print("  Provided:",w["provided"][:360])
            print("  LocalASR:",w["asr"][:360])
    save(ledger)
