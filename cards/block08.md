---
block: 8
title: Auditing your own code, and DAOs
topics: exploits, governance, auditing, ai-audit
plan: week08-audit
---

# Block 8 · Auditing your own code, and DAOs

Harder exploits, writing a real audit, using AI and tools well, and how DAOs govern and get attacked.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b08-pre-1 · exploits
What does marking a Solidity variable `private` mean?

- A. Nobody can read it
- B. It's encrypted
- C. Other contracts can't read it directly, but anyone can read its value from chain storage
- D. Only the owner can read it

<details><summary>Answer</summary>

answer: C
why: Everything on-chain is public. `private` only controls access from other contracts.

</details>

### b08-pre-2 · governance
What is a DAO?

- A. A bank
- B. A type of NFT
- C. An organisation whose rules and treasury are managed by smart contracts and member votes
- D. A mining pool

<details><summary>Answer</summary>

answer: C
why: Decisions are made by proposals and votes, then carried out on-chain.

</details>

### b08-pre-3 · auditing
How is an audit finding usually ranked?

- A. By length
- B. By severity: its impact and likelihood
- C. By author
- D. By gas cost

<details><summary>Answer</summary>

answer: B
why: High impact plus plausible likelihood means high severity.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b08-key-1 · exploits
Why is "private" state not private on a blockchain? How would you read it?

Answer:

### b08-key-2 · exploits
How does a flash loan work, and why does it make some attacks possible with no capital?

Answer:

### b08-key-3 · auditing
How do you decide an audit finding's severity?

Answer:

### b08-key-4 · auditing
What makes a good audit finding write-up?

Answer:

### b08-key-5 · ai-audit
What are AI tools good and bad at when auditing smart contracts?

Answer:

### b08-key-6 · governance
How do proposals, voting, quorum and timelocks work in an on-chain Governor?

Answer:

### b08-key-7 · governance
How did the Beanstalk attacker use a flash loan to vote on and execute a governance proposal in a single transaction?

Answer:

### b08-key-8 · governance
What defences stop flash-loan governance attacks?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b08-post-1 · exploits
When must a flash loan be repaid?

- A. Within 30 days
- B. It must be backed by collateral
- C. Within the same transaction, or everything reverts
- D. When a DAO approves it

<details><summary>Answer</summary>

answer: C
why: Atomicity makes flash loans risk-free for the lender, and hands anyone huge temporary capital.

</details>

### b08-post-2 · governance
Why do voting-power snapshots (checkpoints at a past block) stop flash-loan governance attacks?

- A. Tokens borrowed now don't count toward votes measured at an earlier block
- B. They encrypt votes
- C. They block loans
- D. They make voting free

<details><summary>Answer</summary>

answer: A
why: OpenZeppelin's ERC20Votes stores checkpoints of delegated voting power whenever it changes, and votes are read at the proposal's snapshot block.

</details>

### b08-post-3 · governance
What does a timelock on passed proposals give a DAO?

- A. Faster execution
- B. More votes
- C. Lower fees
- D. Time for users to react, for example by withdrawing, before the change takes effect

<details><summary>Answer</summary>

answer: D
why: It's a safety window between a decision and its execution.

</details>

### b08-post-4 · auditing
A bug lets anyone drain all the funds, but only under a rare condition. The severity is usually…

- A. Informational
- B. A gas issue
- C. High or critical, because the impact is total even if it's less likely
- D. None

<details><summary>Answer</summary>

answer: C
why: Total loss of funds usually outweighs lower likelihood.

</details>

### b08-post-5 · exploits
What does Damn Vulnerable DeFi's "Unstoppable" challenge show?

- A. Flash loans are illegal
- B. A strict equality check on a balance can be broken by someone sending tokens directly, halting the contract
- C. Oracles are always safe
- D. ERC-20 has no bugs

<details><summary>Answer</summary>

answer: B
why: Never assume you control all the ways a contract's balance can change.

</details>

### b08-post-6 · ai-audit
What's a sensible way to use an LLM in an audit?

- A. Trust its findings without checking
- B. Use it to suggest possible issues, then confirm each one with tests or tools
- C. Skip Slither
- D. Let it deploy fixes

<details><summary>Answer</summary>

answer: B
why: LLMs find leads and also invent issues. A failing test is the proof.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b08-ref-1
Why is "private" state not private on a blockchain?

### b08-ref-2
What is the most severe finding in my AUDIT.md, and how did I fix it?

### b08-ref-3
What did the LLM find that Slither missed, and what did it get wrong?

### b08-ref-4
What breaks if one of my mocks is swapped for a malicious contract?

### b08-ref-5
How did the Beanstalk attacker pass a governance vote in one transaction, and which defences (timelocks, vote snapshots) would have stopped it?

### b08-ref-6
Who should hold the issuer and arbiter roles in my trust stack, and why?
