# Week 01: The mental model, keys and signatures

**Dates:** 28 Sep – 4 Oct 2026 · **Planned time:** 10 h

**Goal:** Understand why hash-linking plus proof-of-work makes history expensive to rewrite, then add real ownership with ECDSA signatures and Merkle roots.

**Ship:** pow_demo.py and Project 0 (toy_chain.py with a tamper test)

### Plan

- [ ] Learn (30 min): Watch 3Blue1Brown's bitcoin video end to end  
  [But how does bitcoin actually work?](https://www.youtube.com/watch?v=bBC-nXj3Ng4)
- [ ] Learn (60 min): Click through all five pages of the blockchain demo: hash, block, blockchain, distributed, tokens  
  [andersbrownworth.com/blockchain](https://andersbrownworth.com/blockchain/)
- [ ] Learn (60 min): Read the Bitcoin whitepaper, sections 1–6. Don't worry about the math yet  
  [bitcoin.pdf](https://bitcoin.org/bitcoin.pdf)
- [ ] Build (30 min): Create the blockchain-learning repo with a README and a /week01 folder
- [ ] Build (90 min): Using Python's hashlib, find a nonce that gives 4 leading hex zeros, then time 5 and 6 zeros  
  [hashlib docs](https://docs.python.org/3/library/hashlib.html)
- [ ] Write (30 min): Log: explain in five sentences why editing one block invalidates every block after it
- [ ] Learn (45 min): Read Cloudflare's primer on elliptic-curve cryptography  
  [A (relatively easy to understand) primer on ECC](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
- [ ] Learn (60 min): Princeton textbook, chapter 1: hash pointers, Merkle trees, digital signatures  
  [Princeton book PDF](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf)
- [ ] Build (150 min): Build Project 0: Block class, SHA-256 linking, adjustable-difficulty PoW, transactions signed with the ecdsa library (SECP256k1), a Merkle root per block, and validate_chain()  
  [python-ecdsa](https://pypi.org/project/ecdsa/)
- [ ] Build (30 min): Tamper test: change one transaction in block 2 and confirm validation fails at the right block
- [ ] Write (15 min): Log: what a signature proves, and what it does not

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
