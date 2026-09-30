---
block: 4
title: Ethereum, your first contracts, and what web3 claims
topics: accounts, gas, wallets, solidity, web3
plan: week04-first-contracts
---

# Block 4 · Ethereum, your first contracts, and what web3 claims

Accounts, gas and the EVM, writing Solidity, wallets and exchanges, and a clear-eyed look at web3.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b04-pre-1 · accounts
What does Ethereum keep track of?

- A. Unspent outputs, like Bitcoin
- B. Only token balances
- C. Nothing: it's stateless
- D. Accounts with balances, and for contracts, code and storage

<details><summary>Answer</summary>

answer: D
why: Ethereum is account-based: its global state maps addresses to accounts.

</details>

### b04-pre-2 · gas
What is gas in Ethereum?

- A. The price of ETH
- B. A fee paid to the Ethereum Foundation
- C. A unit of computation: you pay gas used × gas price
- D. Something only contracts pay

<details><summary>Answer</summary>

answer: C
why: Gas measures work, so every operation has a cost and infinite loops can't stall the network.

</details>

### b04-pre-3 · wallets
What does "not your keys, not your coins" mean?

- A. If someone else holds your private keys, such as an exchange, you depend on them to get your funds
- B. You need keys to mine
- C. You must memorise your keys
- D. Coins are stored inside the key

<details><summary>Answer</summary>

answer: A
why: Whoever controls the key controls the funds.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b04-key-1 · accounts
What's the difference between an externally owned account and a contract account?

Answer:

### b04-key-2 · gas
Why does a transaction that reverts still cost gas?

Answer:

### b04-key-3 · solidity
What's the difference between storage, memory and calldata in Solidity, and which costs the most?

Answer:

### b04-key-4 · accounts
How is an Ethereum address derived from a private key?

Answer:

### b04-key-5 · solidity
What are events for, and why are they cheaper than storing the same data?

Answer:

### b04-key-6 · solidity
What do modifiers and custom errors do? Why are custom errors cheaper than revert strings?

Answer:

### b04-key-7 · wallets
Compare a custodial exchange wallet, a self-custody wallet and a DEX. Who can move your funds in each?

Answer:

### b04-key-8 · web3
What does "web3" claim to offer, and what is the strongest criticism of those claims?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b04-post-1 · accounts
An Ethereum address is…

- A. The last 20 bytes of the Keccak-256 hash of the public key
- B. The public key itself
- C. A SHA-256 hash of the private key
- D. A name the user chooses

<details><summary>Answer</summary>

answer: A
why: Hash the 64-byte public key with Keccak-256 and keep the last 20 bytes.

</details>

### b04-post-2 · gas
A transaction runs out of gas halfway through. What happens?

- A. Changes made up to that point are kept
- B. Nothing is charged
- C. All its state changes are reverted, and the whole gas limit is still paid
- D. The validator refunds it

<details><summary>Answer</summary>

answer: C
why: The work was done, so it's paid for: running out of gas uses up the entire gas limit. The state is left as if the transaction never ran.

</details>

### b04-post-3 · solidity
Which of these is the most expensive to write?

- A. A storage variable
- B. A memory variable
- C. Calldata
- D. A constant

<details><summary>Answer</summary>

answer: A
why: Storage persists on-chain for every node. Writing a new slot costs about 20,000 gas.

</details>

### b04-post-4 · solidity
Given `mapping(address => uint256) balances;`, what does `balances[x]` return for an address that was never written?

- A. An error
- B. 0
- C. null
- D. The address

<details><summary>Answer</summary>

answer: B
why: Every key in a mapping exists and holds the default value until it's written.

</details>

### b04-post-5 · wallets
What did the FTX collapse in 2022 show?

- A. Customers of a custodial exchange can lose their funds if the exchange misuses them
- B. Self-custody wallets are unsafe
- C. DEXs are illegal
- D. Ethereum was hacked

<details><summary>Answer</summary>

answer: A
why: FTX held customers' keys and used their funds. Those without self-custody were left as creditors.

</details>

### b04-post-6 · web3
Moxie Marlinspike's critique of web3 pointed out that most "decentralised" apps…

- A. Ran their own nodes
- B. Relied on a few centralised providers, such as Infura and Alchemy for APIs and OpenSea for NFTs
- C. Used Bitcoin
- D. Had no users

<details><summary>Answer</summary>

answer: B
why: Users talked to the chain through a handful of companies, which brought back central points of control.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b04-ref-1
How does an Ethereum account differ from a Bitcoin UTXO?

### b04-ref-2
Why does a failed transaction still cost gas?

### b04-ref-3
What is the difference between storage and memory, and which costs more?

### b04-ref-4
From memory: how do I get from a private key to an address?

### b04-ref-5
What did the FTX collapse show about "not your keys, not your coins"?

### b04-ref-6
Which web3 claims will this plan let me test myself, and what do I think of them today?
