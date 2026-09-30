<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 05](../week05-erc20/) · [Week 07 →](../week07-dapp-and-security/)
<!-- NAV:END -->

# Week 06: Escrow and an on-chain NFT

**Dates:** 2 Nov – 8 Nov 2026 · **Planned time:** 10 h

**Goal:** Write your first contract that holds value, then an NFT whose image lives entirely on-chain. End with frontend prep for next week.

**Ship:** Project 3b (Escrow.sol) and Project 3c (on-chain SVG NFT)

### Plan
- [ ] Learn (20 min): Solidity docs: Security Considerations (read before writing code that holds money)  
  [Security considerations](https://docs.soliditylang.org/en/latest/security-considerations.html)
- [ ] Learn (20 min): Solidity by Example: Sending Ether, Payable, and the Re-entrancy hack  
  [solidity-by-example.org](https://solidity-by-example.org/)
- [ ] Build (135 min): Build Escrow: deposit, release by buyer or arbiter, refund after a deadline, dispute. Emit events, use checks-effects-interactions
- [ ] Write (30 min): Log: every state the escrow can be in, as a small state diagram
- [ ] Learn (20 min): Read EIP-721  
  [EIP-721](https://eips.ethereum.org/EIPS/eip-721)
- [ ] Learn (15 min): OpenZeppelin ERC-721 docs and the Wizard  
  [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) · [Wizard](https://wizard.openzeppelin.com/)
- [ ] Build (80 min): Build an NFT whose tokenURI returns base64 JSON with an SVG generated in Solidity
- [ ] Write (20 min): Log: what an NFT actually owns, and what lives off-chain in most NFTs
- [ ] Learn (20 min): viem: getting started, reading and writing contracts  
  [viem.sh](https://viem.sh/)
- [ ] Learn (10 min): Scaffold-ETH 2 docs: hooks and deploying  
  [docs.scaffoldeth.io](https://docs.scaffoldeth.io/) · [wagmi](https://wagmi.sh/)
- [ ] Crypto (30 min): EIP-712 typed-data signatures and replay protection. Sign an escrow release off-chain and verify it in Solidity  
  [EIP-712](https://eips.ethereum.org/EIPS/eip-712) · [OpenZeppelin EIP712 utilities](https://docs.openzeppelin.com/contracts/5.x/api/utils#EIP712)
- [ ] Explain (45 min): Explainer #3: write "Replacing a middleman with an escrow contract, and what it can't replace" in blog/ (600–900 words, weeks 5–6). Optional: record a 5-minute video teaching it and link it in the post
- [ ] Apps (30 min): Marketplaces: how on-chain marketplaces work (listings, signed orders, escrow, royalties, disputes). Skim the Seaport contracts and sketch how your escrow and NFT could become a small marketplace  
  [Seaport (OpenSea's marketplace protocol)](https://github.com/ProjectOpenSea/seaport)
- [ ] Write (15 min): Write trust-stack/README.md: the four parts (A provenance, B marketplace, C payment rail, D credentials) in your own words, how they connect, and what 'working and tested' means for each
- [ ] Capstone (30 min): Capstone B: copy your escrow into trust-stack/ as Marketplace.sol. list(batchId, price) is allowed only for sellers with a valid credential (check the mock for now), buyers pay in TestUSD into escrow, and completed trades count as reputation. Test it against the mocks
- [ ] Capstone (30 min): Integration design: write trust-stack/INTERFACES.md and the Solidity interfaces the parts talk through (ICredentialRegistry.isValid(account, role), IProvenance.batchStatus(batchId), IMarketplace.list(batchId, price)), plus mock versions of D and A so the marketplace can be tested against them now
- [ ] Capstone (15 min): Traceability design: in trust-stack/POLICY.md, define a batch's journey (harvested → packed → shipped → received), which role may sign each step (farmer, cooperative, transporter, inspector, buyer), and one product policy, e.g. tomatoes: 2–8 °C, at most 48 h in transit, inspection required
- [ ] Capstone (20 min): Rules to tests: for every rule in your POLICY.md, add a row to TESTING.md with a named test (e.g. test_RevertWhen_TransporterSignsInspection) and write the empty test so CI shows what's still missing
- [ ] Capstone (15 min): Demo stages 2–3 with the mocks: issue roles and list batch 1, so make demo now runs stages 01–03
- [ ] Apps (30 min): NFTs beyond the hype: ERC-1155 (many token types in one contract), the royalty standard EIP-2981 and why marketplaces stopped enforcing royalties, wash trading, and what NFTs are used for now (tickets, credentials, game items, real-world assets). End with a capstone question in your log: should each produce batch be an NFT, or is a record in your trace registry enough?  
  [ethereum.org: NFTs](https://ethereum.org/en/nft/) · [EIP-1155](https://eips.ethereum.org/EIPS/eip-1155) · [EIP-2981: NFT royalties](https://eips.ethereum.org/EIPS/eip-2981)

---

## Objectives and check-yourself

**By the end of this block you can:**

- Write a contract that holds value (escrow) using checks-effects-interactions, with a test for every path
- Explain re-entrancy and show how your escrow avoids it
- Build an ERC-721 whose metadata and image live on-chain
- Sign and verify EIP-712 typed data with replay protection
- Explain how NFT marketplaces use signed orders, escrow and royalties, and what NFTs are really used for today
- Define the trust stack's interfaces, product policy and rules-to-tests table

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. List every state my escrow can be in. Which transitions can only the arbiter trigger?
2. Where exactly would a re-entrancy attack hit my escrow if I sent the money before updating state?
3. What does my NFT actually own, and what would break if its metadata lived on an ordinary web server?
4. What stops an EIP-712 signature being replayed on another chain or another contract?
5. Why did most marketplaces stop enforcing royalties, and what does that say about on-chain rules versus off-chain choices?
6. Should a produce batch be an NFT, or is a record in the trace registry enough? Why?


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
