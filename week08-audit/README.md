<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 07](../week07-dapp-and-security/) · [Week 09 →](../week09-amm-and-capstone-spec/)
<!-- NAV:END -->

# Week 08: Deeper exploits and your own audit

**Dates:** 16 Nov – 22 Nov 2026 · **Planned time:** 10 h

**Goal:** Solve harder levels, then treat your earlier contracts as someone else's and write a real findings report.

**Ship:** Project 4: AUDIT.md with severity-ranked findings, invariant tests and fixes

### Plan
- [ ] Build (135 min): Ethernaut: Re-entrancy, Elevator, Privacy and one more level of your choice  
  [Ethernaut](https://ethernaut.openzeppelin.com/)
- [ ] Learn (45 min): ConsenSys best practices: the attacks section  
  [Smart contract best practices](https://consensys.github.io/smart-contract-best-practices/)
- [ ] Write (30 min): Log: which Slither findings were real and which were noise
- [ ] Build (60 min): Damn Vulnerable DeFi: challenge 1 (Unstoppable)  
  [damnvulnerabledefi.xyz](https://www.damnvulnerabledefi.xyz/)
- [ ] Build (165 min): Audit your Escrow, ERC-20 and NFT: write each finding (severity, description, fix), add invariant tests, and fix the code
- [ ] Write (30 min): Log: the one mistake you'll never make again
- [ ] Learn (15 min): Read one more rekt.news post-mortem and match it to a bug class you now know  
  [rekt.news](https://rekt.news/)
- [ ] AI (30 min): AI-assisted audit: run an LLM over your escrow and compare its findings with Slither's and your own. Count true and false positives in AUDIT.md
- [ ] Explain (45 min): Explainer #4: write "What I learned auditing my own smart contracts" in blog/ (600–900 words, weeks 7–8). Optional: record a 5-minute video teaching it and link it in the post
- [ ] Capstone (15 min): Add the integration to your audit: what breaks if a mock is swapped for a malicious contract, or a batch id is reused? Note findings in AUDIT.md
- [ ] Capstone (30 min): Attack tests in test/Attacks.t.sol: replayed signature, reused batch id, re-entrancy on release, a stranger releasing escrow. Each must fail the way TESTING.md says
- [ ] Apps (45 min): DAOs and on-chain governance: how proposals, token voting, quorums and timelocks work (OpenZeppelin Governor), then the Beanstalk attack (April 2022), where a flash loan bought enough votes to drain the treasury in one transaction. In your log, for next week's SPEC.md: who should hold the trust stack's issuer and arbiter roles, you, a Safe multisig, or a DAO of cooperatives?  
  [ethereum.org: DAOs](https://ethereum.org/en/dao/) · [OpenZeppelin: on-chain governance](https://docs.openzeppelin.com/contracts/governance) · [Beanstalk - REKT](https://rekt.news/beanstalk-rekt) · [Updraft: DAOs (optional build)](https://updraft.cyfrin.io/courses/advanced-foundry/daos/create-governor-contract)

---

## Objectives and check-yourself

**By the end of this block you can:**

- Solve harder exploits, including re-entrancy, storage "privacy" and Damn Vulnerable DeFi's Unstoppable
- Audit your own contracts and write severity-ranked findings with fixes
- Compare what AI, tools and your own review each find
- Write attack tests that fail exactly the way TESTING.md says
- Explain how DAOs govern with token voting, and how governance can be attacked

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. Why is "private" state not private on a blockchain?
2. What is the most severe finding in my AUDIT.md, and how did I fix it?
3. What did the LLM find that Slither missed, and what did it get wrong?
4. What breaks if one of my mocks is swapped for a malicious contract?
5. How did the Beanstalk attacker pass a governance vote in one transaction, and which defences (timelocks, vote snapshots) would have stopped it?
6. Who should hold the issuer and arbiter roles in my trust stack, and why?


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
