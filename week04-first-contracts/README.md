<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 03](../week03-consensus-sim/) · [Week 05 →](../week05-erc20/)
<!-- NAV:END -->

# Week 04: The Ethereum model and Solidity fluency

**Dates:** 19 Oct – 25 Oct 2026 · **Planned time:** 10 h

**Goal:** Understand accounts, gas and the EVM, deploy your first contract to Sepolia, and get comfortable writing Solidity.

**Ship:** SimpleStorage on Sepolia and five small contracts in /week04

### Plan
- [ ] Learn (45 min): Read the Ethereum whitepaper  
  [ethereum.org/whitepaper](https://ethereum.org/en/whitepaper/)
- [ ] Learn (60 min): ethereum.org docs: accounts, transactions, gas and fees, the EVM  
  [Ethereum developer docs](https://ethereum.org/en/developers/docs/)
- [ ] Build (90 min): Cyfrin Updraft: Blockchain Basics, then the first Remix lessons of Solidity Smart Contract Development  
  [Blockchain Basics](https://updraft.cyfrin.io/courses/blockchain-basics) · [Updraft course list](https://updraft.cyfrin.io/courses) · [Remix IDE](https://remix.ethereum.org/)
- [ ] Build (30 min): Set up a wallet in a separate browser profile, get Sepolia ETH from a faucet, deploy SimpleStorage  
  [Google Cloud Sepolia faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia)
- [ ] Write (30 min): Log: the difference between a Bitcoin UTXO and an Ethereum account
- [ ] Learn (75 min): Work through the first ~25 Solidity by Example pages, running each in Remix  
  [solidity-by-example.org](https://solidity-by-example.org/)
- [ ] Learn (70 min): Updraft: continue the Solidity course (the FundMe section)  
  [Updraft courses](https://updraft.cyfrin.io/courses)
- [ ] Build (75 min): Write 5 small contracts without looking: a counter, a whitelist, a vault, a voting contract, a timelock
- [ ] Write (30 min): Log: what surprised you about gas costs
- [ ] Crypto (20 min): Keccak-256 vs. SHA-3, and how an Ethereum address is derived from a public key. Derive one yourself in Python  
  [ethereum.org: accounts](https://ethereum.org/en/developers/docs/accounts/)
- [ ] Explain (45 min): Explainer #2: write "How strangers agree: consensus in plain words" in blog/ (600–900 words, weeks 3–4). Optional: record a 5-minute video teaching it and link it in the post
- [ ] Apps (30 min): Exchanges and wallets: custodial vs. self-custody, centralised exchanges vs. DEXs, and what the FTX collapse showed about 'not your keys, not your coins'  
  [ethereum.org: wallets](https://ethereum.org/en/wallets/) · [ethereum.org: DeFi](https://ethereum.org/en/defi/)
- [ ] Apps (30 min): What "web3" means, and the case against it: read ethereum.org's introduction to web3, then Moxie Marlinspike's "My first impressions of web3". In your log, list which web3 claims this plan lets you test yourself, and your view today  
  [ethereum.org: what is web3?](https://ethereum.org/en/web3/) · [Moxie Marlinspike: My first impressions of web3](https://moxie.org/2022/01/07/web3-first-impressions.html)

---

## Objectives and check-yourself

**By the end of this block you can:**

- Explain accounts (externally owned vs contract), gas and fees, and how the EVM runs a transaction
- Deploy a contract to Sepolia from a testnet-only wallet
- Write small contracts with mappings, modifiers, events and custom errors from memory
- Derive an Ethereum address from a public key with Keccak-256
- Compare custodial wallets, self-custody, centralised exchanges and DEXs
- Explain what "web3" claims, and the strongest case against it

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. How does an Ethereum account differ from a Bitcoin UTXO?
2. Why does a failed transaction still cost gas?
3. What is the difference between storage and memory, and which costs more?
4. From memory: how do I get from a private key to an address?
5. What did the FTX collapse show about "not your keys, not your coins"?
6. Which web3 claims will this plan let me test myself, and what do I think of them today?


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
