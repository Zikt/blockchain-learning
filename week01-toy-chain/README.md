<!-- NAV:START -->
[↑ Overview](../README.md) · [Week 02 →](../week02-bitcoin/)
<!-- NAV:END -->

# Week 01: The mental model, keys and signatures

**Dates:** 28 Sep – 4 Oct 2026 · **Planned time:** 10 h

**Goal:** Understand why hash-linking plus proof-of-work makes history expensive to rewrite, then add real ownership with ECDSA signatures and Merkle roots.

**Ship:** pow_demo.py and Project 0 (toy_chain.py with a tamper test)

### Plan

- [x] Learn (30 min): Watch 3Blue1Brown's bitcoin video end to end  
  [But how does bitcoin actually work?](https://www.youtube.com/watch?v=bBC-nXj3Ng4)
- [x] Learn (45 min): Click through all five pages of the blockchain demo: hash, block, blockchain, distributed, tokens  
  [andersbrownworth.com/blockchain](https://andersbrownworth.com/blockchain/)
- [ ] Learn (45 min): Read the Bitcoin whitepaper, sections 1–6. Don't worry about the math yet  
  [bitcoin.pdf](https://bitcoin.org/bitcoin.pdf)
- [ ] Build (30 min): Create the blockchain-learning repo with a README and a /week01 folder
- [ ] Build (90 min): Using Python's hashlib, find a nonce that gives 4 leading hex zeros, then time 5 and 6 zeros  
  [hashlib docs](https://docs.python.org/3/library/hashlib.html)
- [ ] Write (30 min): Log: explain in five sentences why editing one block invalidates every block after it
- [ ] Learn (45 min): Read Cloudflare's primer on elliptic-curve cryptography  
  [A (relatively easy to understand) primer on ECC](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
- [ ] Learn (45 min): Princeton textbook, chapter 1: hash pointers, Merkle trees, digital signatures  
  [Princeton book PDF](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf)
- [ ] Build (150 min): Build Project 0: Block class, SHA-256 linking, adjustable-difficulty PoW, transactions signed with the ecdsa library (SECP256k1), a Merkle root per block, and validate_chain()  
  [python-ecdsa](https://pypi.org/project/ecdsa/)
- [ ] Build (30 min): Tamper test: change one transaction in block 2 and confirm validation fails at the right block
- [ ] Write (15 min): Log: what a signature proves, and what it does not
- [ ] Crypto (30 min): The three security properties of hash functions (preimage, second-preimage and collision resistance), and which one proof-of-work relies on  
  [A Graduate Course in Applied Cryptography (Boneh & Shoup, free)](https://toc.cryptobook.us/) · [Cryptography I (Dan Boneh, Coursera)](https://www.coursera.org/learn/crypto)
- [ ] AI (15 min): Ask an LLM to explain proof-of-work, then use the whitepaper to find one thing it got wrong or oversimplified. Note it in your log

---

## Objectives and check-yourself

**By the end of this block you can:**

- Explain how hash pointers link blocks, and why editing one block breaks every block after it
- Explain what proof-of-work costs an attacker, and measure how the work grows with each extra leading zero
- Sign and verify a transaction on secp256k1, and say what a signature proves and what it doesn't
- Build a Merkle root and explain how it proves one transaction is in a block

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. If I change one transaction in block 2 of 10, which check fails first, and why do all later blocks fail too?
2. Each extra leading hex zero multiplies the expected work by how much? What did my timings show?
3. Which hash property (preimage, second-preimage or collision resistance) does proof-of-work rely on, and why that one?
4. What exactly does a valid signature prove? Name one thing it doesn't prove.
5. How many hashes do I need to prove one transaction is in a block of 1,024 transactions?
6. Can I explain the chain to a non-technical friend in two minutes, without notes?


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
