---
block: 7
title: Frontends, storage and breaking contracts
topics: frontend, storage, vulnerabilities, tooling, invariants, identity
plan: week07-dapp-and-security
---

# Block 7 · Frontends, storage and breaking contracts

Connecting a website to contracts, common vulnerability classes, testing tools, and decentralised storage and naming.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b07-pre-1 · frontend
How does a dApp frontend talk to the blockchain?

- A. Through a central database
- B. Through a wallet and an RPC node (JSON-RPC)
- C. By email
- D. By FTP

<details><summary>Answer</summary>

answer: B
why: The wallet signs, and the RPC node reads state and broadcasts transactions.

</details>

### b07-pre-2 · storage
How does IPFS find files?

- A. By their location (a URL)
- B. By a hash of their content (a CID)
- C. By file name
- D. By owner

<details><summary>Answer</summary>

answer: B
why: Content addressing: the same content always has the same CID.

</details>

### b07-pre-3 · vulnerabilities
What happens to an integer overflow in Solidity 0.8 and later?

- A. It silently wraps around
- B. It reverts by default, unless the code is in an unchecked block
- C. It's impossible to test
- D. It only happens on L2

<details><summary>Answer</summary>

answer: B
why: Before 0.8, overflows wrapped silently, which caused many bugs.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b07-key-1 · frontend
What happens between clicking "Buy" in a dApp and the transaction being included in a block?

Answer:

### b07-key-2 · frontend
Why must a frontend never be relied on for security, even if it hides buttons?

Answer:

### b07-key-3 · vulnerabilities
Name four common smart-contract vulnerability classes and one defence for each.

Answer:

### b07-key-4 · tooling
What is Slither good at finding, and why does it report false positives?

Answer:

### b07-key-5 · invariants
What is an invariant test, and what invariant should always hold for an escrow?

Answer:

### b07-key-6 · storage
What does an IPFS CID guarantee, and what doesn't it guarantee?

Answer:

### b07-key-7 · identity
What does ENS do, and what problem does it solve for users?

Answer:

### b07-key-8 · identity
What is Sign-In with Ethereum (EIP-4361), and when do you actually need it?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b07-post-1 · vulnerabilities
Why is `tx.origin == owner` a dangerous access check?

- A. A malicious contract the owner interacts with can call your contract and pass the check
- B. tx.origin is always zero
- C. It costs too much gas
- D. It only works on testnets

<details><summary>Answer</summary>

answer: A
why: tx.origin is the original sender, not the immediate caller. Use msg.sender.

</details>

### b07-post-2 · vulnerabilities
A lottery picks winners with `block.timestamp % 2 == 0`. What's wrong?

- A. Timestamps are always even
- B. The outcome can be predicted before the block exists, and the block proposer can choose not to publish a block with a result they dislike
- C. Solidity forbids it
- D. It reverts

<details><summary>Answer</summary>

answer: B
why: Block data is public and predictable, and proposers can withhold blocks. Use a verifiable random function (VRF) instead.

</details>

### b07-post-3 · invariants
Which is a good invariant for a token?

- A. Every balance is non-zero
- B. The owner always has the most tokens
- C. Gas use is constant
- D. totalSupply equals the sum of all balances

<details><summary>Answer</summary>

answer: D
why: It must hold after any sequence of calls, which is exactly what invariant tests check.

</details>

### b07-post-4 · storage
If nobody pins a file on IPFS…

- A. It stays available forever
- B. It can disappear, even though its CID still refers to that exact content
- C. It moves to Ethereum
- D. Its CID changes

<details><summary>Answer</summary>

answer: B
why: A CID guarantees integrity, not availability. Someone has to keep hosting the file.

</details>

### b07-post-5 · identity
What do ENS names map?

- A. Human-readable names like alice.eth to addresses and other records
- B. Emails to wallets
- C. Blocks to miners
- D. Only IP addresses to domains

<details><summary>Answer</summary>

answer: A
why: It works like DNS for Ethereum: easier to read, and harder to mistype.

</details>

### b07-post-6 · frontend
What does hiding an Admin button in the frontend achieve?

- A. It's enough security
- B. It encrypts the function
- C. It prevents direct contract calls
- D. It only tidies the page. The contract must check roles on-chain

<details><summary>Answer</summary>

answer: D
why: Anyone can call a contract directly, without your website.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b07-ref-1
What happens, step by step, between clicking "Buy" and the transaction being mined?

### b07-ref-2
For each Ethernaut level I solved, what was the bug in one line?

### b07-ref-3
Which Slither findings were real, and why were the others noise?

### b07-ref-4
What must always be true of my escrow, and how does the invariant test try to break it?

### b07-ref-5
What does an IPFS CID guarantee, and what doesn't it guarantee?

### b07-ref-6
Could a stranger run my demo in Codespaces without asking me anything?
