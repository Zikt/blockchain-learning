---
block: 9
title: DeFi, oracles, rollups and money
topics: amm, rollups, oracles, need-blockchain, stablecoins
plan: week09-amm-and-capstone-spec
---

# Block 9 · DeFi, oracles, rollups and money

How automated market makers work, why oracles are risky, how rollups scale Ethereum, and when a blockchain is worth it.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b09-pre-1 · amm
How does a constant-product AMM such as Uniswap v2 price trades?

- A. With an order book
- B. With a price from an exchange
- C. With the rule x · y = k on its two token reserves
- D. At a fixed price

<details><summary>Answer</summary>

answer: C
why: The price comes from the ratio of the reserves and shifts as trades change them.

</details>

### b09-pre-2 · rollups
What is a rollup?

- A. A faster blockchain unrelated to Ethereum
- B. A mining pool
- C. A wallet
- D. A layer 2 that runs transactions off Ethereum and posts data or proofs back to it

<details><summary>Answer</summary>

answer: D
why: It inherits security from Ethereum, depending on its design.

</details>

### b09-pre-3 · oracles
What does a blockchain oracle do?

- A. Predicts the future
- B. Mines blocks
- C. Brings outside data, such as prices, on-chain
- D. Stores keys

<details><summary>Answer</summary>

answer: C
why: Contracts can't fetch web data themselves.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b09-key-1 · amm
Explain x · y = k. Why does a big trade move the price more in a small pool?

Answer:

### b09-key-2 · amm
What is slippage, and what is impermanent loss?

Answer:

### b09-key-3 · oracles
Why is an AMM's spot price a dangerous oracle? How do Chainlink feeds or time-weighted prices help?

Answer:

### b09-key-4 · rollups
What's the difference between optimistic and zero-knowledge rollups?

Answer:

### b09-key-5 · rollups
What risks does L2BEAT track for a rollup, and what do its "stages" mean?

Answer:

### b09-key-6 · need-blockchain
What questions tell you whether a use case needs a blockchain or a shared database?

Answer:

### b09-key-7 · stablecoins
How are stablecoins used in Sub-Saharan Africa, and why?

Answer:

### b09-key-8 · stablecoins
What do regulators worry about with stablecoins, and what do rules like MiCA and the GENIUS Act require of issuers?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b09-post-1 · amm
A pool holds 100 ETH and 200,000 USDC. Ignoring fees, what's the spot price of ETH?

- A. 200 USDC
- B. 20,000 USDC
- C. 2,000 USDC
- D. 100 USDC

<details><summary>Answer</summary>

answer: C
why: 200,000 ÷ 100 = 2,000 USDC per ETH.

</details>

### b09-post-2 · amm
Why does k never decrease in Uniswap v2 swaps?

- A. Governance fixes k
- B. Liquidity providers top it up
- C. It does decrease
- D. The 0.3% fee stays in the reserves, so k grows slightly with each swap

<details><summary>Answer</summary>

answer: D
why: That's the property your fuzz test checks.

</details>

### b09-post-3 · oracles
An attacker uses a flash loan to skew an AMM's price, then borrows too much from a lending protocol that uses that AMM as its price oracle. What's the fix?

- A. A bigger gas limit
- B. Remove the AMM
- C. Use a manipulation-resistant oracle, such as Chainlink or a time-weighted average price
- D. Pause Ethereum

<details><summary>Answer</summary>

answer: C
why: A spot price can be moved within one transaction. An average over time can't, cheaply.

</details>

### b09-post-4 · rollups
How is invalid state caught in an optimistic rollup?

- A. With fraud proofs during a challenge window
- B. With a validity proof for every batch
- C. By miners
- D. By the bridge operator alone

<details><summary>Answer</summary>

answer: A
why: It's assumed valid unless someone proves otherwise in time.

</details>

### b09-post-5 · rollups
Withdrawing from an optimistic rollup back to Ethereum usually takes about…

- A. Seconds
- B. A year
- C. It's impossible
- D. A week (the challenge period)

<details><summary>Answer</summary>

answer: D
why: Fast-withdrawal services exist, but they're third parties taking on that risk.

</details>

### b09-post-6 · need-blockchain
When is a blockchain most useful?

- A. When one trusted company controls the data anyway
- B. When several parties who don't fully trust each other need a shared record that no single one controls
- C. When you need the fastest possible database
- D. When the data must be secret

<details><summary>Answer</summary>

answer: B
why: If a trusted party already exists, a database is usually simpler and cheaper.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b09-ref-1
What slippage did my tests show for the same trade on a small pool and a large one?

### b09-ref-2
How could an attacker move my AMM's price inside one transaction, and who would lose?

### b09-ref-3
What can Base's operator do to my funds today, according to L2BEAT?

### b09-ref-4
Sending $200 to Nigeria or Rwanda: which route was cheapest, and what costs remain when the recipient cashes out?

### b09-ref-5
For each trust-stack part, what is on-chain, what is off-chain, and why?

### b09-ref-6
What does revoking a credential stop, and what can't it undo?
