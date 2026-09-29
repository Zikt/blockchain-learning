#!/usr/bin/env python3
"""Rebuild the progress section of the root README from the week folders.

It reads every weekNN-*/README.md and counts:
  - checkboxes in the plan ("- [ ]" open, "- [x]" done)
  - hours in the "## Time spent" table (second column)
Then it rewrites everything between the PROGRESS markers in README.md, and
writes progress.json with the ticked task ids (x1t1, x1t2, ...) that match the
tracker, so the two can be compared.

Run it locally before committing:   python scripts/update_progress.py
GitHub Actions also runs it on every push (see .github/workflows/progress.yml).
"""

from __future__ import annotations

import datetime as dt
import json
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
WEEK_HEAD_RE = re.compile(r"^## Week (\d+):", re.M)
PROGRESS_JSON = ROOT / "progress.json"
BLOG = ROOT / "blog"
BSTART, BEND = "<!-- BLOG:START -->", "<!-- BLOG:END -->"
FRONT_RE = re.compile(r"^---\n(.*?)\n---", re.S)


def blog_rows() -> list[str]:
    """One table row per post in blog/, newest first."""
    posts = []
    for f in sorted(BLOG.glob("*.md")) if BLOG.exists() else []:
        if f.name.startswith("_") or f.name in ("README.md", "VIDEO_GUIDE.md"):
            continue
        meta = {}
        m = FRONT_RE.match(f.read_text(encoding="utf-8"))
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.split("#")[0].strip().strip('"')
        video = f"[Watch]({meta['video']})" if meta.get("video") else "–"
        posts.append((meta.get("date", ""), f"| {meta.get('date', '')} | [{meta.get('title', f.stem)}](blog/{f.name}) "
                      f"| {meta.get('weeks', '')} | {video} |"))
    return [row for _, row in sorted(posts, reverse=True)]


NSTART, NEND = "<!-- NAV:START -->", "<!-- NAV:END -->"


def label(folder: str) -> str:
    m = FOLDER_RE.match(folder)
    a, b = int(m.group(1)), m.group(2)
    return f"Weeks {a}–{int(b)}" if b else f"Week {a:02d}"


def add_nav(folders: list[str]) -> int:
    """Keep a navigation line at the top of every week README: overview, previous, next."""
    changed = 0
    for i, f in enumerate(folders):
        path = ROOT / f / "README.md"
        if not path.exists():
            continue
        parts = ["[↑ Overview](../README.md)"]
        if i > 0:
            parts.append(f"[← {label(folders[i - 1])}](../{folders[i - 1]}/)")
        if i + 1 < len(folders):
            parts.append(f"[{label(folders[i + 1])} →](../{folders[i + 1]}/)")
        nav = f"{NSTART}\n{' · '.join(parts)}\n{NEND}\n\n"
        text = path.read_text(encoding="utf-8")
        if NSTART in text:
            new = re.sub(re.escape(NSTART) + r".*?" + re.escape(NEND) + r"\n*", nav, text, count=1, flags=re.S)
        else:
            new = nav + text
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    return changed


def replace_between(text: str, start: str, end: str, block: str) -> str:
    if start in text and end in text:
        before, rest = text.split(start, 1)
        return before + block + rest.split(end, 1)[1]
    return text


def task_ids(folder: str, plan: str) -> list[tuple[str, bool]]:
    """Map each plan checkbox to its tracker id, e.g. ('x1t5', True)."""
    first = int(FOLDER_RE.match(folder).group(1))
    parts = WEEK_HEAD_RE.split(plan)
    if len(parts) == 1:
        sections = [(first, plan)]
    else:  # multi-week folder: "## Week 10: ...", "## Week 11: ..."
        sections = [(int(parts[i]), parts[i + 1]) for i in range(1, len(parts), 2)]
    out = []
    for week, body in sections:
        for k, mark in enumerate(CHECK_RE.findall(body), start=1):
            out.append((f"x{week}t{k}", mark.lower() == "x"))
    return out


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
    checked_ids, hours_by_folder = [], {}
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
        checked_ids += [tid for tid, ok in task_ids(folder.name, plan) if ok]
        hours_by_folder[folder.name] = hours
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

    state = {"checked": checked_ids, "hours": hours_by_folder, "total_tasks": all_total}
    old = json.loads(PROGRESS_JSON.read_text()) if PROGRESS_JSON.exists() else None
    if old is None or {k: old.get(k) for k in state} != state:
        PROGRESS_JSON.write_text(json.dumps({**state, "updated": today}, indent=1) + "\n")

    readme = README.read_text(encoding="utf-8")
    if START in readme and END in readme:
        before, rest = readme.split(START, 1)
        after = rest.split(END, 1)[1]
        new = before + block + after
    else:
        new = readme.rstrip() + "\n\n## Progress\n\n" + block + "\n"

    week_folders = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and FOLDER_RE.match(p.name))
    navs = add_nav(week_folders)
    if navs:
        print(f"Navigation updated in {navs} week README(s)")

    rows_b = blog_rows()
    blog_block = "\n".join([BSTART, "| Date | Post | Weeks | Video |", "|------|------|-------|-------|", *rows_b, BEND]) if rows_b \
        else "\n".join([BSTART, "_No posts yet. The first explainer is due in week 2._", BEND])
    new = replace_between(new, BSTART, BEND, blog_block)
    if BLOG.exists():
        idx = "[↑ Overview](../README.md)\n\n# Writing and videos\n\nExplainers about what I'm learning, newest first. Start a new post by copying `_template.md`.\n\n" + \
              blog_block.replace("](blog/", "](")
        idx_path = BLOG / "README.md"
        if not idx_path.exists() or idx_path.read_text(encoding="utf-8") != idx + "\n":
            idx_path.write_text(idx + "\n", encoding="utf-8")

    # Don't rewrite the file if only the date changed.
    strip = lambda s: re.sub(r"updated \d{4}-\d{2}-\d{2}", "", s)
    if strip(new) != strip(readme):
        README.write_text(new, encoding="utf-8")
        print(f"README updated: {all_done}/{all_total} tasks, {all_hours:g} h")
    else:
        print("README already up to date")


if __name__ == "__main__":
    main()
