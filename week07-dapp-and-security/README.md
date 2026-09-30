<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 06](../week06-escrow-nft/) · [Week 08 →](../week08-audit/)
<!-- NAV:END -->

# Week 07: A dApp frontend, then start breaking contracts

**Dates:** 9 Nov – 15 Nov 2026 · **Planned time:** 10 h

**Goal:** Ship a usable escrow frontend, then learn the common vulnerability classes by exploiting them.

**Ship:** Project 3d (escrow dApp with a 2-minute demo) and Ethernaut levels 0–5

### Plan
- [ ] Build (150 min): Build the frontend: connect wallet, create an escrow, release or refund, and list events
- [ ] Write (30 min): Record a 2-minute demo and write the log
- [ ] Learn (45 min): Updraft Smart Contract Security: the introduction section  
  [Smart Contract Security](https://updraft.cyfrin.io/courses/security)
- [ ] Learn (20 min): Read two rekt.news post-mortems: one re-entrancy, one oracle manipulation  
  [rekt.news](https://rekt.news/)
- [ ] Build (105 min): Ethernaut levels 0–5  
  [ethernaut.openzeppelin.com](https://ethernaut.openzeppelin.com/)
- [ ] Write (30 min): Log: for each level, the bug in one line
- [ ] Build (60 min): Install Slither and run it on your ERC-20, Escrow and NFT  
  [Slither](https://github.com/crytic/slither)
- [ ] Learn (30 min): Foundry docs: invariant testing  
  [Foundry guides](https://www.getfoundry.sh/guides)
- [ ] AI (30 min): Give an LLM one vulnerable Ethernaut contract without the hint. Compare its answer with what you found yourself  
  [Ethernaut](https://ethernaut.openzeppelin.com/)
- [ ] Capstone (30 min): Capstone B: point your escrow frontend at Marketplace.sol so you can list, buy and release from the browser
- [ ] Capstone (30 min): Integration test v1 (test/Integration.t.sol): mock credential → list → pay in TestUSD → release, passing in CI alongside the demo
- [ ] Capstone (20 min): Demo stage 4 (payment into escrow). Then open your repo in GitHub Codespaces from the README badge and run make demo there, to confirm a stranger can run it with no setup
- [ ] Capstone (20 min): Invariant tests: escrow always holds what it owes, and TestUSD's total supply equals the sum of balances (invariant_EscrowSolvent, invariant_SupplyEqualsBalances)  
  [Foundry guides (invariant testing)](https://www.getfoundry.sh/guides)
- [ ] Build (45 min): Decentralised storage and web3 logins: pin your block 6 NFT's metadata to IPFS and compare it with the fully on-chain version, then read how ENS names and Sign-In with Ethereum (EIP-4361) work. Note in your log whether week 12's admin console needs SIWE (hint: the contract already checks the role)  
  [IPFS: content addressing (CIDs)](https://docs.ipfs.tech/concepts/content-addressing/) · [ENS docs](https://docs.ens.domains/) · [EIP-4361: Sign-In with Ethereum](https://eips.ethereum.org/EIPS/eip-4361)

---

## Objectives and check-yourself

**By the end of this block you can:**

- Connect a web frontend to your contracts so a non-developer could use it
- Recognise common vulnerability classes by exploiting them (Ethernaut 0–5)
- Run Slither and tell real findings from noise
- Write invariant tests for escrow solvency and token supply
- Store NFT metadata on IPFS, and explain content addressing, ENS and Sign-In with Ethereum

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. What happens, step by step, between clicking "Buy" and the transaction being mined?
2. For each Ethernaut level I solved, what was the bug in one line?
3. Which Slither findings were real, and why were the others noise?
4. What must always be true of my escrow, and how does the invariant test try to break it?
5. What does an IPFS CID guarantee, and what doesn't it guarantee?
6. Could a stranger run my demo in Codespaces without asking me anything?


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
