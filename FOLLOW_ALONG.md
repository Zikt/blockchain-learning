[↑ Overview](README.md)

# Take this course yourself

**Genesis to Capstone** is a 12-week path from "what is a hash?" to a tested, deployed blockchain system: a *trust stack* that follows a batch of produce from farm to buyer, with credentials, signed sensor readings, escrow payments and a public trace page. It was built in public by [Isaac Thani Moses](https://github.com/Zikt/blockchain-learning), and everything here is free to reuse.

You can use it in three ways:

| If you want to… | Do this | Setup |
|---|---|---|
| **Practise** blockchain concepts | Use the [flashcards and quizzes](https://zikt.github.io/blockchain-learning/cards/). There are 12 blocks, each with a warm-up, key questions, a final quiz and a strengths view | None |
| **Read along** | Read [PLAN.md](PLAN.md): every task, with links to the resources | None |
| **Take the whole course**, with your own repo, tracker, flashcard site and proof of learning | Follow the steps below | About 20 minutes |

## What you need

| | When | Cost |
|---|---|---|
| A GitHub account, [Git](https://git-scm.com/downloads), [Python 3.11+](https://www.python.org/downloads/) and [VS Code](https://code.visualstudio.com/) | Week 1 | Free |
| Bitcoin Core, then Foundry and Node.js 20+ | Weeks 2 and 5. Each week's tasks say how to install them | Free |
| A browser wallet in a separate browser profile, and testnet ETH from faucets | Week 4 | Free (testnets only) |
| An ESP32 board and a temperature sensor. The list is in [BOM.md](BOM.md) | Order by week 6, needed in week 10. A Python device simulator works if you'd rather skip hardware | A few tens of US dollars |
| An LLM API key | Week 12 | A few dollars of credit |
| Docker Desktop | Optional | Free |

Time: about **10 hours a week for 12 weeks**. A slower pace works too; see [Going at your own pace](#going-at-your-own-pace). You should be comfortable writing basic Python.

## Set up your copy

### 1. Create your repo from this one

On the [course repo](https://github.com/Zikt/blockchain-learning), click **Use this template → Create a new repository**. Name it `blockchain-learning` (or anything you like), make it **Public**, and create it.

A template gives you your own clean repo, whose commit history becomes your record of learning, and GitHub Actions work in it straight away. A fork works too, but a fork's history is tied to the original repo, and GitHub keeps Actions turned off in forks until you enable them.

### 2. Get it onto your computer

```
git clone https://github.com/<your-username>/blockchain-learning.git
cd blockchain-learning
```

### 3. Make it yours

The course repo holds the original author's progress, dates and answers. One script resets it for you. Run it first without `--apply` to preview the changes, then again with `--apply`:

```
python scripts/start_my_copy.py --name "Your Name" --start 2027-01-04
python scripts/start_my_copy.py --name "Your Name" --start 2027-01-04 --apply
```

On Windows, use `py` if `python` isn't found. Your start date moves to the Monday of that week. The script:

- points every link at your GitHub account and site, and puts your name in the README, crediting the original course
- re-dates the whole plan from your start: the week READMEs, PLAN.md, the tracker and the countdown
- unticks every task and clears the author's write-ups, time tables, learning log, output links and blog posts
- moves the author's code and capstone work into `reference/`, so you can compare later or just delete it, and restores the starter files
- clears the author's flashcard answers so you write your own, because putting answers in your own words is the learning. Add `--keep-answers` to keep them as a study aid

### 4. Save it and turn on your site

```
git add -A
git commit -m "Start my copy of the course"
git push
```

Then, on GitHub:

1. Go to **Settings → Pages**, and under **Build and deployment** set **Source** to **GitHub Actions**.
2. Go to the **Actions** tab, choose **Site**, then **Run workflow**.

In a minute or two your site is live at `https://<your-username>.github.io/blockchain-learning/`, with:

- **/tracker/**: every task with its due date, the week's objectives, a countdown, a session log and links to your published work
- **/cards/**: your flashcards and quizzes, with your strengths by block and topic, and an Anki deck to download
- **/demo/**: your trust-stack demo, once you build it in week 11

Your progress in the tracker and flashcards is saved in the browser you use, so stick to one browser, or use **Download progress** to move it.

### 5. Check the badges

Open your repo's README. The **Trust stack** badge and the Codespaces button now point at your repo. The Trust stack workflow shows "skipped" for its tests until you write your first contract in week 5. That's expected.

## Your weekly rhythm

Every block has the same shape:

| Day | Session | What to do |
|---|---|---|
| Tue | 2 h | Reading and videos (the Learn, Crypto and Apps tasks). Take the block's **warm-up quiz** first |
| Thu | 2 h | Finish the reading, then start the build |
| Fri | 1.5 h | Keep building |
| Sat | 4.5 h | Finish the build. Answer the **check-yourself** questions in `LEARNING_LOG.md`, write your answers to the block's **key questions** in `cards/blockNN.md`, and take the **final quiz** |
| Sun | Rest | |
| Mon, Wed | Flex | Any time you log counts |

At the end of each session:

```
python scripts/apply_tracker.py x1t1 x1t2     # tick the tasks you finished (IDs are in the tracker and PLAN.md)
git add -A
git commit -m "week01: what you did"
git push
```

Add a row to the week README's **Time spent** table as well. Every push updates the progress table on your README, rebuilds your flashcards and Anki deck, and runs the tests. On Saturday, paste your week's folder link into the tracker as proof of learning.

**Explainers.** Five times during the course you write a short post in `blog/`, and a video is optional. Publishing them is how others learn from you, and it's the best test of your own understanding.

## Going at your own pace

- **The dates are a guide.** They drive the countdown and the due dates, nothing else.
- **Fell behind?** Skip ahead rather than doubling up, and come back to what you missed. Or re-plan from a new start date without losing any progress:
  ```
  python scripts/start_my_copy.py --start 2027-02-01 --dates-only --apply
  ```
  Then set the same date at the top of your tracker.
- **Less time each week?** Give each block two weeks. When a block runs over, re-plan with `--dates-only`.
- **Skipping hardware?** In weeks 10–11, use a Python device simulator in place of the ESP32. The tasks say how.
- **Only here for some topics?** Each block's cards and quizzes stand on their own, so dip in anywhere.

## Reminders

Set recurring calendar events for Tue, Thu, Fri and Sat. If you use an AI assistant that can run scheduled tasks, you can ask it for a study nudge instead. Adapt this:

> Every Tuesday, Thursday and Friday at 18:00 and Saturday at 09:00 (my time zone: …), read my progress at `https://raw.githubusercontent.com/<me>/blockchain-learning/main/progress.json` and the plan in `PLAN.md` in the same repo. Send me a short message with today's 2–3 next tasks, how many tasks I've finished this block, and whether I'm on schedule. On Saturdays, pick two of the block's check-yourself questions for me to answer. Ask what I did last session.

## Staying up to date with the course

The original course keeps improving, with new questions, fixes and features. To pull in the site and build-script updates:

```
git remote add course https://github.com/Zikt/blockchain-learning.git   # once
git fetch course
git checkout course/main -- site/ scripts/build_site.py
git commit -m "Update practice site from the course" && git push
```

For new or changed questions, see what changed with `git diff HEAD course/main -- cards/`, then copy new questions into your files by hand, so your own answers stay put.

## Stay safe

- Use testnets only. Nothing in this course needs real money.
- Keep your course wallet in a separate browser profile, and never reuse a wallet that holds real funds.
- Never commit private keys, seed phrases or `.env` files. The `.gitignore` already blocks the usual ones. Deploy with an encrypted keystore (`cast wallet import`), as the week 11 tasks explain.

## Questions, fixes and contributions

- Stuck, or spotted a mistake in the plan or a question? [Open an issue](https://github.com/Zikt/blockchain-learning/issues) on the course repo.
- Wrote a clearer answer to a key question? Open a pull request that edits `cards/blockNN.md` on the course repo. The build checks the format.
- Finished? Share your repo and site. Your commit history, explainers and deployed trust stack are your proof of learning.

## Credit and licence

The course is by Isaac Thani Moses, and the code and text are under the [MIT licence](LICENSE). Keep the original copyright line in `LICENSE`; you're welcome to add your own line for your work. The resources linked from the plan belong to their authors.
