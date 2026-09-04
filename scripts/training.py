#!/usr/bin/env python3
"""Cross-platform progress recorder for the training repository."""

from __future__ import annotations

import argparse
import json
import os
from datetime import date, timedelta
from pathlib import Path
from typing import Any


NONE_VALUES = {"", "无", "none", "null", "n/a", "no"}


def repo_root() -> Path:
    override = os.environ.get("TRAINING_REPO_ROOT")
    return Path(override).resolve() if override else Path(__file__).resolve().parent.parent


def normalize_blocker(value: str) -> str:
    cleaned = value.strip()
    return "" if cleaned.lower() in NONE_VALUES else cleaned


def progress_path(root: Path) -> Path:
    return root / "daily" / "progress.jsonl"


def append_progress(
    root: Path,
    *,
    minutes: int,
    completed: str,
    blocker: str = "",
    self_score: int = -1,
    phase: str = "",
) -> dict[str, Any]:
    if minutes <= 0:
        raise ValueError("minutes 必须大于 0")
    if not completed.strip():
        raise ValueError("completed 不能为空")
    if self_score not in {-1, 0, 1, 2, 3, 4}:
        raise ValueError("self_score 必须是 -1 或 L0–L4 对应的 0–4")

    entry: dict[str, Any] = {
        "date": date.today().isoformat(),
        "minutes": minutes,
        "completed": completed.strip(),
        "blocker": normalize_blocker(blocker),
        "self_score": self_score,
        "phase": phase.upper(),
        "review_7d": (date.today() + timedelta(days=7)).isoformat(),
        "review_21d": (date.today() + timedelta(days=21)).isoformat(),
    }
    path = progress_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(entry, ensure_ascii=False, separators=(",", ":")) + "\n")
    return entry


def read_last_progress(root: Path) -> dict[str, Any] | None:
    path = progress_path(root)
    if not path.exists():
        return None
    lines = [line.strip() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if not lines:
        return None
    value = json.loads(lines[-1])
    if not isinstance(value, dict):
        raise ValueError("最后一条进度记录不是 JSON 对象")
    return value


def next_suggestion(last: dict[str, Any] | None) -> str:
    if last is None:
        return "暂无进度记录：从 daily/current.md 的 A 日闭卷诊断开始。"
    blocker = normalize_blocker(str(last.get("blocker", "")))
    if blocker:
        return f"下一单元：保留当前阶段并拆小阻塞项——{blocker}"
    level = int(last.get("self_score", -1))
    phase = str(last.get("phase", "")).upper()
    if phase == "A" and level >= 1:
        return "下一单元：进入 B 日，先复现失败基线，再开始闭卷实现并补边界测试。"
    if phase == "A":
        return "下一单元：重复 A 日，缩小资料范围，补一个预测—结果微实验。"
    if phase == "" and level >= 2:
        return "下一单元：进入 B 日，先复现失败基线，再开始闭卷实现并补边界测试。"
    if level < 2:
        return "下一单元：保留当前阶段，缩小任务并补一个预测—结果微实验。"
    if phase == "B":
        return "下一单元：进入 C 日，做故障注入、性能/替代方案对照和口头复述。"
    return "本轮可进入下一主题；先把 7 天和 21 天复测写入任务队列。"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    record = subparsers.add_parser("record", help="追加一条真实训练记录")
    record.add_argument("--minutes", required=True, type=int)
    record.add_argument("--completed", required=True)
    record.add_argument("--blocker", default="")
    record.add_argument("--self-score", type=int, default=-1)
    record.add_argument("--phase", choices=("A", "B", "C"), default="")

    subparsers.add_parser("next", help="根据最后一条记录给出下一单元建议")
    subparsers.add_parser("status", help="显示最后一条进度和下一单元建议")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = repo_root()
    if args.command == "record":
        entry = append_progress(
            root,
            minutes=args.minutes,
            completed=args.completed,
            blocker=args.blocker,
            self_score=args.self_score,
            phase=args.phase,
        )
        print(f"已记录：{entry['date']}，{entry['minutes']} 分钟；7 天复测：{entry['review_7d']}")
        return 0

    last = read_last_progress(root)
    if args.command == "status":
        print("最后进度：" + (json.dumps(last, ensure_ascii=False) if last else "无"))
    print(next_suggestion(last))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
