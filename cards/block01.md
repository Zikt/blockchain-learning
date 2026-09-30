---
block: 1
title: Hashes, chains and proof-of-work
topics: hashing, chain-structure, signatures, proof-of-work, merkle-trees
plan: week01-toy-chain
---

# Block 1 · Hashes, chains and proof-of-work

How a chain of hashes makes history hard to change, how signatures prove who sent something, and how Merkle trees prove what's in a block.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b01-pre-1 · hashing
What does a cryptographic hash function produce?

- A. A fixed-size fingerprint that changes unpredictably when the input changes
- B. An encrypted copy you can decrypt with a key
- C. A compressed copy you can decompress
- D. A random number unrelated to the input

<details><summary>Answer</summary>

answer: A
why: A hash is one-way and fixed-size. There's no key, and you can't get the input back from it.

</details>

### b01-pre-2 · chain-structure
What does each block in a blockchain contain that links it to the chain?

- A. The hash of the previous block
- B. A copy of every earlier block
- C. The private keys of its miners
- D. A timestamp signed by a bank

<details><summary>Answer</summary>

answer: A
why: Storing the previous block's hash is what makes it a chain: change an old block and the link breaks.

</details>

### b01-pre-3 · signatures
A digital signature lets anyone check that…

- A. The message is true
- B. The message is secret
- C. The sender is a real person
- D. A message came from the holder of a specific private key and wasn't changed

<details><summary>Answer</summary>

answer: D
why: A signature proves key ownership and integrity. It says nothing about truth, secrecy or identity.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b01-key-1 · chain-structure
Why does changing one transaction in an old block invalidate every block after it?

Answer:

### b01-key-2 · proof-of-work
What is proof-of-work, and what does it cost someone who wants to rewrite history?

Answer:

### b01-key-3 · proof-of-work
Each extra leading zero hex digit in a hash target multiplies the expected work by how much, and why?

Answer:

### b01-key-4 · hashing
Name the three security properties of a cryptographic hash function. Which one does proof-of-work rely on?

Answer:

### b01-key-5 · signatures
What does a valid ECDSA signature prove, and what doesn't it prove?

Answer:

### b01-key-6 · signatures
How are a private key, a public key and an address related? Which direction is easy to compute, and which is infeasible?

Answer:

### b01-key-7 · merkle-trees
What is a Merkle root, and how does a Merkle proof show that one transaction is in a block?

Answer:

### b01-key-8 · merkle-trees
How many hashes are in a Merkle proof for one transaction among 1,024? Why?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b01-post-1 · proof-of-work
A miner looks for a nonce that makes the block hash fall below a target. Lowering the target…

- A. Makes blocks harder to find, so more work is expected
- B. Makes blocks easier to find
- C. Changes nothing about difficulty
- D. Makes blocks smaller

<details><summary>Answer</summary>

answer: A
why: A lower target means fewer possible hashes qualify, so on average more attempts are needed.

</details>

### b01-post-2 · hashing
Which property means it's infeasible to find any two different inputs with the same hash?

- A. Preimage resistance
- B. Second-preimage resistance
- C. Determinism
- D. Collision resistance

<details><summary>Answer</summary>

answer: D
why: Collision resistance is about any pair. Second-preimage resistance is about matching one given input.

</details>

### b01-post-3 · chain-structure
An attacker edits a transaction in block 5 of a 100-block chain. To make the chain valid again they must…

- A. Re-sign block 5 only
- B. Change the genesis block
- C. Redo the proof-of-work for block 5 and every block after it
- D. Nothing, because hashes don't cover transactions

<details><summary>Answer</summary>

answer: C
why: Block 5's hash changes, which breaks block 6's link, and so on to the tip. Every one needs new proof-of-work.

</details>

### b01-post-4 · merkle-trees
A Merkle proof for one transaction among n transactions needs about how many hashes?

- A. n
- B. n / 2
- C. log₂(n)
- D. 1

<details><summary>Answer</summary>

answer: C
why: You need one sibling hash per level of the tree, and a tree over n leaves has about log₂(n) levels.

</details>

### b01-post-5 · signatures
Alice signs "pay Bob 5". Mallory changes it to "pay Bob 50". What happens when someone verifies it with Alice's public key?

- A. It passes, because the key is Alice's
- B. It passes if Mallory re-hashes the message
- C. It fails, because the signature covers the exact message
- D. It depends on the miner

<details><summary>Answer</summary>

answer: C
why: The signature is over the hash of the original message. Any change produces a different hash, so verification fails.

</details>

### b01-post-6 · proof-of-work
Why does proof-of-work make history expensive to rewrite, rather than impossible?

- A. Hashes can be reversed with enough money
- B. Miners vote to reject edits
- C. An attacker with enough hash power could redo the work, and the cost grows with every block added on top
- D. Signatures expire

<details><summary>Answer</summary>

answer: C
why: Security is economic: rewriting needs more work than the honest network adds, which becomes very expensive the deeper the block.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b01-ref-1
If I change one transaction in block 2 of 10, which check fails first, and why do all later blocks fail too?

### b01-ref-2
Each extra leading hex zero multiplies the expected work by how much? What did my timings show?

### b01-ref-3
Which hash property (preimage, second-preimage or collision resistance) does proof-of-work rely on, and why that one?

### b01-ref-4
What exactly does a valid signature prove? Name one thing it doesn't prove.

### b01-ref-5
How many hashes do I need to prove one transaction is in a block of 1,024 transactions?

### b01-ref-6
Can I explain the chain to a non-technical friend in two minutes, without notes?
