#!/usr/bin/env python3
"""Tick tasks in the week READMEs that you already ticked in the tracker.

The tracker's "Repo sync" panel gives you the exact command, for example:
    python scripts/apply_tracker.py x1t5 x1t6 x2t1

Each id is x<week>t<task number>, matching the order of the checkboxes in
that week's README. After ticking, it rebuilds the progress table and
progress.json. Then commit and push.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDER_RE = re.compile(r"^week(\d+)(?:-(\d+))?-")
BOX_RE = re.compile(r"^(\s*[-*] )\[( |x|X)\] ", re.M)
WEEK_HEAD_RE = re.compile(r"^## Week (\d+):", re.M)
ID_RE = re.compile(r"^x(\d+)t(\d+)$")


def folder_for(week: int) -> Path | None:
    for p in ROOT.iterdir():
        m = FOLDER_RE.match(p.name)
        if p.is_dir() and m:
            a, b = int(m.group(1)), int(m.group(2) or m.group(1))
            if a <= week <= b:
                return p
    return None


def tick(path: Path, week: int, task: int) -> str:
    text = path.read_text(encoding="utf-8")
    plan_end = text.find("\n---\n")
    plan_end = len(text) if plan_end < 0 else plan_end
    # Where this week's checkboxes start (multi-week folders have "## Week N:" headings).
    start = 0
    head = next((m for m in WEEK_HEAD_RE.finditer(text) if int(m.group(1)) == week), None)
    if head:
        start = head.end()
        nxt = next((m for m in WEEK_HEAD_RE.finditer(text, head.end())), None)
        plan_end = min(plan_end, nxt.start()) if nxt else plan_end
    boxes = [m for m in BOX_RE.finditer(text, start, plan_end)]
    if task > len(boxes):
        return f"x{week}t{task}: week {week} only has {len(boxes)} tasks, skipped"
    m = boxes[task - 1]
    if m.group(2).lower() == "x":
        return f"x{week}t{task}: already ticked"
    text = text[: m.start()] + m.group(1) + "[x] " + text[m.end():]
    path.write_text(text, encoding="utf-8")
    return f"x{week}t{task}: ticked in {path.parent.name}/README.md"


def main(ids: list[str]) -> None:
    if not ids:
        sys.exit(__doc__)
    for raw in ids:
        m = ID_RE.match(raw.strip().strip(","))
        if not m:
            print(f"{raw}: not a task id like x1t5, skipped")
            continue
        week, task = int(m.group(1)), int(m.group(2))
        folder = folder_for(week)
        if not folder:
            print(f"{raw}: no folder for week {week}, skipped")
            continue
        print(tick(folder / "README.md", week, task))
    subprocess.run([sys.executable, str(ROOT / "scripts" / "update_progress.py")], check=True)


if __name__ == "__main__":
    main(sys.argv[1:])
