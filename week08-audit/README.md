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
