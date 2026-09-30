---
block: 3
title: Consensus: how strangers agree
topics: consensus, pos, nakamoto, byzantine, finality, governance
plan: week03-consensus-sim
---

# Block 3 · Consensus: how strangers agree

The consensus problem, how Nakamoto consensus and proof-of-stake solve it, and where each breaks.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b03-pre-1 · consensus
What core problem do blockchains solve?

- A. Storing data cheaply
- B. Encrypting messages
- C. Making payments faster
- D. Getting many computers that don't trust each other to agree on one ordered history

<details><summary>Answer</summary>

answer: D
why: Everything else, from tokens to contracts, depends on first agreeing on the order of events.

</details>

### b03-pre-2 · pos
In proof-of-stake, what replaces mining power?

- A. Electricity
- B. Locked-up coins (stake) that can be destroyed for cheating
- C. Votes by users
- D. A central server

<details><summary>Answer</summary>

answer: B
why: Validators put capital at risk instead of spending energy.

</details>

### b03-pre-3 · nakamoto
A temporary fork happens when…

- A. Someone copies the code
- B. Two valid blocks are found at about the same time and nodes briefly disagree on the tip
- C. A node crashes
- D. A transaction fails

<details><summary>Answer</summary>

answer: B
why: It resolves when the next block extends one side, which then has more work.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b03-key-1 · consensus
What are safety and liveness in a consensus protocol? Give an example of each one failing.

Answer:

### b03-key-2 · byzantine
What is a Byzantine fault, and why do classic protocols tolerate fewer than one third of nodes being faulty?

Answer:

### b03-key-3 · nakamoto
How does Nakamoto consensus work without a list of known participants?

Answer:

### b03-key-4 · nakamoto
Why do longer network delays lead to more forks?

Answer:

### b03-key-5 · nakamoto
What does selfish mining show about the "honest majority" assumption?

Answer:

### b03-key-6 · pos
How does proof-of-stake stop someone creating thousands of fake identities (a Sybil attack)?

Answer:

### b03-key-7 · finality
What does "finality" mean in Ethereum, and what is slashing?

Answer:

### b03-key-8 · governance
How were Bitcoin's block-size dispute and Ethereum's DAO fork resolved, and what do they say about "code is law"?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b03-post-1 · byzantine
Classic Byzantine agreement protocols such as PBFT tolerate up to how many faulty nodes out of n?

- A. Fewer than n / 2
- B. Any number
- C. Exactly one
- D. Fewer than n / 3

<details><summary>Answer</summary>

answer: D
why: With n ≥ 3f + 1, honest nodes can still outvote conflicting messages from f faulty ones.

</details>

### b03-post-2 · consensus
A network splits in half, and each half keeps producing blocks. When it reconnects, which property has been hurt?

- A. Liveness only
- B. Neither
- C. Confidentiality
- D. Safety: blocks that one side treated as confirmed get reorganised away

<details><summary>Answer</summary>

answer: D
why: Both halves stayed live, but one side's history is thrown out, so earlier "confirmations" didn't hold.

</details>

### b03-post-3 · pos
An Ethereum validator signs two conflicting blocks for the same slot. What happens?

- A. It earns a bonus
- B. It's ignored
- C. It becomes the next proposer
- D. It is slashed: part of its stake is destroyed and it is removed

<details><summary>Answer</summary>

answer: D
why: Slashing makes equivocation provably costly.

</details>

### b03-post-4 · finality
Under normal conditions, roughly how long does Ethereum take to finalise a block?

- A. 12 seconds
- B. One day
- C. It never finalises
- D. About 13 minutes (two epochs)

<details><summary>Answer</summary>

answer: D
why: A slot is 12 seconds, an epoch is 32 slots, and finality usually takes two epochs.

</details>

### b03-post-5 · nakamoto
Why can selfish mining pay off for a pool with less than 50% of the hash power?

- A. It withholds blocks so honest miners waste work on blocks that get orphaned
- B. It steals coins
- C. It breaks SHA-256
- D. It controls finality

<details><summary>Answer</summary>

answer: A
why: By revealing blocks strategically, it earns more than its share of rewards.

</details>

### b03-post-6 · pos
Why can't someone create a million validators to control Ethereum?

- A. Registering needs an ID
- B. The protocol caps validators at 1,000
- C. Each validator needs at least 32 ETH at stake, so influence costs real capital
- D. The Ethereum Foundation picks validators

<details><summary>Answer</summary>

answer: C
why: Influence is proportional to stake, not to how many identities you create.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b03-ref-1
What is the difference between safety and liveness? Which one did the partition in my simulation break?

### b03-ref-2
How did longer network delays change the fork rate in my simulation, and why?

### b03-ref-3
What does selfish mining show about the "honest majority" assumption?

### b03-ref-4
How does proof-of-stake stop someone creating a million fake validators?

### b03-ref-5
What does "finalised" mean on Ethereum, and roughly how long does it take?

### b03-ref-6
Who actually decided Bitcoin's block-size dispute and Ethereum's DAO fork? What does that say about "code is law"?
