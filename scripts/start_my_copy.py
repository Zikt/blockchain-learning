#!/usr/bin/env python3
"""Turn a copy of this course repo into YOUR learning repo. Run once, from the repo root.

    python scripts/start_my_copy.py --name "Ada Obi" --start 2027-01-04            # preview
    python scripts/start_my_copy.py --name "Ada Obi" --start 2027-01-04 --apply    # do it

What it does:
  1. Points every link at your GitHub account and repo (read from `git remote`, or --user / --repo),
     and puts your name in the README intro, with credit to the original course.
  2. Re-dates the whole plan from your start date (moved to that week's Monday): week READMEs,
     PLAN.md, OUTPUTS.md, curriculum/tasks.json and the tracker's default start date.
  3. Resets progress to zero: unticks every task, clears the "What I built / learned" sections
     and time tables, the learning log, output links and blog posts.
  4. Moves the original author's code and capstone work into reference/ (so you can peek, or
     delete it) and restores the starter files from scripts/starter/.
  5. Clears the author's answers to the flashcard key questions, so you write your own
     (keep them with --keep-answers).

Later, to re-plan without touching progress (fell behind, took a break):
    python scripts/start_my_copy.py --start 2027-03-01 --dates-only --apply
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STARTER = ROOT / "scripts" / "starter"
ORIGINAL_REPO = "https://github.com/Zikt/blockchain-learning"
ORIGINAL_AUTHOR = "Isaac Thani Moses"
ORIGINAL_SITE = "zikt.github.io/blockchain-learning"
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
WEEK_RE = re.compile(r"^week(\d+)(?:-(\d+))?-")
KEEP_BLOG = {"README.md", "VIDEO_GUIDE.md", "_template.md"}
# Where the author's own work accumulates. Anything here that isn't a starter file moves to reference/.
WORK_DIRS = ["trust-stack/src", "trust-stack/test", "trust-stack/script", "trust-stack/app/site",
             "trust-stack/deployments", "trust-stack/firmware", "trust-stack/broadcast"]
SECTIONS_TEMPLATE = """## What I built

<!-- One paragraph, plus a screenshot or terminal output if it helps. -->

## How to run it

```bash
# commands here
```

## What I learned

- 

## What broke, and how I fixed it

- 

## Time spent

| Date | Hours | What |
|------|-------|------|
|      |       |      |
"""


class Plan:
    """Collects changes, then prints them (preview) or writes them (--apply)."""

    def __init__(self, apply: bool):
        self.apply, self.log = apply, []

    def write(self, path: Path, text: str, why: str):
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old == text:
            return
        self.log.append(f"edit   {path.relative_to(ROOT)}  ({why})")
        if self.apply:
            path.write_text(text, encoding="utf-8")

    def move(self, src: Path, dst: Path, why: str):
        self.log.append(f"move   {src.relative_to(ROOT)} → {dst.relative_to(ROOT)}  ({why})")
        if self.apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))

    def copy(self, src: Path, dst: Path, why: str):
        self.log.append(f"copy   {src.relative_to(ROOT)} → {dst.relative_to(ROOT)}  ({why})")
        if self.apply:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)

    def delete(self, path: Path, why: str):
        self.log.append(f"delete {path.relative_to(ROOT)}  ({why})")
        if self.apply:
            path.unlink()


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def git_remote() -> tuple[str, str]:
    try:
        url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        return "", ""
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?$", url)
    return (m.group(1), m.group(2)) if m else ("", "")


def week_folders() -> list[tuple[int, int, Path]]:
    out = []
    for p in sorted(ROOT.iterdir()):
        m = WEEK_RE.match(p.name)
        if p.is_dir() and m:
            a = int(m.group(1))
            out.append((a, int(m.group(2) or a), p))
    return out


def fmt(d: date) -> str:
    return f"{d.day} {MONTHS[d.month - 1]}"


# ---------- 1. Links and name ----------
def relink(plan: Plan, user: str, repo: str, name: str):
    site = f"{user.lower()}.github.io/{repo}"
    gh = f"github.com/{user}/{repo}"
    files = [ROOT / "README.md", ROOT / "DEMO.md", ROOT / "tracker" / "index.html", ROOT / "trust-stack" / "app" / "README.md"]
    files += sorted((ROOT / "cards").glob("*.md"))
    for f in files:
        if not f.exists():
            continue
        t = read(f)
        n = t.replace("YOUR-GITHUB-USERNAME", user).replace(ORIGINAL_SITE, site)
        n = re.sub(r"github\.com/Zikt/blockchain-learning(?=[/)\s\"'#?]|$)", gh, n)
        if repo != "blockchain-learning":
            u = re.escape(user)
            n = re.sub(rf"(?i)((?:github\.com|codespaces\.new)/{u}|{u}\.github\.io)/blockchain-learning\b", rf"\1/{repo}", n)
        plan.write(f, n, "links point at your repo and site")
    readme = ROOT / "README.md"
    if readme.exists() and name:
        t = read(readme)
        intro = (f"I'm {name}. This repo is my own run through [Genesis to Capstone]({ORIGINAL_REPO}), a 12-week course by "
                 f"{ORIGINAL_AUTHOR} that learns blockchain and the cryptography behind it from first principles, with running "
                 "threads on AI and real-world applications. Everything is built in the open: code, tests, notes and explainers. "
                 "It ends in a working **trust stack** that follows a batch of produce from farm to buyer, with proof at every step.")
        n = re.sub(r"^I'm Isaac Thani[^\n]*$", intro, t, count=1, flags=re.M)
        if n == t and ORIGINAL_REPO not in t:
            print("Note: couldn't find the author's intro line in README.md. Edit the intro yourself and credit the original course.")
        plan.write(readme, n, "your name in the intro, with credit to the original course")
    book = ROOT / "book" / "book.toml"
    if book.exists() and name:
        plan.write(book, re.sub(r'authors = \[.*\]', f'authors = ["{name}"]', read(book)), "you as the book's author")


# ---------- 2. Dates ----------
def current_start() -> date:
    t = read(ROOT / "tracker" / "index.html")
    m = re.search(r'const DEFAULT_START = "(\d{4}-\d{2}-\d{2})"', t)
    return date.fromisoformat(m.group(1)) if m else date(2026, 9, 28)


def shift_text(text: str, old: date, delta: int) -> str:
    """Shift 'Tue 29 Sep', '28 Sep' style dates (no year) and ISO dates by delta days."""
    def infer(day: int, mon: int) -> date:
        cands = [date(y, mon, day) for y in (old.year - 1, old.year, old.year + 1) if _valid(y, mon, day)]
        return min(cands, key=lambda d: abs((d - (old + timedelta(days=60))).days))
    def dow(m):
        d = infer(int(m.group(2)), MONTHS.index(m.group(3)) + 1) + timedelta(days=delta)
        return f"{DAYS[d.weekday()]} {d.day} {MONTHS[d.month - 1]}"
    def bare(m):
        d = infer(int(m.group(1)), MONTHS.index(m.group(2)) + 1) + timedelta(days=delta)
        return f"{d.day} {MONTHS[d.month - 1]}"
    mon = "|".join(MONTHS)
    text = re.sub(rf"\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (\d{{1,2}}) ({mon})\b", dow, text)
    text = re.sub(rf"(?<![A-Za-z] )(?<!\d )\b(\d{{1,2}}) ({mon})\b(?! \d{{4}})", bare, text)
    return text


def _valid(y, m, d):
    try:
        date(y, m, d)
        return True
    except ValueError:
        return False


def redate(plan: Plan, start: date):
    old = current_start()
    delta = (start - old).days
    end = start + timedelta(days=12 * 7 - 1)
    ship = start + timedelta(days=11 * 7 - 1)
    # Week READMEs: regenerate each "**Dates:**" line from the block number.
    for a, b, folder in week_folders():
        f = folder / "README.md"
        if not f.exists():
            continue
        blocks = iter(range(a, b + 1))
        def repl(m):
            n = next(blocks, b)
            s = start + timedelta(days=(n - 1) * 7)
            e = s + timedelta(days=6)
            return f"**Dates:** {fmt(s)} – {fmt(e)} {e.year}"
        plan.write(f, re.sub(r"\*\*Dates:\*\*\s*\d{1,2} \w{3} – \d{1,2} \w{3} \d{4}", repl, read(f)), "dates from your start")
    # PLAN.md and OUTPUTS.md: shift every date, and rewrite the intro sentence.
    for name in ("PLAN.md", "OUTPUTS.md"):
        f = ROOT / name
        if not f.exists() or delta == 0:
            continue
        t = shift_text(read(f), old, delta)
        t = re.sub(r"starting Monday \d{1,2} \w+ \d{4}\. The capstone ships Sunday \d{1,2} \w+ and the plan ends Sunday \d{1,2} \w+\.",
                   f"starting Monday {start.day} {start.strftime('%B')} {start.year}. The capstone ships Sunday {ship.day} {ship.strftime('%B')} "
                   f"and the plan ends Sunday {end.day} {end.strftime('%B')}.", t)
        plan.write(f, t, "dates from your start")
    # curriculum/tasks.json: ISO dates.
    f = ROOT / "curriculum" / "tasks.json"
    if f.exists() and delta:
        t = re.sub(r"\b(\d{4}-\d{2}-\d{2})\b", lambda m: (date.fromisoformat(m.group(1)) + timedelta(days=delta)).isoformat(), read(f))
        plan.write(f, t, "dates from your start")
    # Tracker default start.
    f = ROOT / "tracker" / "index.html"
    plan.write(f, re.sub(r'const DEFAULT_START = "\d{4}-\d{2}-\d{2}"', f'const DEFAULT_START = "{start.isoformat()}"', read(f)), "tracker starts on your date")
    return ship, end


# ---------- 3. Progress ----------
def reset_progress(plan: Plan, start: date, keep_answers: bool):
    for a, b, folder in week_folders():
        f = folder / "README.md"
        if not f.exists():
            continue
        t = read(f)
        cut = t.find("\n---\n")
        head, tail = (t, "") if cut < 0 else (t[:cut], t[cut:])
        head = re.sub(r"^(\s*[-*] )\[[xX]\] ", r"\1[ ] ", head, flags=re.M)
        i = tail.find("## What I built")
        if i >= 0:
            tail = tail[:i] + SECTIONS_TEMPLATE
        plan.write(f, head + tail, "untick tasks, empty the write-up and time table")
    log = ROOT / "LEARNING_LOG.md"
    if log.exists():
        t = read(log)
        i = t.find("\n---\n")
        if i >= 0:
            t = t[: i + 5] + f"\n## {start.isoformat()} · Week 01 · 0h\n**Did:** Set up my copy of the course.\n**Learned:** \n**Stuck on / next:** Watch the 3Blue1Brown bitcoin video and start pow_demo.py.\n"
            plan.write(log, t, "fresh learning log")
    out = ROOT / "OUTPUTS.md"
    if out.exists():
        lines = []
        for ln in read(out).splitlines():
            cells = ln.split("|")
            if ln.startswith("| ") and len(cells) == 7 and not set(cells[1].strip()) <= set("-") and cells[1].strip() != "Block":
                cells[5] = " "
                ln = "|".join(cells)
            lines.append(ln)
        plan.write(out, "\n".join(lines) + "\n", "clear the author's output links")
    blog = ROOT / "blog"
    if blog.exists():
        for p in sorted(blog.iterdir()):
            if p.is_file() and p.suffix == ".md" and p.name not in KEEP_BLOG:
                plan.move(p, ROOT / "reference" / "blog" / p.name, "the author's post")
    if not keep_answers:
        for f in sorted((ROOT / "cards").glob("block*.md")):
            t = read(f)
            n = re.sub(r"^Answer:[^\n]*\n.*?(?=^### |^## |\Z)", "Answer:\n\n", t, flags=re.M | re.S)
            plan.write(f, n, "clear the author's flashcard answers, so you write your own")


def move_author_work(plan: Plan):
    starter = {p.relative_to(STARTER).as_posix() for p in STARTER.rglob("*") if p.is_file()} if STARTER.exists() else set()
    candidates = []
    for _, _, folder in week_folders():
        candidates += [p for p in folder.rglob("*") if p.is_file() and p.name != "README.md"]
    for d in WORK_DIRS:
        base = ROOT / d
        if base.exists():
            candidates += [p for p in base.rglob("*") if p.is_file() and not p.name.endswith("README.md")]
    moved = set()
    for p in sorted(set(candidates)):
        rel = p.relative_to(ROOT).as_posix()
        if "/lib/" in f"/{rel}" or "/cache/" in f"/{rel}" or "/out/" in f"/{rel}":
            continue
        s = STARTER / rel
        if s.exists() and s.read_bytes() == p.read_bytes():
            continue
        plan.move(p, ROOT / "reference" / rel, "the author's work")
        moved.add(rel)
    for rel in sorted(starter):
        if rel in moved or not (ROOT / rel).exists():
            plan.copy(STARTER / rel, ROOT / rel, "starter file")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--start", required=True, help="your start date, YYYY-MM-DD (moved to that week's Monday)")
    ap.add_argument("--name", default="", help='your name for the README intro, e.g. "Ada Obi"')
    ap.add_argument("--user", default="", help="your GitHub username (default: from git remote)")
    ap.add_argument("--repo", default="", help="your repo name (default: from git remote)")
    ap.add_argument("--keep-answers", action="store_true", help="keep the author's flashcard answers")
    ap.add_argument("--dates-only", action="store_true", help="only re-date the plan; leave progress alone")
    ap.add_argument("--apply", action="store_true", help="make the changes (without it, you get a preview)")
    a = ap.parse_args()

    start = date.fromisoformat(a.start)
    if start.weekday():
        monday = start - timedelta(days=start.weekday())
        print(f"Blocks run Monday to Sunday, so your start moves to Monday {monday.isoformat()}.")
        start = monday
    plan = Plan(a.apply)
    ship, end = redate(plan, start)
    if not a.dates_only:
        user, repo = git_remote()
        user, repo = a.user or user, a.repo or repo or "blockchain-learning"
        if not user:
            sys.exit("Couldn't read your GitHub username from `git remote`. Pass --user <your-username>.")
        if user.lower() == "zikt" and repo == "blockchain-learning":
            sys.exit("This is the original course repo. Run this in your own copy (Use this template → your account).")
        if not a.name:
            print('Tip: add --name "Your Name" to put your name in the README intro.')
        relink(plan, user, repo, a.name)
        reset_progress(plan, start, a.keep_answers)
        move_author_work(plan)

    print("\n".join(plan.log) if plan.log else "Nothing to change.")
    print(f"\nPlan: {start.isoformat()} to {end.isoformat()}; the capstone ships {ship.isoformat()}.")
    if not a.apply:
        print("\nThis was a preview. Run the same command with --apply to make these changes.")
        return
    subprocess.run([sys.executable, str(ROOT / "scripts" / "update_progress.py")], check=False)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py"), "--check"], check=False)
    if not a.dates_only:
        print(f"""
Done. Next:
  1. git add -A && git commit -m "Start my copy of the course" && git push
  2. On GitHub: Settings → Pages → Source: GitHub Actions. Then Actions → Site → Run workflow.
     Your site: https://{(a.user or git_remote()[0]).lower()}.github.io/{a.repo or git_remote()[1] or 'blockchain-learning'}/
  3. Open the tracker on your site, check the start date, and follow FOLLOW_ALONG.md from step 4.""")


if __name__ == "__main__":
    main()
