#!/usr/bin/env python3
"""Rebuild the progress section of the root README from the week folders.

It reads every weekNN-*/README.md and counts:
  - checkboxes in the plan ("- [ ]" open, "- [x]" done)
  - hours in the "## Time spent" table (second column)
Then it rewrites everything between the PROGRESS markers in README.md.

Run it locally before committing:   python scripts/update_progress.py
GitHub Actions also runs it on every push (see .github/workflows/progress.yml).
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
START, END = "<!-- PROGRESS:START -->", "<!-- PROGRESS:END -->"
BAR_WIDTH = 10

CHECK_RE = re.compile(r"^\s*[-*] \[( |x|X)\] ", re.M)
DATES_RE = re.compile(r"\*\*Dates:\*\*\s*([^·\n]+)")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.M)
FOLDER_RE = re.compile(r"^week(\d+)(?:-(\d+))?-")


def week_label(folder: str) -> str:
    m = FOLDER_RE.match(folder)
    a, b = int(m.group(1)), m.group(2)
    return f"{a}–{int(b)}" if b else str(a)


def hours_logged(text: str) -> float:
    """Sum the Hours column of the '## Time spent' table."""
    if "## Time spent" not in text:
        return 0.0
    table = text.split("## Time spent", 1)[1]
    total = 0.0
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2:
            try:
                total += float(cells[1].replace("h", "").replace(",", "."))
            except ValueError:
                pass
    return total


def bar(done: int, total: int) -> str:
    filled = round(BAR_WIDTH * done / total) if total else 0
    return "█" * filled + "░" * (BAR_WIDTH - filled)


def status(done: int, total: int) -> str:
    if total and done == total:
        return "✅ Done"
    return "🔨 In progress" if done else "Not started"


def main() -> None:
    rows, all_done, all_total, all_hours = [], 0, 0, 0.0
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and FOLDER_RE.match(p.name)):
        readme = folder / "README.md"
        if not readme.exists():
            continue
        text = readme.read_text(encoding="utf-8")
        plan = text.split("\n---\n", 1)[0]  # only count checkboxes in the plan section
        marks = CHECK_RE.findall(plan)
        done = sum(1 for m in marks if m.lower() == "x")
        total = len(marks)
        hours = hours_logged(text)
        title = TITLE_RE.search(text).group(1).split(":", 1)[-1].strip()
        dates = DATES_RE.findall(text)
        span = dates[0].split("–")[0].strip() + " – " + dates[-1].split("–")[-1].strip() if dates else ""
        pct = f"{round(100 * done / total)}%" if total else "–"
        rows.append(
            f"| {week_label(folder.name)} | {span} | [{title}]({folder.name}/) "
            f"| `{bar(done, total)}` {done}/{total} ({pct}) | {hours:g} h | {status(done, total)} |"
        )
        all_done, all_total, all_hours = all_done + done, all_total + total, all_hours + hours

    overall = round(100 * all_done / all_total) if all_total else 0
    today = dt.date.today().isoformat()
    block = "\n".join([
        START,
        f"**Overall:** `{bar(all_done, all_total)}` {all_done}/{all_total} tasks ({overall}%) · "
        f"{all_hours:g} h logged · updated {today}",
        "",
        "| Week | Dates | Project | Progress | Time | Status |",
        "|------|-------|---------|----------|------|--------|",
        *rows,
        END,
    ])

    readme = README.read_text(encoding="utf-8")
    if START in readme and END in readme:
        before, rest = readme.split(START, 1)
        after = rest.split(END, 1)[1]
        new = before + block + after
    else:
        new = readme.rstrip() + "\n\n## Progress\n\n" + block + "\n"

    # Don't rewrite the file if only the date changed.
    strip = lambda s: re.sub(r"updated \d{4}-\d{2}-\d{2}", "", s)
    if strip(new) != strip(readme):
        README.write_text(new, encoding="utf-8")
        print(f"README updated: {all_done}/{all_total} tasks, {all_hours:g} h")
    else:
        print("README already up to date")


if __name__ == "__main__":
    main()
