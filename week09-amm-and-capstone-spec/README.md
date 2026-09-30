<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 08](../week08-audit/) · [Weeks 10–11 →](../week10-11-capstone/)
<!-- NAV:END -->

# Week 09: AMMs, oracles, rollups

**Dates:** 23 Nov – 29 Nov 2026 · **Planned time:** 10 h

**Goal:** Build x·y=k, see why a spot price is a dangerous oracle, compare rollups by their real risks, and decide exactly what your capstone puts on-chain.

**Ship:** Project 5 (AMM with a fuzz test), the 'do you need a blockchain?' memo, and SPEC.md for the capstone

### Plan

- [ ] Learn (30 min): Finematics: the AMM and Uniswap explainers  
  [Finematics channel](https://www.youtube.com/@Finematics)
- [ ] Learn (30 min): Uniswap v2 whitepaper, sections 1–3  
  [Uniswap v2 whitepaper](https://uniswap.org/whitepaper.pdf)
- [ ] Build (75 min): Build an AMM with addLiquidity, removeLiquidity and swap with a 0.3% fee. Fuzz-test that k never decreases
- [ ] Learn (60 min): DeFi MOOC lecture: Oracles (Ari Juels)  
  [Oracles lecture](https://www.youtube.com/watch?v=vFcW18ZpPZ4)
- [ ] Learn (30 min): Chainlink: Data Feeds overview  
  [docs.chain.link](https://docs.chain.link/)
- [ ] Learn (30 min): Vitalik Buterin: An incomplete guide to rollups  
  [vitalik.eth.limo](https://vitalik.eth.limo/general/2021/01/05/rollup.html)
- [ ] Learn (30 min): L2BEAT: read the FAQ, then compare two rollups on its risk dashboard  
  [L2BEAT](https://l2beat.com/) · [L2BEAT FAQ](https://l2beat.com/faq)
- [ ] Write (60 min): Write a 'do you need a blockchain?' memo for remittances, land registry and cold-chain provenance
- [ ] Write (90 min): Capstone SPEC.md for the whole trust stack: actors, trust assumptions, what is on-chain vs. off-chain for each part, the threat model, and the end-to-end test you'll write in week 11
- [ ] Write (30 min): Log: slippage on a small pool vs. a large one, with numbers from your tests
- [ ] Crypto (30 min): Commitments and Merkle proofs. Write a Merkle proof verifier in Solidity and test it (you'll reuse it in the capstone)  
  [OpenZeppelin MerkleProof](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleProof)
- [ ] Apps (30 min): Payments and remittances in Africa: compare the cost of sending $200 to Nigeria or Rwanda by bank, mobile money and a stablecoin. Add the numbers to your 'do you need a blockchain?' memo  
  [World Bank: Remittance Prices Worldwide](https://remittanceprices.worldbank.org/)
- [ ] Capstone (60 min): Capstone D: CredentialRegistry.sol with roles (farmer, cooperative, transporter, inspector, buyer). An issuer signs EIP-712 credentials, each cohort is Merkle-rooted on-chain, and isValid(account, role) replaces the mock in the integration test  
  [EIP-712](https://eips.ethereum.org/EIPS/eip-712)
- [ ] Capstone (15 min): Credential tests: a revoked credential can't sign or list (test_RevertWhen_RevokedCredential). Switch demo stage 2 from the mock to the real registry


- [ ] Apps (45 min): Stablecoins II: why they matter in Africa, the BIS critique, and the rules (MiCA, GENIUS Act, Rwanda and Nigeria)
- [ ] Explain (45 min): Stablecoin write-up: "Digital dollars for Africa? What stablecoins could fix and what they risk" in blog/ (600–900 words)
---

## Objectives and check-yourself

**By the end of this block you can:**

- Build a constant-product AMM and prove with a fuzz test that k never decreases
- Explain why an AMM spot price is a dangerous oracle, and how Chainlink feeds differ
- Compare rollups by their real risks using L2BEAT
- Decide with numbers whether a use case needs a blockchain at all
- Explain why stablecoins matter in Africa, and what regulators worry about
- Write the trust stack's SPEC.md and replace the credential mock with the real registry

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. What slippage did my tests show for the same trade on a small pool and a large one?
2. How could an attacker move my AMM's price inside one transaction, and who would lose?
3. What can Base's operator do to my funds today, according to L2BEAT?
4. Sending $200 to Nigeria or Rwanda: which route was cheapest, and what costs remain when the recipient cashes out?
5. For each trust-stack part, what is on-chain, what is off-chain, and why?
6. What does revoking a credential stop, and what can't it undo?


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
