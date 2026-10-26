#!/usr/bin/env python3
"""Check the installed capcut-cli contract without using truncated bare describe.

This read-only helper resolves the CLI, runs --version, parses
`describe --compact`, and verifies a selected set of full command contracts.
It never calls bare `capcut describe`, which was observed to truncate stdout
on capcut-cli 0.31.1.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any

DEFAULT_COMMANDS = [
    "info",
    "diagnose",
    "tracks",
    "segments",
    "materials",
    "speed",
    "keyframe",
    "mask",
    "crop",
    "mix-mode",
    "audio-fade",
    "chroma",
    "matting",
    "add-filter",
    "add-text",
    "text-style",
    "text-anim",
    "image-anim",
    "compile",
    "render",
    "loudness",
    "detect-scenes",
    "detect-silence",
    "detect-retakes",
]

JS_SUFFIXES = {".js", ".mjs", ".cjs"}


def fail(message: str, code: int = 2) -> None:
    print(json.dumps({"ok": False, "error": message}, ensure_ascii=False), file=sys.stderr)
    raise SystemExit(code)


def candidate_cli() -> list[str]:
    configured = os.environ.get("CAPCUT_CLI")
    candidates = [configured] if configured else []
    candidates.extend([shutil.which("capcut"), shutil.which("capcut-cli")])
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            suffix = Path(candidate).suffix.lower()
            if suffix in JS_SUFFIXES:
                node = shutil.which("node")
                if not node:
                    fail("CAPCUT_CLI points to JavaScript, but node was not found")
                return [node, candidate]
            return [candidate]
    fail("capcut or capcut-cli was not found; install it or set CAPCUT_CLI")
    raise AssertionError("unreachable")


def run_json(command: list[str], label: str) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except subprocess.TimeoutExpired:
        fail(f"{label} timed out")
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "unknown error"
        fail(f"{label} failed with exit {proc.returncode}: {detail}")
    try:
        value = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        fail(f"{label} did not return valid JSON: {exc}")
    if not isinstance(value, dict):
        fail(f"{label} returned a non-object JSON payload")
    return value


def run_version(command: list[str]) -> str:
    proc = subprocess.run(
        [*command, "--version"],
        check=False,
        capture_output=True,
        text=True,
        timeout=15,
    )
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "unknown error"
        fail(f"capcut --version failed with exit {proc.returncode}: {detail}")
    return proc.stdout.strip().splitlines()[0] if proc.stdout.strip() else "unknown"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only capcut-cli contract check using compact + selected describe."
    )
    parser.add_argument(
        "--command",
        action="append",
        dest="commands",
        help="Command contract to verify; repeat for multiple commands.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    selected = args.commands or DEFAULT_COMMANDS
    cli = candidate_cli()

    version = run_version(cli)
    compact = run_json([*cli, "describe", "--compact"], "describe --compact")
    describe_args: list[str] = []
    for name in selected:
        describe_args.extend(["--command", name])
    detail = run_json([*cli, "describe", *describe_args], "selected describe")

    compact_commands = compact.get("commands")
    detail_commands = detail.get("commands")
    if not isinstance(compact_commands, list) or not isinstance(detail_commands, list):
        fail("describe output did not contain command arrays")

    compact_names = {item.get("name") for item in compact_commands if isinstance(item, dict)}
    detail_names = {item.get("name") for item in detail_commands if isinstance(item, dict)}
    missing_compact = sorted(set(selected) - compact_names)
    missing_detail = sorted(set(selected) - detail_names)
    schema_version = detail.get("schema_version", compact.get("schema_version"))

    result = {
        "ok": not missing_compact and not missing_detail and schema_version == 2,
        "cli": cli[-1],
        "version": version,
        "schema_version": schema_version,
        "compact_command_count": len(compact_commands),
        "selected_command_count": len(detail_commands),
        "missing_from_compact": missing_compact,
        "missing_from_selected_describe": missing_detail,
        "selected_commands": sorted(str(name) for name in detail_names if name),
        "notes": [
            "Bare `capcut describe` is intentionally not used because truncated output was observed on this machine.",
            "Command-level mutates flags do not capture option-level side effects; inspect the selected contract before writing.",
        ],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["ok"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
