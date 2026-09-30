---
block: 10
title: Hardware that signs its own data
topics: custody, device-signing, anchoring, tee, merkle-batching
plan: week10-11-capstone
---

# Block 10 · Hardware that signs its own data

How keys are protected in hardware, how a sensor can sign its readings, and what anchoring data on-chain does and doesn't prove.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b10-pre-1 · custody
How does a hardware wallet protect keys?

- A. It stores them in the cloud
- B. It prints them
- C. It emails them
- D. It keeps the private key on the device and signs there, so the key never touches your computer

<details><summary>Answer</summary>

answer: D
why: Even malware on your laptop can't read the key.

</details>

### b10-pre-2 · device-signing
What does `ecrecover` in Solidity return?

- A. The private key
- B. The message
- C. The block number
- D. The address that signed a message hash, given the signature

<details><summary>Answer</summary>

answer: D
why: Compare that address with the one you expect.

</details>

### b10-pre-3 · anchoring
What does anchoring data on a blockchain usually mean?

- A. Storing all the raw data on-chain
- B. Encrypting it
- C. Posting a hash or Merkle root of the data, so it can later be proven unchanged
- D. Deleting it

<details><summary>Answer</summary>

answer: C
why: You get tamper-evidence cheaply, without putting the data itself on-chain.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b10-key-1 · custody
How do hardware wallets and secure elements protect private keys, and how can they still fail?

Answer:

### b10-key-2 · tee
What is a trusted execution environment, and what did SGX.Fail show about relying on one?

Answer:

### b10-key-3 · device-signing
How can a sensor sign its readings, and how does a contract check the signature?

Answer:

### b10-key-4 · merkle-batching
Why sign and anchor a Merkle root of many readings instead of each reading?

Answer:

### b10-key-5 · anchoring
What does anchoring a signed reading prove, and what can't it prove?

Answer:

### b10-key-6 · anchoring
How does OpenTimestamps anchor many documents with a single Bitcoin transaction?

Answer:

### b10-key-7 · device-signing
How do you register devices on-chain, and what should happen if a device's key is stolen?

Answer:

### b10-key-8 · device-signing
What are test vectors, and why use them to check firmware against a contract?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b10-post-1 · merkle-batching
1,000 readings are anchored as one Merkle root. What do you need to prove one reading later?

- A. The reading plus about 10 sibling hashes (its Merkle proof)
- B. All 1,000 readings
- C. The private key
- D. Nothing

<details><summary>Answer</summary>

answer: A
why: log₂(1,000) ≈ 10 levels, so about 10 hashes.

</details>

### b10-post-2 · anchoring
A sensor sitting in ice honestly signs "2 °C" while the produce is warm. What does the system prove?

- A. It detects the fraud automatically
- B. It rejects the reading
- C. That the device signed that value, but it can't tell that the reading is misleading
- D. It slashes the device

<details><summary>Answer</summary>

answer: C
why: Signatures prove who said something, not that it's true. Physical tamper resistance and inspections cover the rest.

</details>

### b10-post-3 · device-signing
A contract accepts a reading if ecrecover(hash, sig) equals a registered device address. An attacker changes one digit of the reading. What happens?

- A. It's accepted
- B. The recovered address changes, so the reading is rejected
- C. The device is deleted
- D. Gas is refunded

<details><summary>Answer</summary>

answer: B
why: A different message gives a different hash, and that recovers an unrelated address.

</details>

### b10-post-4 · custody
What's the main weakness of keeping a device key in an ordinary ESP32's flash memory?

- A. It's too slow
- B. It uses too much power
- C. Someone with physical access can often read the flash and extract the key
- D. It can't do ECDSA

<details><summary>Answer</summary>

answer: C
why: Flash encryption or a secure element such as the ATECC608A makes extraction much harder.

</details>

### b10-post-5 · tee
What does SGX.Fail document?

- A. Intel SGX enclaves have been broken repeatedly by side-channel and other attacks, so they shouldn't be the only line of defence
- B. TEEs are unbreakable
- C. SGX is only for games
- D. TEEs replace blockchains

<details><summary>Answer</summary>

answer: A
why: Treat a TEE as one layer of defence, not a guarantee.

</details>

### b10-post-6 · anchoring
Why anchor many batches on an L2 like Base rather than on Ethereum mainnet?

- A. An L2 is more secure than mainnet
- B. It's private
- C. Far lower fees, while still settling to Ethereum
- D. There's no reason to

<details><summary>Answer</summary>

answer: C
why: Security comes from settling to Ethereum, and the cost per anchor falls a lot.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b10-ref-1
Where does my ESP32's private key live, and how could someone holding the board extract it?

### b10-ref-2
Why sign a Merkle root instead of every reading? What does that save on-chain?

### b10-ref-3
Does my firmware reproduce test_vectors.json byte for byte? If not, where do the bytes differ?

### b10-ref-4
What does ecrecover return for a tampered reading, and how does my contract reject it?

### b10-ref-5
A sensor sitting in ice honestly signs "2 °C" while the tomatoes are warm. What does my system prove, and what does it miss?

### b10-ref-6
How does OpenTimestamps anchor millions of hashes with one transaction?
