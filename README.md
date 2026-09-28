# Blockchain, learned in public

I'm learning blockchain from first principles and building every step in the open: 12 weeks at 10 hours a week, from a toy blockchain in Python to a tamper-evident cold-chain provenance system, where edge devices sign sensor readings and a smart contract on an L2 testnet verifies them.

Each week has its own folder with the code, a README on what I built and learned, and what broke along the way.

## Progress

This table updates itself: tick the boxes in each week's README, add rows to its "Time spent" table, and push. A GitHub Action rebuilds it.

<!-- PROGRESS:START -->
**Overall:** `░░░░░░░░░░` 0/111 tasks (0%) · 0 h logged · updated 2026-09-28

| Week | Dates | Project | Progress | Time | Status |
|------|-------|---------|----------|------|--------|
| 1 | 28 Sep – 4 Oct 2026 | [The mental model, keys and signatures](week01-toy-chain/) | `░░░░░░░░░░` 0/11 (0%) | 0 h | Not started |
| 2 | 5 Oct – 11 Oct 2026 | [Bitcoin: UTXOs, raw transactions and mining](week02-bitcoin/) | `░░░░░░░░░░` 0/10 (0%) | 0 h | Not started |
| 3 | 12 Oct – 18 Oct 2026 | [Consensus, attacks and proof-of-stake](week03-consensus-sim/) | `░░░░░░░░░░` 0/10 (0%) | 0 h | Not started |
| 4 | 19 Oct – 25 Oct 2026 | [The Ethereum model and Solidity fluency](week04-first-contracts/) | `░░░░░░░░░░` 0/9 (0%) | 0 h | Not started |
| 5 | 26 Oct – 1 Nov 2026 | [Foundry and your ERC-20](week05-erc20/) | `░░░░░░░░░░` 0/9 (0%) | 0 h | Not started |
| 6 | 2 Nov – 8 Nov 2026 | [Escrow and an on-chain NFT](week06-escrow-nft/) | `░░░░░░░░░░` 0/10 (0%) | 0 h | Not started |
| 7 | 9 Nov – 15 Nov 2026 | [A dApp frontend, then start breaking contracts](week07-dapp-and-security/) | `░░░░░░░░░░` 0/8 (0%) | 0 h | Not started |
| 8 | 16 Nov – 22 Nov 2026 | [Deeper exploits and your own audit](week08-audit/) | `░░░░░░░░░░` 0/7 (0%) | 0 h | Not started |
| 9 | 23 Nov – 29 Nov 2026 | [AMMs, oracles, rollups](week09-amm-and-capstone-spec/) | `░░░░░░░░░░` 0/10 (0%) | 0 h | Not started |
| 10–11 | 30 Nov – 13 Dec 2026 | [Capstone, tamper-evident cold-chain provenance](week10-11-capstone/) | `░░░░░░░░░░` 0/15 (0%) | 0 h | Not started |
| 12 | 14 Dec – 20 Dec 2026 | [Agents with wallets, verifiable AI, and a retrospective](week12-agent-wallet/) | `░░░░░░░░░░` 0/12 (0%) | 0 h | Not started |
<!-- PROGRESS:END -->

## Milestones

- [ ] `v0.1-toy-chain`: signed, Merkle-rooted toy blockchain (week 1)
- [ ] `v0.2-network-sim`: multi-node consensus simulation (week 3)
- [ ] `v0.3-erc20`: ERC-20 from scratch, verified on Sepolia (week 5)
- [ ] `v0.4-escrow-dapp`: escrow contract with a web frontend (week 7)
- [ ] `v0.5-audit`: audit of my own contracts (week 8)
- [ ] `v0.6-amm`: constant-product AMM (week 9)
- [ ] `v1.0-capstone`: cold-chain provenance system (week 11)
- [ ] `v1.1-agent-wallet`: guarded LLM agent wallet (week 12)

## How I work

- Weekly rhythm: Tue 2h, Thu 2h, Fri 1.5h, Sat 4.5h, with Sunday off.
- I tick tasks in each week's README as I finish them, commit at the end of every session, and push every Saturday. The progress table above updates automatically.
- Session notes go in [LEARNING_LOG.md](LEARNING_LOG.md).
- Everything runs on local chains and testnets. No mainnet funds, no real keys in this repo.

## Tools

Python · Bitcoin Core (regtest) · Solidity · Foundry · viem / Scaffold-ETH 2 · ESP32 (ESP-IDF) · EZKL

## License

MIT
