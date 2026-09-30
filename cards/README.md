[↑ Overview](../README.md) · [Practise online](https://zikt.github.io/blockchain-learning/cards/)

# Practice cards

Flashcards and quizzes for the 12 blocks of the plan. Anyone can use them, whether or not you're following the plan.

- **Practise online:** [zikt.github.io/blockchain-learning/cards](https://zikt.github.io/blockchain-learning/cards/). No account needed; your progress stays in your browser.
- **Practise in Anki:** download `genesis-to-capstone.apkg` from the page above and open it in [Anki](https://apps.ankiweb.net/). It's one deck, *Genesis to Capstone*, with a sub-deck per block. Download it again whenever cards are added and import it over the old one: existing cards update, and your review history is kept.

## How each block works

| Part | When | What it's for |
|---|---|---|
| **Before you start** | Before the block (optional) | A 3-question warm-up. It's your baseline, so it doesn't count toward your strength |
| **Key questions** | While you study | 8 flashcards on the block's core ideas. Rate yourself Again, Hard, Good or Easy and they come back when you're about to forget |
| **Final quiz** | After the block | 6 questions. Your latest score, together with your flashcard ratings, gives your strength for the block |
| **Reflect** | Saturday, if you follow the plan | Questions about your own builds. Answer them in LEARNING_LOG.md. They aren't scored or exported |

The **Strengths** tab shows each block as Strong, Solid, Shaky or Needs work, your weakest topics, and the cards and questions you keep missing, with a button to practise just those.

In Anki, the same information comes from its own statistics. Every card is tagged `block::01`, `topic::hashing` and `type::key` (or `pre`, `post`), so you can search, for example, `tag:topic::consensus prop:lapses>1`, or build a filtered deck of the cards you forgot this month. Cards you keep forgetting get tagged `leech` automatically.

## Writing answers to the key questions

Each key question has an empty `Answer:` line. Write yours underneath, in your own words: a few sentences, a formula, or a small example. Putting it in your own words is the learning. Cards without an answer still show up online, where learners can write their own. Only answered cards go into the Anki deck.

```markdown
### b01-key-1 · chain-structure
Why does changing one transaction in an old block invalidate every block after it?

Answer:
Each block stores the hash of the previous block. Changing a transaction changes that
block's hash, so the next block's "previous hash" no longer matches, and so on to the tip.
source: week01-toy-chain/toy_chain.py
```

`source:` is optional: a file, a link or a book chapter where the answer comes from.

## File format

One file per block: `cards/block01.md` … `cards/block12.md`. Each has a short header, then four sections in this order: `## Before you start`, `## Key questions`, `## Final quiz`, `## Reflect`.

Every card starts with `### <id> · <topic>`:

- **The id** never changes once published, even if you reword the question. It's how Anki keeps your review history. Use `b<block>-<pre|key|post|ref>-<n>`, and give new cards the next number.
- **The topic** is a short lower-case tag such as `hashing` or `stablecoins`. It powers "weakest topics".

Quiz questions (warm-up and final) list options as `- A. …`, then give `answer:` and `why:`. The answer sits inside `<details>` so it stays hidden when reading on GitHub:

```markdown
### b01-post-2 · hashing
Which property means it's infeasible to find any two different inputs with the same hash?

- A. Preimage resistance
- B. Second-preimage resistance
- C. Collision resistance
- D. Determinism

<details><summary>Answer</summary>

answer: C
why: Collision resistance is about any pair; second-preimage is about matching one given input.

</details>
```

## Checking and building

```
python scripts/build_site.py --check    # checks every card and prints a count
python scripts/build_site.py            # builds the whole site into dist/site/ (pip install genanki for the Anki deck)
```

Then open `dist/site/cards/index.html` in a browser to try it. On every push, GitHub Actions runs the same build and publishes the site (see `.github/workflows/pages.yml`). If a card is malformed, the build fails and names the file and line.

## Contributing

Spotted a wrong answer or a better way to explain something? Edit the block's file on GitHub and open a pull request. The build checks your change before it's merged.
