# Week 02: Bitcoin: UTXOs, raw transactions and mining

**Dates:** 5 Oct – 11 Oct 2026 · **Planned time:** 10 h

**Goal:** Run your own node, see that Bitcoin has no balances, and build and decode a transaction by hand.

**Ship:** A regtest node, a UTXO version of your toy chain, and raw_tx.py with a decoded transaction

### Plan

- [ ] Learn (75 min): Mastering Bitcoin: the 'Introduction' and 'How Bitcoin Works' chapters  
  [bitcoinbook on GitHub](https://github.com/bitcoinbook/bitcoinbook)
- [ ] Learn (45 min): learnmeabitcoin: the transaction and UTXO pages  
  [learnmeabitcoin technical](https://learnmeabitcoin.com/technical/)
- [ ] Build (90 min): Install Bitcoin Core, start it with -regtest, mine 101 blocks, send coins to a second address with bitcoin-cli  
  [Bitcoin Core download](https://bitcoincore.org/en/download/) · [Bitcoin developer examples (regtest)](https://developer.bitcoin.org/examples/testing.html)
- [ ] Build (60 min): Change your toy chain to UTXOs: inputs reference earlier outputs, and double spends are rejected
- [ ] Learn (60 min): Mastering Bitcoin: the 'Keys and Addresses' and 'Transactions' chapters  
  [bitcoinbook on GitHub](https://github.com/bitcoinbook/bitcoinbook)
- [ ] Learn (30 min): learnmeabitcoin: Script, P2PKH and P2WPKH  
  [learnmeabitcoin technical](https://learnmeabitcoin.com/technical/)
- [ ] Build (120 min): With python-bitcoinlib, build, sign and broadcast a raw transaction on regtest, then run decoderawtransaction on it  
  [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib)
- [ ] Learn (60 min): Mastering Bitcoin: the mining and consensus chapter  
  [bitcoinbook on GitHub](https://github.com/bitcoinbook/bitcoinbook)
- [ ] Learn (45 min): Re-read the whitepaper, sections 7–11, including the attacker probability calculation  
  [bitcoin.pdf](https://bitcoin.org/bitcoin.pdf)
- [ ] Write (15 min): Log: what the locking and unlocking scripts did in your transaction, and why a 51% attacker still can't steal coins

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
