---
block: 2
title: Bitcoin: UTXOs, transactions and mining
topics: utxo, mining, transactions, script, security, signatures
plan: week02-bitcoin
---

# Block 2 · Bitcoin: UTXOs, transactions and mining

How Bitcoin tracks ownership without balances, what's inside a transaction, and how mining and difficulty keep the network secure.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b02-pre-1 · utxo
Where is a Bitcoin "balance" stored?

- A. In an account record on every node
- B. In each miner's private database
- C. Nowhere as such: wallets add up the unspent transaction outputs they can spend
- D. On the exchange you bought from

<details><summary>Answer</summary>

answer: C
why: Bitcoin only records outputs. A balance is something your wallet works out.

</details>

### b02-pre-2 · mining
Roughly how often is a new Bitcoin block found?

- A. Every second
- B. About every 10 minutes
- C. Every hour
- D. Once a day

<details><summary>Answer</summary>

answer: B
why: Difficulty adjusts so the average stays near 10 minutes.

</details>

### b02-pre-3 · transactions
What is a Bitcoin transaction fee?

- A. A fixed 1% charge
- B. A payment to the Bitcoin Foundation
- C. The difference between the inputs and the outputs, which the miner collects
- D. Only charged on large transfers

<details><summary>Answer</summary>

answer: C
why: There's no fee field. Whatever the inputs add up to beyond the outputs goes to the miner.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b02-key-1 · utxo
Explain the UTXO model. How is it different from an account balance?

Answer:

### b02-key-2 · transactions
What are a transaction's inputs and outputs, and why do most payments create a change output?

Answer:

### b02-key-3 · script
What do the locking script and the unlocking script (or witness) do in a P2PKH or P2WPKH payment?

Answer:

### b02-key-4 · transactions
Where is the fee in a Bitcoin transaction, and who receives it?

Answer:

### b02-key-5 · mining
Why can't newly mined coins be spent until 100 blocks later?

Answer:

### b02-key-6 · mining
How does difficulty retargeting keep block times near 10 minutes?

Answer:

### b02-key-7 · security
What can an attacker with 51% of the hash power do, and what can't they do?

Answer:

### b02-key-8 · signatures
What do Schnorr signatures and Taproot add compared with ECDSA?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b02-post-1 · utxo
Alice has one UTXO worth 1 BTC. She pays Bob 0.3 BTC with a 0.001 BTC fee. Her transaction's outputs are…

- A. One output of 0.3 BTC to Bob
- B. 0.3 BTC to Bob and 0.699 BTC back to Alice as change
- C. 0.3 BTC to Bob and 0.7 BTC to the miner
- D. 0.301 BTC to Bob

<details><summary>Answer</summary>

answer: B
why: The input must be spent in full. 1 − 0.3 − 0.001 = 0.699 comes back as change, and the missing 0.001 is the fee.

</details>

### b02-post-2 · mining
How often does Bitcoin adjust its difficulty?

- A. Every block
- B. Every 2,016 blocks, about two weeks
- C. Every 210,000 blocks
- D. Once a year

<details><summary>Answer</summary>

answer: B
why: 210,000 blocks is the halving interval, not the difficulty period.

</details>

### b02-post-3 · security
What can an attacker with 51% of the hash power do?

- A. Spend coins from any address
- B. Create unlimited new bitcoin
- C. Change the 21 million cap
- D. Reverse their own recent payments (double-spend) and censor transactions

<details><summary>Answer</summary>

answer: D
why: They can reorder history, but they can't forge signatures or break consensus rules that every node checks.

</details>

### b02-post-4 · script
In a P2PKH payment, what does the unlocking data provide?

- A. The recipient's address
- B. The miner's nonce
- C. A signature, plus the public key that matches the hash in the locking script
- D. The block hash

<details><summary>Answer</summary>

answer: C
why: The locking script checks that the public key hashes to the stored value and that the signature is valid for it.

</details>

### b02-post-5 · mining
Why is "the longest chain" really "the chain with the most work"?

- A. Nodes only count blocks
- B. To save storage
- C. An attacker could make many easy blocks, so nodes follow the most cumulative proof-of-work
- D. Miners vote on it

<details><summary>Answer</summary>

answer: C
why: Counting blocks could be gamed with low-difficulty blocks. Total work can't be faked.

</details>

### b02-post-6 · transactions
Why do newly created coins (coinbase outputs) wait 100 blocks before they can be spent?

- A. It's a tax rule
- B. The miner must sign twice
- C. The network needs to see the fee first
- D. A reorganisation could remove the block that created them

<details><summary>Answer</summary>

answer: D
why: If the block were orphaned, those coins would vanish, along with anything spent from them.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b02-ref-1
Where is "my balance" actually stored, and how does a wallet work it out?

### b02-ref-2
In my raw transaction, which script locks the output and which one unlocks it?

### b02-ref-3
Why did I have to mine 101 blocks before I could spend anything?

### b02-ref-4
What can a 51% attacker do to recent transactions, and why can't they take my coins?

### b02-ref-5
Where is the fee in my transaction? (It isn't a field.)

### b02-ref-6
If half the miners switched off tomorrow, what would happen to block times, and for how long?
