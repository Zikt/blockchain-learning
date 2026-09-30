<!-- NAV:START -->
[↑ Overview](../README.md) · [← Weeks 10–11](../week10-11-capstone/)
<!-- NAV:END -->

# Week 12: Agents with wallets, verifiable AI, and a retrospective

**Dates:** 14 Dec – 20 Dec 2026 · **Planned time:** 10 h

**Goal:** Give an LLM agent spending power that a contract limits, try to break it, and learn what zkML can and can't prove.

**Ship:** Project 7 (guarded agent wallet with a red-team report), an implications memo, and your retrospective

### Plan
- [ ] Learn (30 min): Vitalik Buterin: The promise and challenges of crypto + AI applications  
  [vitalik.eth.limo](https://vitalik.eth.limo/general/2024/01/30/cryptoai.html)
- [ ] Learn (30 min): ERC-4337 motivation, then EIP-7702  
  [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) · [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702)
- [ ] Learn (30 min): x402 docs: the quickstart  
  [docs.x402.org](https://docs.x402.org/) · [x402 on GitHub](https://github.com/x402-foundation/x402)
- [ ] Learn (20 min): ERC-8004 abstract and motivation  
  [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004)
- [ ] Learn (20 min): Simon Willison on prompt injection: two posts  
  [Prompt injection series](https://simonwillison.net/series/prompt-injection/)
- [ ] Build (105 min): Build a guarded agent wallet that pays through your TestUSD rail: a contract wallet with a daily cap and a recipient allowlist, and an LLM with a single 'pay' tool. Try five injection prompts and record what the contract blocked
- [ ] Write (30 min): Log: which defences held in the model and which only held in the contract
- [ ] Learn (30 min): Vitalik Buterin: an approximate introduction to how zk-SNARKs are possible  
  [vitalik.eth.limo](https://vitalik.eth.limo/general/2021/01/26/snarks.html)
- [ ] Learn (30 min): EZKL: read the getting-started guide and run its example (the full build is optional)  
  [EZKL docs](https://docs.ezkl.xyz/getting-started/) · [ezkl on GitHub](https://github.com/zkonduit/ezkl)
- [ ] Write (45 min): Memo: custody for autonomous agents, accountability, energy, and the current rules in Rwanda, Nigeria and the EU (check these; they change)  
  [EU MiCA (ESMA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)
- [ ] Write (60 min): Retrospective: pick the next direction (ZK, auditing, DePIN, or agent payments)
- [ ] Build (20 min): Proof of learning (Capstone D): issue yourself a credential for each finished week, with that week's folder commit hash as evidence, and verify one on the testnet
- [ ] Crypto (30 min): Zero-knowledge in practice. Read the first chapters of the RareSkills ZK Book, then revisit what your EZKL proof actually proved  
  [RareSkills ZK Book (free)](https://www.rareskills.io/zk-book)
- [ ] Apps (30 min): Other applications, one paragraph each on who has to trust whom: tokenised real-world assets, DAOs and on-chain governance, prediction markets, and DePIN networks  
  [ethereum.org: DAOs](https://ethereum.org/en/dao/) · [Helium docs (DePIN example)](https://docs.helium.com/)
- [ ] Capstone (30 min): Seed the live demo: put throwaway actor keys in trust-stack/.env (never your real wallet), run make seed so the sample batches, listings and one failing batch exist on Base Sepolia, then make smoke. Rerun make seed any time to top it up  
  [Foundry: keystores (cast wallet)](https://getfoundry.sh/cast/reference/cast-wallet-import)
- [ ] Capstone (60 min): Admin console: an Admin tab that appears only when the connected wallet holds the issuer role on-chain. From it, issue a credential, create a batch, record a step and anchor readings, so you can show something new live. The contracts enforce the role; the page only hides the buttons  
  [viem: writing to contracts](https://viem.sh/docs/contract/writeContract)

---

## Objectives and check-yourself

**By the end of this block you can:**

- Give an AI agent a contract wallet with limits, and show which limits held under prompt injection
- Explain account abstraction (ERC-4337, EIP-7702) and agent payments (x402)
- Explain what zk-SNARKs and zkML can and can't prove
- Issue verifiable credentials for your own learning, backed by commit hashes
- Seed the live demo and run an admin console gated by an on-chain role
- Reflect on what you learned and choose your next direction

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. Which injection prompts fooled the model, and did the contract still block the payment?
2. What does my EZKL proof actually prove about the model, and what doesn't it?
3. What is the difference between an ordinary account, an ERC-4337 smart account and an EIP-7702 delegated account?
4. If someone doubts my week 5 credential, how can they check it themselves?
5. What would I build with one more month, and why?
6. Of tokenised assets, DAOs, prediction markets and DePIN, which has the most honest need for a blockchain?


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
