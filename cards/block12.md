---
block: 12
title: AI agents, zero knowledge and what's next
topics: agents, zk, account-abstraction, credentials, applications
plan: week12-agent-wallet
---

# Block 12 · AI agents, zero knowledge and what's next

Giving AI agents wallets safely, account abstraction, what zero-knowledge proofs can show, and verifiable credentials.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b12-pre-1 · agents
What is prompt injection?

- A. When text the AI reads, such as a web page, email or document, contains instructions that hijack what it does
- B. Typing too fast
- C. Retraining a model
- D. Hacking a wallet

<details><summary>Answer</summary>

answer: A
why: The model can't reliably tell your instructions apart from instructions hidden in its data.

</details>

### b12-pre-2 · zk
What does a zero-knowledge proof let you do?

- A. Hide that a proof exists
- B. Encrypt a wallet
- C. Prove a statement is true without revealing the underlying secret data
- D. Speed up mining

<details><summary>Answer</summary>

answer: C
why: For example, proving you know a password without revealing it.

</details>

### b12-pre-3 · account-abstraction
What can a smart-contract wallet do that an ordinary account can't?

- A. Enforce custom rules such as spending limits, allowlists or several required signers
- B. Only hold ETH
- C. Mine blocks
- D. Skip gas

<details><summary>Answer</summary>

answer: A
why: The account's rules are code.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b12-key-1 · agents
Why should limits on an AI agent's spending be enforced by a contract rather than by its prompt?

Answer:

### b12-key-2 · agents
What is prompt injection, and how could it make an agent with a wallet misbehave?

Answer:

### b12-key-3 · account-abstraction
What's the difference between an externally owned account, an ERC-4337 smart account and an EIP-7702 delegated account?

Answer:

### b12-key-4 · agents
What is x402, and how would an agent use it to pay for an API?

Answer:

### b12-key-5 · zk
What does a zk-SNARK prove, and what do "succinct" and "non-interactive" mean?

Answer:

### b12-key-6 · zk
What can zkML prove about a model's output, and what can't it prove?

Answer:

### b12-key-7 · credentials
How can anyone verify a credential you issued, without trusting a central database?

Answer:

### b12-key-8 · applications
For tokenised real-world assets, DAOs, prediction markets and DePIN, who has to trust whom?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b12-post-1 · agents
An agent's wallet contract has a daily cap and an allowlist. A malicious web page tells the agent to pay an unknown address. What happens?

- A. The payment goes through if the prompt is convincing
- B. The contract rejects it, because the address isn't on the allowlist
- C. The cap doubles
- D. The agent is deleted

<details><summary>Answer</summary>

answer: B
why: The model may be fooled. The contract isn't.

</details>

### b12-post-2 · account-abstraction
What did ERC-4337 introduce?

- A. A new consensus mechanism
- B. NFTs
- C. Smart accounts using UserOperations, bundlers and an EntryPoint contract, without changing the core protocol
- D. Rollups

<details><summary>Answer</summary>

answer: C
why: It adds account abstraction at the application layer.

</details>

### b12-post-3 · account-abstraction
What does EIP-7702 allow?

- A. Contracts become ordinary accounts
- B. Unlimited gas
- C. Private transactions
- D. An existing ordinary account to delegate to smart-contract code, gaining smart-wallet features at the same address

<details><summary>Answer</summary>

answer: D
why: It shipped in Ethereum's Pectra upgrade.

</details>

### b12-post-4 · zk
What can a zkML proof show?

- A. That a specific committed model produced this output from this input (optionally without revealing the model's weights)
- B. That the model is fair
- C. That the training data was accurate
- D. That the model is safe

<details><summary>Answer</summary>

answer: A
why: It proves the computation happened, not that the model is good.

</details>

### b12-post-5 · credentials
A credential's Merkle root is on-chain. What does a verifier need to check one credential?

- A. The issuer's private key
- B. Every credential in the cohort
- C. A login
- D. The credential, its Merkle proof and the on-chain root (plus the issuer's signature)

<details><summary>Answer</summary>

answer: D
why: That's the same pattern as the sensor readings, applied to certificates.

</details>

### b12-post-6 · zk
What does "succinct" mean in zk-SNARK?

- A. The proof is small and quick to verify, even for a large computation
- B. The statement is short
- C. It uses little memory to generate
- D. It expires quickly

<details><summary>Answer</summary>

answer: A
why: Verifying costs far less than redoing the computation.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b12-ref-1
Which injection prompts fooled the model, and did the contract still block the payment?

### b12-ref-2
What does my EZKL proof actually prove about the model, and what doesn't it?

### b12-ref-3
What is the difference between an ordinary account, an ERC-4337 smart account and an EIP-7702 delegated account?

### b12-ref-4
If someone doubts my week 5 credential, how can they check it themselves?

### b12-ref-5
What would I build with one more month, and why?

### b12-ref-6
Of tokenised assets, DAOs, prediction markets and DePIN, which has the most honest need for a blockchain?
