---
block: 11
title: The trust stack, end to end
topics: deployment, integration, blockchain-vs-database, policy, roles
plan: week10-11-capstone
---

# Block 11 · The trust stack, end to end

Connecting credentials, provenance, a marketplace and payments into one tested system, and judging honestly where a blockchain helps.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b11-pre-1 · deployment
Why deploy with an encrypted keystore instead of pasting a private key into a .env file?

- A. It's faster
- B. Solidity requires keystores
- C. There's no difference
- D. A plain-text key can leak through git, logs or malware

<details><summary>Answer</summary>

answer: D
why: Leaked deploy keys are one of the most common causes of lost funds.

</details>

### b11-pre-2 · integration
What does an end-to-end test do?

- A. Checks one function
- B. Tests CSS
- C. Only benchmarks gas
- D. Runs a whole user flow across all the contracts together

<details><summary>Answer</summary>

answer: D
why: It catches bugs in how the parts connect.

</details>

### b11-pre-3 · blockchain-vs-database
If one organisation that everyone already trusts runs the system, the better choice is usually…

- A. A blockchain
- B. An NFT
- C. An ordinary database
- D. A DAO

<details><summary>Answer</summary>

answer: C
why: Blockchains earn their cost when no single party is trusted by everyone.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b11-key-1 · integration
Walk through a produce batch's journey in a trust stack, from issuing credentials to settlement or refund.

Answer:

### b11-key-2 · policy
How can a contract decide whether a batch was compliant, and who can prove a violation?

Answer:

### b11-key-3 · roles
List the roles in a supply-chain system like this, what each can do, and the worst thing each could do if compromised.

Answer:

### b11-key-4 · deployment
What should a deployments file record, and what does a smoke test check against a live deployment?

Answer:

### b11-key-5 · blockchain-vs-database
For provenance, a marketplace, payments and credentials, would a shared database work just as well? Why or why not?

Answer:

### b11-key-6 · deployment
Why verify every contract on the block explorer?

Answer:

### b11-key-7 · integration
Why can a demo site that reads directly from contracts work with no login and no backend server?

Answer:

### b11-key-8 · policy
How do you stop an actor signing a step their role doesn't allow, such as a transporter signing an inspection?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b11-post-1 · policy
A batch has a signed reading of 11 °C, and its policy is 2–8 °C. Once a valid Merkle proof is submitted, the escrowed payment should…

- A. Go to the seller
- B. Be burned
- C. Be refunded to the buyer
- D. Stay locked forever

<details><summary>Answer</summary>

answer: C
why: A proven violation triggers the refund path.

</details>

### b11-post-2 · roles
The Admin tab is hidden unless the wallet holds the issuer role. What actually protects the admin functions?

- A. On-chain role checks in each function
- B. The hidden tab
- C. The RPC provider
- D. GitHub Pages

<details><summary>Answer</summary>

answer: A
why: The page only decides what's shown. The contract decides what's allowed.

</details>

### b11-post-3 · deployment
What is `cast wallet import` used for?

- A. Importing tokens
- B. Storing an existing private key in an encrypted keystore account, so scripts can sign without a plain-text key
- C. Verifying contracts
- D. Starting anvil

<details><summary>Answer</summary>

answer: B
why: You then pass --account <name> to forge script.

</details>

### b11-post-4 · blockchain-vs-database
Which kind of system most needs a blockchain?

- A. One where parties who don't trust each other need to verify records none of them controls
- B. A private admin notes page
- C. A website's styling
- D. One company's internal inventory

<details><summary>Answer</summary>

answer: A
why: Shared, tamper-evident records between rivals are the sweet spot.

</details>

### b11-post-5 · integration
What does a smoke test against a live deployment check?

- A. Every edge case
- B. Quickly, that the deployed contracts exist and basic read calls return what's expected
- C. Gas optimisation
- D. Frontend styling

<details><summary>Answer</summary>

answer: B
why: It's a fast sanity check after deploying, not a full test suite.

</details>

### b11-post-6 · roles
A farmer's credential is revoked. What happens?

- A. Their past signed steps disappear
- B. They can't sign new steps or list new batches, but past records remain
- C. All batches are refunded
- D. The registry is deleted

<details><summary>Answer</summary>

answer: B
why: Revocation stops future actions. It can't erase history.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b11-ref-1
Can I run the whole demo from a fresh clone with one command, and does CI agree?

### b11-ref-2
What happens to the buyer's TestUSD when a reading is out of range, and which test proves it?

### b11-ref-3
Who can do what in my system, and what is the worst thing each role could do?

### b11-ref-4
For which of the four parts would a shared database be just as good, and why?

### b11-ref-5
Does make smoke pass against the live deployment?

### b11-ref-6
Can someone who has never seen my repo follow a batch on the trace page?
