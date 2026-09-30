# Repo update kit (29 Sep 2026)

Copy these into the root of `blockchain-learning/`, then commit:

| File | What it is |
|---|---|
| `PLAN.md` | Every task in all 12 blocks: ID, due date, kind, minutes, resources |
| `OUTPUTS.md` | Your portfolio: one row per post, video, demo and social post, with a link column |
| `curriculum/tasks.json` | The same plan as data. Scripts, the book and other learners can read it |
| `tracker/index.html` | A standalone copy of the tracker. It saves in the browser, so anyone who clones the repo can use it |
| `FOLLOW_ALONG.md` | How someone else takes the course from your repo |
| `book/` | An mdBook skeleton: one chapter per block, each with idea, build, practice and quiz sections |
| `.github/ISSUE_TEMPLATE/week.md` | Optional weekly issue, closed by the week's last commit |

## Also add by hand

1. **New stablecoin tasks.** Add them to your week READMEs in the same checkbox format as the other tasks:
   - `week05-erc20/README.md`: `x5t15` Stablecoins I: how they hold $1
   - `week09-amm-and-capstone-spec/README.md`: `x9t15` Stablecoins II: why they matter · `x9t16` Stablecoin write-up post
   If `scripts/apply_tracker.py` keeps its own list of task IDs, add these three there too, then run it once and check `progress.json` lists them.
2. **README links.** In the root README, link `PLAN.md`, `OUTPUTS.md` and `FOLLOW_ALONG.md`.
3. **Licence.** A common choice for learning material: CC BY 4.0 for text and MIT for code. Pick one before other people start reusing it.
4. **GitHub Pages.** Your Pages site will host the trust-stack demo. To also serve the tracker, publish `tracker/` alongside `trust-stack/app/site/` in the same Pages build (e.g. copy it to `site/tracker/` in the workflow).

`PLAN.md` and `tasks.json` were exported from the tracker on 29 Sep 2026. If the tracker changes, re-export them rather than editing both.
