#!/usr/bin/env python3
"""Build the GitHub Pages site: landing page, tracker, flashcards and demo.

    python scripts/build_site.py            # everything, into dist/site/
    python scripts/build_site.py --check    # only check the card files (fast, no output)
    python scripts/build_site.py --no-anki  # skip the Anki deck (no genanki needed)

Then open dist/site/cards/index.html in a browser to try the flashcards locally.

It reads cards/block*.md (format in cards/README.md), checks every card, and writes:
  dist/site/index.html                      landing page (from site/index.html)
  dist/site/tracker/index.html              the progress tracker (from tracker/)
  dist/site/cards/                          the flashcard app + cards.js + cards.json
  dist/site/cards/genesis-to-capstone.apkg  the Anki deck (needs: pip install genanki)
  dist/site/demo/                           trust-stack/app/site/ once it exists, else a placeholder
GitHub Actions runs this on every push (.github/workflows/pages.yml) and publishes dist/site/.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
OUT = ROOT / "dist" / "site"
DECK = "Genesis to Capstone"

SECTION_TYPES = [("before you start", "pre"), ("key questions", "key"), ("final quiz", "post"), ("reflect", "reflect")]
CARD_RE = re.compile(r"^###\s+([a-z0-9][a-z0-9-]*)\s*(?:·\s*([a-z0-9-]+))?\s*$")
OPT_RE = re.compile(r"^[-*]\s+([A-F])[.)]\s+(.+)$")


class CardError(Exception):
    pass


def parse_front(text: str, path: Path) -> tuple[dict, list[str], int]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise CardError(f"{path.name}:1: file must start with a --- front-matter block")
    meta, i = {}, 1
    while i < len(lines) and lines[i].strip() != "---":
        if ":" in lines[i]:
            k, v = lines[i].split(":", 1)
            meta[k.strip()] = v.strip()
        i += 1
    if i >= len(lines):
        raise CardError(f"{path.name}: front matter is never closed with ---")
    for k in ("block", "title"):
        if k not in meta:
            raise CardError(f"{path.name}: front matter needs '{k}:'")
    meta["block"] = int(meta["block"])
    meta["topics"] = [t.strip() for t in meta.get("topics", "").split(",") if t.strip()]
    return meta, lines, i + 1


def parse_file(path: Path) -> tuple[dict, list[dict]]:
    meta, lines, i = parse_front(path.read_text(encoding="utf-8"), path)
    intro, cards, section, cur = [], [], None, None

    def finish(c):
        if not c:
            return
        body = c.pop("_body")
        q, opts, fields, ans_lines, mode = [], [], {}, [], "q"
        for ln, raw in body:
            s = raw.strip()
            if re.match(r"^</?details>|^<summary>", s):
                continue
            m = OPT_RE.match(s)
            if c["type"] in ("pre", "post") and m and mode in ("q", "opts"):
                opts.append((m.group(1), m.group(2).strip()))
                mode = "opts"
                continue
            fm = re.match(r"^(answer|why|source)\s*:\s*(.*)$", s, re.I)
            if fm and c["type"] in ("pre", "post"):
                fields[fm.group(1).lower()] = fm.group(2).strip()
                mode = fm.group(1).lower()
                continue
            if c["type"] in ("pre", "post") and mode in ("why", "source") and s:
                fields[mode] += " " + s
                continue
            if c["type"] == "key":
                am = re.match(r"^\*{0,2}answer\s*:\*{0,2}\s*(.*)$", s, re.I)
                sm = re.match(r"^source\s*:\s*(.*)$", s, re.I)
                if am and mode == "q":
                    mode = "a"
                    if am.group(1):
                        ans_lines.append(am.group(1))
                    continue
                if sm and mode == "a":
                    fields["source"] = sm.group(1).strip()
                    continue
                if mode == "a":
                    ans_lines.append(raw.rstrip())
                    continue
            if mode == "q":
                q.append(raw.rstrip())
        c["q"] = "\n".join(q).strip()
        if not c["q"]:
            raise CardError(f"{path.name}:{c['line']}: card {c['id']} has no question text")
        if c["type"] in ("pre", "post"):
            if len(opts) < 2:
                raise CardError(f"{path.name}:{c['line']}: quiz card {c['id']} needs at least 2 options like '- A. ...'")
            letters = [o[0] for o in opts]
            a = fields.get("answer", "").strip().upper()[:1]
            if a not in letters:
                raise CardError(f"{path.name}:{c['line']}: quiz card {c['id']} needs 'answer: <letter>' matching one of {''.join(letters)}")
            c["options"] = [o[1] for o in opts]
            c["correct"] = letters.index(a)
            c["why"] = fields.get("why", "")
        elif c["type"] == "key":
            c["answer"] = "\n".join(ans_lines).strip()
        if fields.get("source"):
            c["source"] = fields["source"]
        cards.append(c)

    for n in range(i, len(lines)):
        raw = lines[n]
        s = raw.strip()
        if s.startswith("## "):
            finish(cur)
            cur = None
            name = s[3:].strip().lower()
            section = next((t for k, t in SECTION_TYPES if name.startswith(k)), None)
            if section is None:
                raise CardError(f"{path.name}:{n + 1}: unknown section '{s[3:]}'. Use: Before you start, Key questions, Final quiz, Reflect")
            continue
        m = CARD_RE.match(s)
        if s.startswith("### "):
            if not m:
                raise CardError(f"{path.name}:{n + 1}: card heading must look like '### b01-key-1 · topic'")
            if section is None:
                raise CardError(f"{path.name}:{n + 1}: card {m.group(1)} is outside a section")
            finish(cur)
            topic = m.group(2) or ("reflect" if section == "reflect" else "general")
            cur = {"id": m.group(1), "block": meta["block"], "type": section, "topic": topic,
                   "file": f"cards/{path.name}", "line": n + 1, "_body": []}
            continue
        if cur is not None:
            cur["_body"].append((n + 1, raw))
        elif section is None and not s.startswith("# "):
            intro.append(raw)
    finish(cur)
    # The block intro is the first paragraph under the title.
    paras = "\n".join(intro).strip().split("\n\n")
    meta["intro"] = paras[0].strip() if paras else ""
    return meta, cards


def load_all() -> tuple[list[dict], list[dict]]:
    files = sorted(CARDS.glob("block*.md"))
    if not files:
        raise CardError("no cards/block*.md files found")
    blocks, cards, seen = [], [], {}
    for f in files:
        meta, cs = parse_file(f)
        for c in cs:
            if c["id"] in seen:
                raise CardError(f"{c['file']}:{c['line']}: duplicate card id {c['id']} (also in {seen[c['id']]})")
            seen[c["id"]] = f"{c['file']}:{c['line']}"
        blocks.append(meta)
        cards.extend(cs)
    blocks.sort(key=lambda b: b["block"])
    return blocks, cards


def repo_slug() -> str:
    if os.environ.get("GITHUB_REPOSITORY"):
        return os.environ["GITHUB_REPOSITORY"]
    try:
        url = subprocess.run(["git", "config", "--get", "remote.origin.url"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        m = re.search(r"github\.com[:/]([^/]+/[^/.]+)", url)
        if m:
            return m.group(1)
    except OSError:
        pass
    return ""


# ---------- Anki ----------
BULLET = re.compile(r"^\s*[-*]\s+")
NUMBER = re.compile(r"^\s*\d+[.)]\s+")


def md_to_html(text: str) -> str:
    out = []
    for para in re.split(r"\n\s*\n", text.strip()):
        lines = para.splitlines()
        if all(re.match(r"^\s*[-*]\s+", l) for l in lines):
            items = "".join("<li>" + inline(BULLET.sub("", l)) + "</li>" for l in lines)
            out.append(f"<ul>{items}</ul>")
        elif all(re.match(r"^\s*\d+[.)]\s+", l) for l in lines):
            items = "".join("<li>" + inline(NUMBER.sub("", l)) + "</li>" for l in lines)
            out.append(f"<ol>{items}</ol>")
        elif para.startswith("```"):
            code = re.sub(r"^```\w*\n?|\n?```$", "", para)
            out.append(f"<pre><code>{html.escape(code)}</code></pre>")
        else:
            out.append("<p>" + "<br>".join(inline(l) for l in lines) + "</p>")
    return "".join(out)


def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    return s


def build_anki(blocks: list[dict], cards: list[dict], path: Path, slug: str) -> int:
    import genanki  # pip install genanki

    css = (".card{font-family:-apple-system,Segoe UI,Roboto,sans-serif;font-size:19px;line-height:1.5;text-align:left;max-width:680px;margin:0 auto;padding:8px}"
           ".meta{font-size:13px;opacity:.65;margin-bottom:10px}.opt{padding:6px 10px;border:1px solid #8884;border-radius:8px;margin:6px 0}"
           ".ok{border-color:#1a8a5a;background:#1a8a5a22;font-weight:600}.why{margin-top:12px;font-size:16px}.src{margin-top:14px;font-size:13px;opacity:.65}"
           "code{font-size:.9em;background:#8882;padding:1px 4px;border-radius:4px}")
    basic = genanki.Model(1760207201, "Genesis to Capstone · key question",
        fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "Meta"}, {"name": "Source"}],
        templates=[{"name": "Card", "qfmt": '<div class="meta">{{Meta}}</div>{{Question}}',
                    "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}<div class="src">{{Source}}</div>'}], css=css)
    quiz = genanki.Model(1760207202, "Genesis to Capstone · quiz question",
        fields=[{"name": "Question"}, {"name": "Options"}, {"name": "OptionsAnswered"}, {"name": "Why"}, {"name": "Meta"}],
        templates=[{"name": "Card", "qfmt": '<div class="meta">{{Meta}}</div>{{Question}}{{Options}}',
                    "afmt": '<div class="meta">{{Meta}}</div>{{Question}}{{OptionsAnswered}}<div class="why">{{Why}}</div>'}], css=css)
    decks, count = {}, 0
    for b in blocks:
        n = b["block"]
        decks[n] = genanki.Deck(2059400000 + n, f"{DECK}::Block {n:02d} · {b['title']}")
    for c in cards:
        if c["type"] == "reflect" or (c["type"] == "key" and not c.get("answer")):
            continue
        n = c["block"]
        kind = {"pre": "Warm-up", "key": "Key question", "post": "Final quiz"}[c["type"]]
        meta = f"Block {n} · {c['topic'].replace('-', ' ')} · {kind}"
        tags = [f"block::{n:02d}", f"topic::{c['topic']}", f"type::{c['type']}"]
        guid = genanki.guid_for("genesis-to-capstone", c["id"])
        if c["type"] == "key":
            src = inline(c["source"]) if c.get("source") else ""
            note = genanki.Note(model=basic, fields=[md_to_html(c["q"]), md_to_html(c["answer"]), meta, src], tags=tags, guid=guid)
        else:
            letters = "ABCDEF"
            opts = "".join(f'<div class="opt">{letters[i]}. {inline(o)}</div>' for i, o in enumerate(c["options"]))
            ans = "".join(f'<div class="opt{" ok" if i == c["correct"] else ""}">{letters[i]}. {inline(o)}</div>' for i, o in enumerate(c["options"]))
            note = genanki.Note(model=quiz, fields=[md_to_html(c["q"]), opts, ans, inline(c.get("why", "")), meta], tags=tags, guid=guid)
        decks[n].add_note(note)
        count += 1
    path.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(list(decks.values())).write_to_file(str(path))
    return count


# ---------- Site ----------
PLACEHOLDER = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trust stack demo</title><style>body{font-family:system-ui,sans-serif;max-width:560px;margin:15vh auto;padding:0 16px;line-height:1.55;color:#1c2530;background:#f4f6f8}
@media (prefers-color-scheme:dark){body{color:#e3e9ef;background:#0e141b}a{color:#86a9ec}}</style></head>
<body><h1>Trust stack demo</h1><p>The live demo site goes up in week 11 of the plan (December 2026). Until then, you can follow the build in the repo and practise with the flashcards.</p>
<p><a href="../">← Back</a></p></body></html>"""


def build_site(blocks, cards, anki: bool) -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "cards").mkdir(parents=True)
    slug = repo_slug()
    shutil.copy(ROOT / "site" / "index.html", OUT / "index.html")
    if (ROOT / "tracker" / "index.html").exists():
        (OUT / "tracker").mkdir()
        shutil.copy(ROOT / "tracker" / "index.html", OUT / "tracker" / "index.html")
    demo = ROOT / "trust-stack" / "app" / "site"
    if (demo / "index.html").exists():
        shutil.copytree(demo, OUT / "demo")
    else:
        (OUT / "demo").mkdir()
        (OUT / "demo" / "index.html").write_text(PLACEHOLDER, encoding="utf-8")
    shutil.copy(ROOT / "site" / "cards" / "index.html", OUT / "cards" / "index.html")
    n_anki = 0
    if anki:
        try:
            n_anki = build_anki(blocks, cards, OUT / "cards" / "genesis-to-capstone.apkg", slug)
        except ImportError:
            print("genanki isn't installed, so no Anki deck this time (pip install genanki)")
            anki = False
    data = {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "repo": slug,
            "anki": bool(anki), "blocks": blocks, "cards": cards}
    (OUT / "cards" / "cards.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "cards" / "cards.js").write_text("window.CARDS = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    if anki:
        print(f"Anki deck: {n_anki} cards → dist/site/cards/genesis-to-capstone.apkg")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="only check the card files")
    ap.add_argument("--no-anki", action="store_true", help="skip the Anki deck")
    args = ap.parse_args()
    try:
        blocks, cards = load_all()
    except CardError as e:
        sys.exit(f"Card error: {e}")
    by = {t: sum(1 for c in cards if c["type"] == t) for t in ("pre", "key", "post", "reflect")}
    answered = sum(1 for c in cards if c["type"] == "key" and c.get("answer"))
    print(f"{len(blocks)} blocks · {by['pre']} warm-up, {by['key']} key ({answered} answered), {by['post']} final quiz, {by['reflect']} reflect")
    if args.check:
        return
    build_site(blocks, cards, anki=not args.no_anki)
    print("Site built in dist/site/. Open dist/site/cards/index.html to try the flashcards.")


if __name__ == "__main__":
    main()
