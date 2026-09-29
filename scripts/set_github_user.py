#!/usr/bin/env python3
"""Fill in your GitHub username in the README and DEMO links.

Usage: python scripts/set_github_user.py your-username
"""
import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit(__doc__)
user = sys.argv[1].strip().lstrip("@")
root = Path(__file__).resolve().parent.parent
for name in ["README.md", "DEMO.md"]:
    p = root / name
    if p.exists():
        text = p.read_text(encoding="utf-8")
        if "YOUR-GITHUB-USERNAME" in text:
            p.write_text(text.replace("YOUR-GITHUB-USERNAME", user), encoding="utf-8")
            print(f"Updated {name}")
