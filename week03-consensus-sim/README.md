<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 02](../week02-bitcoin/) · [Week 04 →](../week04-first-contracts/)
<!-- NAV:END -->

# Week 03: Consensus, attacks and proof-of-stake

**Dates:** 12 Oct – 18 Oct 2026 · **Planned time:** 10 h

**Goal:** Learn the problem blockchains solve, then watch forks, partitions and reorgs happen in your own network simulation.

**Ship:** Project 2: a multi-node simulation with gossip, fork resolution, a partition that heals, and stake-weighted proposers

### Plan
- [ ] Learn (75 min): Roughgarden: Lecture 1 (overview, state machine replication, consistency and liveness)  
  [Foundations of Blockchains playlist](https://www.youtube.com/playlist?list=PLEGCF-WLh2RLOHv_xUGLqRts_9JxrckiA)
- [ ] Learn (30 min): Decentralized Thoughts on Nakamoto consensus  
  [Nakamoto's longest-chain-wins protocol](https://decentralizedthoughts.github.io/2021-10-15-Nakamoto-Consensus/)
- [ ] Learn (45 min): Lamport, Shostak and Pease: The Byzantine Generals Problem, sections 1–3  
  [byz.pdf](https://lamport.azurewebsites.net/pubs/byz.pdf)
- [ ] Build (95 min): Build a simulation of 4 nodes that mine and gossip blocks with random network delays and resolve forks by the longest chain
- [ ] Write (30 min): Log: how often did forks happen, and how did delay change that?
- [ ] Learn (60 min): Roughgarden: the lectures on selfish mining and proof-of-stake sybil resistance  
  [Foundations of Blockchains playlist](https://www.youtube.com/playlist?list=PLEGCF-WLh2RLOHv_xUGLqRts_9JxrckiA)
- [ ] Learn (45 min): ethereum.org: proof-of-stake and Gasper  
  [Proof-of-stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/) · [Gasper](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/gasper/)
- [ ] Learn (30 min): Skim Eyal and Sirer, Majority is not Enough (selfish mining)  
  [Selfish mining paper](https://www.cs.cornell.edu/~ie53/publications/btcProcFC.pdf)
- [ ] Build (110 min): Split your network into two halves for 20 blocks, heal it, and log the reorg. Then add stake-weighted proposer selection
- [ ] Write (30 min): Log: a table comparing PoW and PoS on security, finality, energy and who can participate
- [ ] Crypto (30 min): BLS signature aggregation and VRFs. How proof-of-stake compresses thousands of validator votes and picks proposers fairly  
  [ethereum.org: proof-of-stake keys (BLS)](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/keys/) · [A Graduate Course in Applied Cryptography (Boneh & Shoup, free)](https://toc.cryptobook.us/)
- [ ] Apps (20 min): How cryptocurrencies change their rules: read about Bitcoin's block-size dispute and Ethereum's DAO fork. Who decided, and what happened to people who disagreed?  
  [ethereum.org: history of Ethereum](https://ethereum.org/en/history/)

---

## What I built

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
