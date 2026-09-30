---
block: 5
title: Tokens, Foundry and stablecoins
topics: erc20, stablecoins, testing, deployment
plan: week05-erc20
---

# Block 5 · Tokens, Foundry and stablecoins

Writing and testing an ERC-20 token, deploying and verifying it, and how stablecoins hold (or lose) their peg.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b05-pre-1 · erc20
What is an ERC-20 token?

- A. A separate blockchain
- B. A smart contract that keeps balances and follows a standard interface (transfer, approve and so on)
- C. An NFT
- D. A wallet

<details><summary>Answer</summary>

answer: B
why: The standard interface lets any wallet or exchange work with any token.

</details>

### b05-pre-2 · stablecoins
What does a stablecoin try to do?

- A. Grow in value
- B. Replace Ether
- C. Stay at a fixed value, usually $1
- D. Pay interest

<details><summary>Answer</summary>

answer: C
why: It's pegged to a reference asset, usually the US dollar.

</details>

### b05-pre-3 · testing
What does a fuzz test do?

- A. Checks spelling
- B. Only measures gas
- C. Tests the frontend
- D. Runs your test with many random inputs to find cases that break a property

<details><summary>Answer</summary>

answer: D
why: Instead of hand-picked examples, the fuzzer searches for counterexamples.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b05-key-1 · erc20
What do approve and transferFrom let a spender do? What is the known approval race condition?

Answer:

### b05-key-2 · erc20
Why do tokens have a decimals setting, and what goes wrong when two tokens use different decimals?

Answer:

### b05-key-3 · testing
What makes a good property for a fuzz test? Give one for an ERC-20.

Answer:

### b05-key-4 · deployment
What does verifying a contract on Etherscan prove, and why does it matter?

Answer:

### b05-key-5 · erc20
What does OpenZeppelin's ERC20 handle that a minimal hand-written token often misses?

Answer:

### b05-key-6 · stablecoins
How do fiat-backed, crypto-collateralised and algorithmic stablecoins each try to hold $1?

Answer:

### b05-key-7 · stablecoins
Why did TerraUST collapse in May 2022?

Answer:

### b05-key-8 · stablecoins
Why did USDC briefly lose its peg in March 2023, and why did it recover?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b05-post-1 · erc20
Alice approves a spender for 100 tokens, then sends a transaction changing it to 50. The spender front-runs the change. What's the worst case?

- A. They spend nothing
- B. They spend 50
- C. The transaction fails
- D. They spend 100, then another 50: 150 in total

<details><summary>Answer</summary>

answer: D
why: That's the approval race. The fix is to set the allowance to 0 first, or to use increase/decrease functions or permits.

</details>

### b05-post-2 · erc20
A token with 6 decimals stores "1.5 tokens" as…

- A. 1.5
- B. 1500000
- C. 15
- D. 150

<details><summary>Answer</summary>

answer: B
why: 1.5 × 10⁶ = 1,500,000. Contracts only store whole numbers.

</details>

### b05-post-3 · stablecoins
What mainly keeps USDC and USDT at $1?

- A. An algorithm mints and burns them
- B. They're backed by ETH
- C. The issuer holds reserves (cash and Treasury bills) and redeems tokens for dollars
- D. Miners enforce the price

<details><summary>Answer</summary>

answer: C
why: Fiat-backed coins depend on reserves and redemption, so trust in the issuer matters.

</details>

### b05-post-4 · stablecoins
What mainly backs DAI (and its successor USDS)?

- A. A bank account
- B. Gold
- C. Collateral locked in smart contracts: crypto, plus other stablecoins and real-world assets, with volatile crypto worth more than the coins it backs
- D. Nothing

<details><summary>Answer</summary>

answer: C
why: Volatile collateral is over-collateralised and liquidated automatically if it falls. A large share is now backed by USDC and tokenised Treasury bills.

</details>

### b05-post-5 · stablecoins
Why did TerraUST fail?

- A. Its reserves were stolen
- B. A hacker broke the code
- C. Regulators shut it down
- D. Its peg relied on minting LUNA. When confidence fell, redemptions minted huge amounts of LUNA and crashed its price in a spiral

<details><summary>Answer</summary>

answer: D
why: An algorithmic peg backed only by its own sister token can't survive a loss of confidence.

</details>

### b05-post-6 · testing
A fuzz test checks that `transfer` never changes totalSupply. What kind of check is this?

- A. A property (invariant) that must hold for all inputs
- B. A unit test with fixed inputs
- C. A gas benchmark
- D. A deployment script

<details><summary>Answer</summary>

answer: A
why: Properties that must always hold are the most valuable things to fuzz.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b05-ref-1
What does approve plus transferFrom let a spender do, and what is the known approval race?

### b05-ref-2
What did my fuzz tests find, or why did they find nothing, and what would be a stronger property to test?

### b05-ref-3
Why does TestUSD use 6 decimals, and what goes wrong when two tokens' decimals differ?

### b05-ref-4
What would have to back TestUSD for it to be a real stablecoin?

### b05-ref-5
Why did UST collapse for good while USDC got its peg back?

### b05-ref-6
Is the Trust stack workflow green, and can I say what each job checks?
