---
block: 6
title: Escrow, NFTs and marketplaces
topics: escrow, nft, security, signatures, marketplaces
plan: week06-escrow-nft
---

# Block 6 · Escrow, NFTs and marketplaces

Contracts that hold money safely, NFTs and what they really own, signed messages, and how marketplaces work.

You don't need to follow the 12-week plan to use these cards. The warm-up and final quiz are self-contained, and the key questions work on their own. Practise them on the [flashcard site](https://zikt.github.io/blockchain-learning/cards/) or in Anki ([how, and the file format](README.md)).

## Before you start

Optional warm-up quiz. Take it before you study the block, to see what you already know. It isn't scored against you: it's your baseline.

### b06-pre-1 · escrow
What does an escrow contract do?

- A. Holds funds until conditions are met, then releases or refunds them
- B. Mints tokens
- C. Stores images
- D. Mines blocks

<details><summary>Answer</summary>

answer: A
why: It replaces a trusted middleman with code everyone can read.

</details>

### b06-pre-2 · nft
What is an ERC-721 token?

- A. Interchangeable with others like it
- B. A stablecoin
- C. A wallet
- D. Unique: each token ID has exactly one owner

<details><summary>Answer</summary>

answer: D
why: Non-fungible means each token is distinct.

</details>

### b06-pre-3 · security
What is re-entrancy?

- A. Logging in twice
- B. When a contract calls an external contract that calls back into it before the first call finishes
- C. Replaying a transaction the next day
- D. Mining a block twice

<details><summary>Answer</summary>

answer: B
why: If state isn't updated before the external call, the callback can exploit the stale state.

</details>

## Key questions

The core ideas of the block, as flashcards. Write your answer under **Answer:** in your own words: a few sentences, a formula, or a small example. Cards with no answer yet still appear on the flashcard site, where learners can write their own.

### b06-key-1 · escrow
What is the checks-effects-interactions pattern, and why does it prevent re-entrancy?

Answer:

### b06-key-2 · escrow
List the states an escrow can be in, and the transitions between them.

Answer:

### b06-key-3 · nft
What does an NFT actually own on-chain, and what usually lives off-chain?

Answer:

### b06-key-4 · nft
How can an NFT's image live entirely on-chain?

Answer:

### b06-key-5 · signatures
What is EIP-712 typed-data signing, and how does it stop a signature being replayed on another chain or contract?

Answer:

### b06-key-6 · marketplaces
How do NFT marketplaces combine signed off-chain orders with on-chain settlement?

Answer:

### b06-key-7 · nft
What's the difference between ERC-721 and ERC-1155?

Answer:

### b06-key-8 · marketplaces
What is EIP-2981, and why did many marketplaces stop enforcing creator royalties?

Answer:

## Final quiz

Take it after the block. Your score here, together with how well you know the key questions, gives your strength for the block.

### b06-post-1 · security
To avoid re-entrancy in `withdraw()`, you should…

- A. Set the balance to zero first, then send the ETH
- B. Send the ETH first, then set the balance to zero
- C. Use a bigger gas limit
- D. Make the function public

<details><summary>Answer</summary>

answer: A
why: Effects before interactions: by the time any callback runs, the balance is already zero.

</details>

### b06-post-2 · nft
What does most NFTs' tokenURI point to?

- A. The image, stored in the contract
- B. A JSON metadata file, often on IPFS or an ordinary web server
- C. The owner's wallet
- D. A block explorer

<details><summary>Answer</summary>

answer: B
why: That's why many NFT images break when a server goes away.

</details>

### b06-post-3 · signatures
Why does an EIP-712 domain separator include the chain ID and contract address?

- A. So a signature meant for one contract on one chain can't be replayed on another
- B. To make signatures shorter
- C. To lower gas
- D. So wallets can skip showing the data

<details><summary>Answer</summary>

answer: A
why: The domain binds the signature to exactly where it's meant to be used.

</details>

### b06-post-4 · marketplaces
How are royalties under EIP-2981 enforced?

- A. By the Ethereum protocol
- B. They aren't: it's a standard way to report a royalty, and each marketplace chooses whether to pay it
- C. By validators
- D. They're mandatory for every ERC-721

<details><summary>Answer</summary>

answer: B
why: On-chain code can report a royalty, but it can't force an off-chain marketplace to honour it.

</details>

### b06-post-5 · nft
How does ERC-1155 differ from ERC-721?

- A. It can't hold NFTs
- B. It only works on layer 2
- C. It manages many token types, fungible and non-fungible, in one contract
- D. It has no owners

<details><summary>Answer</summary>

answer: C
why: It's common in games, where one contract holds swords, coins and unique items.

</details>

### b06-post-6 · escrow
A buyer deposits into escrow and the seller never ships. What should a well-designed escrow allow?

- A. The funds stay locked forever
- B. The seller withdraws anyway
- C. A refund after a deadline, or a decision by an arbiter
- D. The validator keeps it

<details><summary>Answer</summary>

answer: C
why: Every path needs an exit, including the one where nothing happens.

</details>

## Reflect (if you're following the plan)

Questions about your own builds this week. Answer them in LEARNING_LOG.md. They aren't scored or exported to Anki.

### b06-ref-1
List every state my escrow can be in. Which transitions can only the arbiter trigger?

### b06-ref-2
Where exactly would a re-entrancy attack hit my escrow if I sent the money before updating state?

### b06-ref-3
What does my NFT actually own, and what would break if its metadata lived on an ordinary web server?

### b06-ref-4
What stops an EIP-712 signature being replayed on another chain or another contract?

### b06-ref-5
Why did most marketplaces stop enforcing royalties, and what does that say about on-chain rules versus off-chain choices?

### b06-ref-6
Should a produce batch be an NFT, or is a record in the trace registry enough? Why?
