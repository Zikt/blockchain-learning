# Blockchain, learned in public

[![Trust stack](https://github.com/zikt/blockchain-learning/actions/workflows/trust-stack.yml/badge.svg)](https://github.com/zikt/blockchain-learning/actions/workflows/trust-stack.yml)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/zikt/blockchain-learning)

I'm Isaac Thani Moses, a research engineer and founder based in Kigali. This repo is my 12-week journey (September to December 2026) learning blockchain and the cryptography behind it from first principles, with running threads on AI and real-world applications. Everything is built in the open: code, tests, notes and explainers. It ends in a working **trust stack** that follows a batch of produce from farm to buyer, with proof at every step.

## Start here

| If you want to… | Go to |
|-----------------|-------|
| See the finished project working | [Live demo site](https://zikt.github.io/blockchain-learning/) (from week 11): browse sample batches, listings and trace pages with no login. [How it works](trust-stack/app/README.md) |
| Run the demo yourself, in the browser or locally | [DEMO.md](DEMO.md) |
| Understand how the trust stack works | [trust-stack/README.md](trust-stack/README.md): the story, a diagram, the contracts |
| Check it's tested and secure | [TESTING.md](TESTING.md) and the [latest CI run](https://github.com/zikt/blockchain-learning/actions/workflows/trust-stack.yml) |
| Follow the learning, week by week | [Progress](#progress) below, and [LEARNING_LOG.md](LEARNING_LOG.md) |
| Read the explainers or watch the videos | [blog/](blog/) |
| Build it yourself | [BOM.md](BOM.md) for hardware and accounts, then [trust-stack/README.md](trust-stack/README.md) |

## The capstone in one minute

A cooperative issues role credentials to a farmer, a transporter, an inspector and a buyer. The farmer creates a batch of tomatoes under a rule set (2–8 °C, at most 48 hours in transit, inspection required). Every handoff is signed by someone with the right role, and a sensor in the crate signs temperature readings that are anchored on-chain. The buyer pays in a test stablecoin into escrow. If the batch met its rules, payment is released and the farmer's reputation goes up; if a reading broke them, the buyer can prove it and is refunded. Anyone can look up the batch's journey.

| Part | What it does | Built in |
|------|--------------|----------|
| A. Provenance and traceability | Signed handoffs, ESP32 temperature readings, a product policy, a public trace page | Weeks 6, 10, 11 |
| B. Marketplace | Listings by credentialed sellers, escrow, release only for compliant batches, reputation | Weeks 6–8 |
| C. Payment rail | TestUSD, a test stablecoin, with a cost comparison against bank and mobile money | Weeks 5, 9, 11 |
| D. Credentials | Role credentials for supply-chain actors, and my own proof-of-learning credentials | Weeks 6, 9, 12 |

It runs on test networks only. No real money is involved.

## What's in this repo

```
blockchain-learning/
├── README.md            you are here
├── DEMO.md              how to watch or run the demo
├── TESTING.md           every rule and security property, and the test that checks it
├── BOM.md               hardware and accounts needed to build it
├── LEARNING_LOG.md      dated notes from each study session
├── week01-toy-chain/    one folder per week: code, plus a README with the plan, what I built and learned
├── …
├── week12-agent-wallet/
├── trust-stack/         the capstone: contracts, tests, demo scripts, firmware
│   └── app/             the live demo site (sample data for visitors, admin tab for me)
├── blog/                explainer posts, with links to videos
└── scripts/             helpers that keep the progress table and plan up to date
```

Each folder has a `README.md`, which GitHub shows automatically when you open the folder. Its heading says what the folder is, and it starts with links back to this page (and, in week folders, to the weeks before and after).

## Run the demo

- **Watch it:** open the [latest Trust stack run](https://github.com/zikt/blockchain-learning/actions/workflows/trust-stack.yml) and read the stage table on its summary page, or visit the [live demo site](https://zikt.github.io/blockchain-learning/).
- **Run it in your browser:** click the Codespaces badge above, wait for setup, then `cd trust-stack && make demo`.
- **Run it locally:** see [DEMO.md](DEMO.md).

The demo runs as far as the parts built so far; stages still to come show as "not built yet".

## Progress

This table updates itself from the checklists in each week's README. [progress.json](progress.json) holds the same data for my private study tracker.

<!-- PROGRESS:START -->
**Overall:** `░░░░░░░░░░` 0/159 tasks (0%) · 0 h logged · updated 2026-09-29

| Week | Dates | Project | Progress | Time | Status |
|------|-------|---------|----------|------|--------|
| 1 | 28 Sep – 4 Oct 2026 | [The mental model, keys and signatures](week01-toy-chain/) | `░░░░░░░░░░` 0/13 (0%) | 0 h | Not started |
| 2 | 5 Oct – 11 Oct 2026 | [Bitcoin: UTXOs, raw transactions and mining](week02-bitcoin/) | `░░░░░░░░░░` 0/13 (0%) | 0 h | Not started |
| 3 | 12 Oct – 18 Oct 2026 | [Consensus, attacks and proof-of-stake](week03-consensus-sim/) | `░░░░░░░░░░` 0/12 (0%) | 0 h | Not started |
| 4 | 19 Oct – 25 Oct 2026 | [The Ethereum model and Solidity fluency](week04-first-contracts/) | `░░░░░░░░░░` 0/12 (0%) | 0 h | Not started |
| 5 | 26 Oct – 1 Nov 2026 | [Foundry and your ERC-20](week05-erc20/) | `░░░░░░░░░░` 0/13 (0%) | 0 h | Not started |
| 6 | 2 Nov – 8 Nov 2026 | [Escrow and an on-chain NFT](week06-escrow-nft/) | `░░░░░░░░░░` 0/19 (0%) | 0 h | Not started |
| 7 | 9 Nov – 15 Nov 2026 | [A dApp frontend, then start breaking contracts](week07-dapp-and-security/) | `░░░░░░░░░░` 0/13 (0%) | 0 h | Not started |
| 8 | 16 Nov – 22 Nov 2026 | [Deeper exploits and your own audit](week08-audit/) | `░░░░░░░░░░` 0/11 (0%) | 0 h | Not started |
| 9 | 23 Nov – 29 Nov 2026 | [AMMs, oracles, rollups](week09-amm-and-capstone-spec/) | `░░░░░░░░░░` 0/14 (0%) | 0 h | Not started |
| 10–11 | 30 Nov – 13 Dec 2026 | [Capstone, a four-part trust stack](week10-11-capstone/) | `░░░░░░░░░░` 0/23 (0%) | 0 h | Not started |
| 12 | 14 Dec – 20 Dec 2026 | [Agents with wallets, verifiable AI, and a retrospective](week12-agent-wallet/) | `░░░░░░░░░░` 0/16 (0%) | 0 h | Not started |
<!-- PROGRESS:END -->

## Writing and videos

An explainer every two weeks about what I've built and learned, sometimes with a short video. Teaching it is how I check I actually understand it.

<!-- BLOG:START -->
_No posts yet. The first explainer is due in week 2._
<!-- BLOG:END -->

## Milestones

- [ ] `v0.1-toy-chain`: signed, Merkle-rooted toy blockchain (week 1)
- [ ] `v0.2-network-sim`: multi-node consensus simulation (week 3)
- [ ] `v0.3-testusd`: ERC-20 test stablecoin, and demo stage 1 (week 5)
- [ ] `v0.4-marketplace`: marketplace with credential checks and a web frontend (weeks 6–7)
- [ ] `v0.5-audit`: audit and attack tests (week 8)
- [ ] `v0.6-credentials`: role credential registry (week 9)
- [ ] `v0.7-provenance`: ESP32-signed traceability (week 10)
- [ ] `v1.0-trust-stack`: all four parts on Base Sepolia, tested end to end, demo site live (week 11)
- [ ] `v1.1-live-demo`: seeded demo data, admin console, proof-of-learning credentials (week 12)

## How I work

- Weekly rhythm: Tue 2h, Thu 2h, Fri 1.5h, Sat 4.5h, with Sunday off.
- I tick tasks in each week's README as I finish them, commit at the end of every session, and push every Saturday.
- Session notes go in [LEARNING_LOG.md](LEARNING_LOG.md); explainers go in [blog/](blog/).
- Everything runs on local chains and testnets. No mainnet funds, and no private keys in this repo.

## Tools

Python · Bitcoin Core (regtest) · Solidity · Foundry · viem · ESP32 (ESP-IDF) · Base Sepolia · GitHub Actions · EZKL

## License

MIT. Personal site: [paa.ge/isaacthani](https://paa.ge/isaacthani/).
