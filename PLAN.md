# The plan: every task, with due dates

Genesis to Capstone: 12 weeks at 10 hours a week, starting Monday 28 September 2026. The capstone ships Sunday 13 December and the plan ends Sunday 20 December.

Due dates follow the weekly rhythm: Tuesday reading (2 h), Thursday reading then building (2 h), Friday building (1.5 h), Saturday main build, log and push (4.5 h). Mon and Wed are flex days. If you start on a different date, shift every date by the same number of days (the tracker in `tracker/` does this for you).

Task IDs (`x3t4` = block 3, task 4) match the tracker and `progress.json`. Each block lists what you should be able to do by the end, and questions to answer in your log on Saturday.

## Block 1 · 28 Sep – 4 Oct · The mental model, keys and signatures → Project 0

**Goal:** Understand why hash-linking plus proof-of-work makes history expensive to rewrite, then add real ownership with ECDSA signatures and Merkle roots.  
**Ship:** pow_demo.py and Project 0 (toy_chain.py with a tamper test)  
**Time:** 10 h

**By the end of this block you can:**

- Explain how hash pointers link blocks, and why editing one block breaks every block after it
- Explain what proof-of-work costs an attacker, and measure how the work grows with each extra leading zero
- Sign and verify a transaction on secp256k1, and say what a signature proves and what it doesn't
- Build a Merkle root and explain how it proves one transaction is in a block

**Check yourself** (answer in your log on Saturday):

1. If I change one transaction in block 2 of 10, which check fails first, and why do all later blocks fail too?
2. Each extra leading hex zero multiplies the expected work by how much? What did my timings show?
3. Which hash property (preimage, second-preimage or collision resistance) does proof-of-work rely on, and why that one?
4. What exactly does a valid signature prove? Name one thing it doesn't prove.
5. How many hashes do I need to prove one transaction is in a block of 1,024 transactions?
6. Can I explain the chain to a non-technical friend in two minutes, without notes?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x1t1` | Tue 29 Sep | Learn | 30 | Watch 3Blue1Brown's bitcoin video end to end | [But how does bitcoin actually work?](https://www.youtube.com/watch?v=bBC-nXj3Ng4) |
| ☐ | `x1t2` | Tue 29 Sep | Learn | 45 | Click through all five pages of the blockchain demo: hash, block, blockchain, distributed, tokens | [andersbrownworth.com/blockchain](https://andersbrownworth.com/blockchain/) |
| ☐ | `x1t3` | Tue 29 Sep | Learn | 45 | Read the Bitcoin whitepaper, sections 1–6. Don't worry about the math yet | [bitcoin.pdf](https://bitcoin.org/bitcoin.pdf) |
| ☐ | `x1t4` | Fri 2 Oct | Build | 30 | Create the blockchain-learning repo with a README and a /week01 folder | — |
| ☐ | `x1t5` | Sat 3 Oct | Build | 90 | Using Python's hashlib, find a nonce that gives 4 leading hex zeros, then time 5 and 6 zeros | [hashlib docs](https://docs.python.org/3/library/hashlib.html) |
| ☐ | `x1t6` | Sat 3 Oct | Write | 30 | Log: explain in five sentences why editing one block invalidates every block after it | — |
| ☐ | `x1t7` | Thu 1 Oct | Learn | 45 | Read Cloudflare's primer on elliptic-curve cryptography | [A (relatively easy to understand) primer on ECC](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/) |
| ☐ | `x1t8` | Thu 1 Oct | Learn | 45 | Princeton textbook, chapter 1: hash pointers, Merkle trees, digital signatures | [Princeton book PDF](https://d28rh4a8wq0iu5.cloudfront.net/bitcointech/readings/princeton_bitcoin_book.pdf) |
| ☐ | `x1t9` | Sat 3 Oct | Build | 150 | Build Project 0: Block class, SHA-256 linking, adjustable-difficulty PoW, transactions signed with the ecdsa library (SECP256k1), a Merkle root per block, and validate_chain() | [python-ecdsa](https://pypi.org/project/ecdsa/) |
| ☐ | `x1t10` | Sat 3 Oct | Build | 30 | Tamper test: change one transaction in block 2 and confirm validation fails at the right block | — |
| ☐ | `x1t11` | Sat 3 Oct | Write | 15 | Log: what a signature proves, and what it does not | — |
| ☐ | `x1t12` | Thu 1 Oct | Crypto | 30 | The three security properties of hash functions (preimage, second-preimage and collision resistance), and which one proof-of-work relies on | [A Graduate Course in Applied Cryptography (Boneh & Shoup, free)](https://toc.cryptobook.us/) · [Cryptography I (Dan Boneh, Coursera)](https://www.coursera.org/learn/crypto) |
| ☐ | `x1t13` | Fri 2 Oct | AI | 15 | Ask an LLM to explain proof-of-work, then use the whitepaper to find one thing it got wrong or oversimplified. Note it in your log | — |

## Block 2 · 5 Oct – 11 Oct · Bitcoin: UTXOs, raw transactions and mining

**Goal:** Run your own node, see that Bitcoin has no balances, and build and decode a transaction by hand.  
**Ship:** A regtest node, a UTXO version of your toy chain, and raw_tx.py with a decoded transaction  
**Time:** 10 h

**By the end of this block you can:**

- Explain the UTXO model and why Bitcoin has no account balances
- Run a regtest node and move coins with bitcoin-cli
- Build, sign, broadcast and decode a raw transaction, and explain every field
- Explain difficulty retargeting, the most-work chain rule, and what a 51% attacker can and can't do
- Explain in one paragraph what Schnorr signatures and Taproot add to ECDSA

**Check yourself** (answer in your log on Saturday):

1. Where is "my balance" actually stored, and how does a wallet work it out?
2. In my raw transaction, which script locks the output and which one unlocks it?
3. Why did I have to mine 101 blocks before I could spend anything?
4. What can a 51% attacker do to recent transactions, and why can't they take my coins?
5. Where is the fee in my transaction? (It isn't a field.)
6. If half the miners switched off tomorrow, what would happen to block times, and for how long?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x2t1` | Tue 6 Oct | Learn | 60 | Mastering Bitcoin: the 'Introduction' and 'How Bitcoin Works' chapters | [bitcoinbook on GitHub](https://github.com/bitcoinbook/bitcoinbook) |
| ☐ | `x2t2` | Tue 6 Oct | Learn | 45 | learnmeabitcoin: the transaction and UTXO pages | [learnmeabitcoin technical](https://learnmeabitcoin.com/technical/) |
| ☐ | `x2t3` | Sat 10 Oct | Build | 60 | Install Bitcoin Core, start it with -regtest, mine 101 blocks, send coins to a second address with bitcoin-cli | [Bitcoin Core download](https://bitcoincore.org/en/download/) · [Bitcoin developer examples (regtest)](https://developer.bitcoin.org/examples/testing.html) |
| ☐ | `x2t4` | Sat 10 Oct | Build | 60 | Change your toy chain to UTXOs: inputs reference earlier outputs, and double spends are rejected | — |
| ☐ | `x2t5` | Thu 8 Oct | Learn | 45 | Mastering Bitcoin: the 'Keys and Addresses' and 'Transactions' chapters | [bitcoinbook on GitHub](https://github.com/bitcoinbook/bitcoinbook) |
| ☐ | `x2t6` | Thu 8 Oct | Learn | 30 | learnmeabitcoin: Script, P2PKH and P2WPKH | [learnmeabitcoin technical](https://learnmeabitcoin.com/technical/) |
| ☐ | `x2t7` | Sat 10 Oct | Build | 105 | With python-bitcoinlib, build, sign and broadcast a raw transaction on regtest, then run decoderawtransaction on it | [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib) |
| ☐ | `x2t8` | Thu 8 Oct | Learn | 45 | Mastering Bitcoin: the mining and consensus chapter | [bitcoinbook on GitHub](https://github.com/bitcoinbook/bitcoinbook) |
| ☐ | `x2t9` | Fri 9 Oct | Learn | 30 | Re-read the whitepaper, sections 7–11, including the attacker probability calculation | [bitcoin.pdf](https://bitcoin.org/bitcoin.pdf) |
| ☐ | `x2t10` | Sat 10 Oct | Write | 15 | Log: what the locking and unlocking scripts did in your transaction, and why a 51% attacker still can't steal coins | — |
| ☐ | `x2t11` | Fri 9 Oct | Crypto | 30 | Schnorr signatures and Taproot. Why Bitcoin added them alongside ECDSA (linearity, key aggregation) | [BIP-340: Schnorr signatures](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki) · [learnmeabitcoin: technical guide](https://learnmeabitcoin.com/technical/) |
| ☐ | `x2t12` | Sat 10 Oct | Explain | 45 | Explainer #1: write "I built a blockchain from scratch" in blog/ (600–900 words, weeks 1–2). Optional: record a 5-minute video teaching it and link it in the post | — |
| ☐ | `x2t13` | Fri 9 Oct | Apps | 30 | Cryptocurrencies as money: Bitcoin's fixed supply and halvings, why stablecoins exist, and what a CBDC is. Look up the eNaira and one other CBDC on the tracker and note why adoption differed | [ethereum.org: stablecoins](https://ethereum.org/en/stablecoins/) · [Atlantic Council CBDC tracker](https://www.atlanticcouncil.org/cbdctracker/) |

## Block 3 · 12 Oct – 18 Oct · Consensus, attacks and proof-of-stake → Project 2

**Goal:** Learn the problem blockchains solve, then watch forks, partitions and reorgs happen in your own network simulation.  
**Ship:** Project 2: a multi-node simulation with gossip, fork resolution, a partition that heals, and stake-weighted proposers  
**Time:** 10 h

**By the end of this block you can:**

- State the consensus problem (state machine replication) and its safety and liveness properties
- Explain why classic Byzantine agreement needs identities and a two-thirds honest majority, and how proof-of-work avoids identities
- Observe forks and reorgs in your own simulation and relate them to network delay
- Explain how proof-of-stake picks proposers, what finality means in Gasper, and what slashing punishes
- Compare PoW and PoS on security, finality, energy and who can take part

**Check yourself** (answer in your log on Saturday):

1. What is the difference between safety and liveness? Which one did the partition in my simulation break?
2. How did longer network delays change the fork rate in my simulation, and why?
3. What does selfish mining show about the "honest majority" assumption?
4. How does proof-of-stake stop someone creating a million fake validators?
5. What does "finalised" mean on Ethereum, and roughly how long does it take?
6. Who actually decided Bitcoin's block-size dispute and Ethereum's DAO fork? What does that say about "code is law"?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x3t1` | Tue 13 Oct | Learn | 75 | Roughgarden: Lecture 1 (overview, state machine replication, consistency and liveness) | [Foundations of Blockchains playlist](https://www.youtube.com/playlist?list=PLEGCF-WLh2RLOHv_xUGLqRts_9JxrckiA) |
| ☐ | `x3t2` | Tue 13 Oct | Learn | 30 | Decentralized Thoughts on Nakamoto consensus | [Nakamoto's longest-chain-wins protocol](https://decentralizedthoughts.github.io/2021-10-15-Nakamoto-Consensus/) |
| ☐ | `x3t3` | Thu 15 Oct | Learn | 45 | Lamport, Shostak and Pease: The Byzantine Generals Problem, sections 1–3 | [byz.pdf](https://lamport.azurewebsites.net/pubs/byz.pdf) |
| ☐ | `x3t4` | Sat 17 Oct | Build | 95 | Build a simulation of 4 nodes that mine and gossip blocks with random network delays and resolve forks by the longest chain | — |
| ☐ | `x3t5` | Sat 17 Oct | Write | 30 | Log: how often did forks happen, and how did delay change that? | — |
| ☐ | `x3t6` | Thu 15 Oct | Learn | 60 | Roughgarden: the lectures on selfish mining and proof-of-stake sybil resistance | [Foundations of Blockchains playlist](https://www.youtube.com/playlist?list=PLEGCF-WLh2RLOHv_xUGLqRts_9JxrckiA) |
| ☐ | `x3t7` | Fri 16 Oct | Learn | 45 | ethereum.org: proof-of-stake and Gasper | [Proof-of-stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/) · [Gasper](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/gasper/) |
| ☐ | `x3t8` | Fri 16 Oct | Learn | 30 | Skim Eyal and Sirer, Majority is not Enough (selfish mining) | [Selfish mining paper](https://www.cs.cornell.edu/~ie53/publications/btcProcFC.pdf) |
| ☐ | `x3t9` | Sat 17 Oct | Build | 110 | Split your network into two halves for 20 blocks, heal it, and log the reorg. Then add stake-weighted proposer selection | — |
| ☐ | `x3t10` | Sat 17 Oct | Write | 30 | Log: a table comparing PoW and PoS on security, finality, energy and who can participate | — |
| ☐ | `x3t11` | Fri 16 Oct | Crypto | 30 | BLS signature aggregation and VRFs. How proof-of-stake compresses thousands of validator votes and picks proposers fairly | [ethereum.org: proof-of-stake keys (BLS)](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/keys/) · [A Graduate Course in Applied Cryptography (Boneh & Shoup, free)](https://toc.cryptobook.us/) |
| ☐ | `x3t12` | Sat 17 Oct | Apps | 20 | How cryptocurrencies change their rules: read about Bitcoin's block-size dispute and Ethereum's DAO fork. Who decided, and what happened to people who disagreed? | [ethereum.org: history of Ethereum](https://ethereum.org/en/history/) |

## Block 4 · 19 Oct – 25 Oct · The Ethereum model and Solidity fluency

**Goal:** Understand accounts, gas and the EVM, deploy your first contract to Sepolia, and get comfortable writing Solidity.  
**Ship:** SimpleStorage on Sepolia and five small contracts in /week04  
**Time:** 10.5 h

**By the end of this block you can:**

- Explain accounts (externally owned vs contract), gas and fees, and how the EVM runs a transaction
- Deploy a contract to Sepolia from a testnet-only wallet
- Write small contracts with mappings, modifiers, events and custom errors from memory
- Derive an Ethereum address from a public key with Keccak-256
- Compare custodial wallets, self-custody, centralised exchanges and DEXs
- Explain what "web3" claims, and the strongest case against it

**Check yourself** (answer in your log on Saturday):

1. How does an Ethereum account differ from a Bitcoin UTXO?
2. Why does a failed transaction still cost gas?
3. What is the difference between storage and memory, and which costs more?
4. From memory: how do I get from a private key to an address?
5. What did the FTX collapse show about "not your keys, not your coins"?
6. Which web3 claims will this plan let me test myself, and what do I think of them today?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x4t1` | Tue 20 Oct | Learn | 45 | Read the Ethereum whitepaper | [ethereum.org/whitepaper](https://ethereum.org/en/whitepaper/) |
| ☐ | `x4t2` | Tue 20 Oct | Learn | 60 | ethereum.org docs: accounts, transactions, gas and fees, the EVM | [Ethereum developer docs](https://ethereum.org/en/developers/docs/) |
| ☐ | `x4t3` | Sat 24 Oct | Build | 90 | Cyfrin Updraft: Blockchain Basics, then the first Remix lessons of Solidity Smart Contract Development | [Blockchain Basics](https://updraft.cyfrin.io/courses/blockchain-basics) · [Updraft course list](https://updraft.cyfrin.io/courses) · [Remix IDE](https://remix.ethereum.org/) |
| ☐ | `x4t4` | Sat 24 Oct | Build | 30 | Set up a wallet in a separate browser profile, get Sepolia ETH from a faucet, deploy SimpleStorage | [Google Cloud Sepolia faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia) |
| ☐ | `x4t5` | Sat 24 Oct | Write | 30 | Log: the difference between a Bitcoin UTXO and an Ethereum account | — |
| ☐ | `x4t6` | Thu 22 Oct | Learn | 75 | Work through the first ~25 Solidity by Example pages, running each in Remix | [solidity-by-example.org](https://solidity-by-example.org/) |
| ☐ | `x4t7` | Fri 23 Oct | Learn | 70 | Updraft: continue the Solidity course (the FundMe section) | [Updraft courses](https://updraft.cyfrin.io/courses) |
| ☐ | `x4t8` | Sat 24 Oct | Build | 75 | Write 5 small contracts without looking: a counter, a whitelist, a vault, a voting contract, a timelock | — |
| ☐ | `x4t9` | Sat 24 Oct | Write | 30 | Log: what surprised you about gas costs | — |
| ☐ | `x4t10` | Fri 23 Oct | Crypto | 20 | Keccak-256 vs. SHA-3, and how an Ethereum address is derived from a public key. Derive one yourself in Python | [ethereum.org: accounts](https://ethereum.org/en/developers/docs/accounts/) |
| ☐ | `x4t11` | Sat 24 Oct | Explain | 45 | Explainer #2: write "How strangers agree: consensus in plain words" in blog/ (600–900 words, weeks 3–4). Optional: record a 5-minute video teaching it and link it in the post | — |
| ☐ | `x4t12` | Fri 23 Oct | Apps | 30 | Exchanges and wallets: custodial vs. self-custody, centralised exchanges vs. DEXs, and what the FTX collapse showed about 'not your keys, not your coins' | [ethereum.org: wallets](https://ethereum.org/en/wallets/) · [ethereum.org: DeFi](https://ethereum.org/en/defi/) |
| ☐ | `x4t13` | Fri 23 Oct | Apps | 30 | What "web3" means, and the case against it: read ethereum.org's introduction to web3, then Moxie Marlinspike's "My first impressions of web3". In your log, list which web3 claims this plan lets you test yourself, and your view today | [ethereum.org: what is web3?](https://ethereum.org/en/web3/) · [Moxie Marlinspike: My first impressions of web3](https://moxie.org/2022/01/07/web3-first-impressions.html) |

## Block 5 · 26 Oct – 1 Nov · Foundry and your ERC-20 → Project 3a

**Goal:** Move to a real toolchain, write a token from the spec, fuzz it, deploy it and verify it.  
**Ship:** Project 3a: an ERC-20 with unit and fuzz tests, verified on Sepolia Etherscan  
**Time:** 10.75 h

**By the end of this block you can:**

- Set up a Foundry project and write unit and fuzz tests
- Implement ERC-20 from the spec, including allowances, and explain the approval race
- Deploy with forge script and verify the source on Etherscan
- Compare your token with OpenZeppelin's and explain the differences
- Explain how fiat-backed, crypto-backed and algorithmic stablecoins hold their peg, and why UST failed
- Start the capstone: TestUSD with tests, demo stage 1, and the Trust stack workflow green

**Check yourself** (answer in your log on Saturday):

1. What does approve plus transferFrom let a spender do, and what is the known approval race?
2. What did my fuzz tests find, or why did they find nothing, and what would be a stronger property to test?
3. Why does TestUSD use 6 decimals, and what goes wrong when two tokens' decimals differ?
4. What would have to back TestUSD for it to be a real stablecoin?
5. Why did UST collapse for good while USDC got its peg back?
6. Is the Trust stack workflow green, and can I say what each job checks?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x5t1` | Tue 27 Oct | Learn | 45 | Foundry: getting started, then forge test basics. Install the pinned version the repo uses: foundryup --install v1.5.1 (see toolchain.env) | [Foundry getting started](https://www.getfoundry.sh/introduction/getting-started) |
| ☐ | `x5t2` | Tue 27 Oct | Learn | 60 | Updraft Foundry Fundamentals: the first section | [Foundry Fundamentals](https://updraft.cyfrin.io/courses/foundry) |
| ☐ | `x5t3` | Sat 31 Oct | Build | 120 | Write an ERC-20 by reading the spec only. Test transfer, approve, transferFrom and the failure cases | [EIP-20](https://eips.ethereum.org/EIPS/eip-20) |
| ☐ | `x5t4` | Sat 31 Oct | Write | 30 | Log: what the allowance pattern protects, and its known approval race | — |
| ☐ | `x5t5` | Thu 29 Oct | Learn | 20 | Compare your token with OpenZeppelin's ERC20 source | [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) · [OpenZeppelin Wizard](https://wizard.openzeppelin.com/) |
| ☐ | `x5t6` | Thu 29 Oct | Learn | 20 | Foundry docs: fuzz testing and forge scripts | [Foundry guides](https://www.getfoundry.sh/guides) |
| ☐ | `x5t7` | Sat 31 Oct | Build | 150 | Add fuzz tests, deploy with forge script to Sepolia, verify the contract on Etherscan | [Sepolia Etherscan](https://sepolia.etherscan.io/) |
| ☐ | `x5t8` | Thu 29 Oct | Learn | 15 | Updraft Foundry Fundamentals: continue | [Foundry Fundamentals](https://updraft.cyfrin.io/courses/foundry) |
| ☐ | `x5t9` | Sat 31 Oct | Write | 30 | Log: one bug the fuzzer found, or why it found none | — |
| ☐ | `x5t10` | Thu 29 Oct | AI | 30 | Have an LLM write fuzz tests for your ERC-20, then check which ones actually test something. Keep the good ones and note the useless ones in your log | — |
| ☐ | `x5t11` | Sat 31 Oct | Capstone | 30 | Capstone C: turn your ERC-20 into TestUSD, the stablecoin for the payment rail. Use 6 decimals, add a capped faucet mint for testers, write tests, and keep it in trust-stack/ (the shared capstone project) | — |
| ☐ | `x5t12` | Sat 31 Oct | Capstone | 20 | Demo stage 1: add forge-std as a submodule (see trust-stack/README.md), write script/demo/01_TestUSD.s.sol from the template in script/demo/README.md, run make demo, push, and check the Trust stack run on GitHub shows stage 01 passed | [Foundry: scripting](https://www.getfoundry.sh/guides) |
| ☐ | `x5t13` | Sat 31 Oct | Capstone | 15 | Testing setup: run python scripts/set_github_user.py <your-username>, open TESTING.md, and start the rules-to-tests table with TestUSD's tests. Check coverage and Slither pass in CI | [Slither](https://github.com/crytic/slither) |
| ☐ | `x5t14` | Sat 31 Oct | Capstone | 15 | Docker check (optional, see DOCKER.md): install Docker Desktop, then from trust-stack/ run make docker-test and make docker-demo. They should match your normal run, and the docker job in the Trust stack run on GitHub should be green | [Docker: get started](https://docs.docker.com/get-started/get-docker/) |
| ☐ | `x5t15` | Thu 29 Oct | Apps | 45 | Stablecoins I, how they hold $1: fiat-backed (USDC, USDT) and what their reserve reports actually show; crypto-collateralised (DAI); algorithmic. Then two failures: TerraUST's collapse (May 2022) and USDC's brief depeg when Silicon Valley Bank failed (March 2023). Note in your log which design TestUSD copies, and what would have to back it for real | [ethereum.org: stablecoins](https://ethereum.org/en/stablecoins/) · [Circle: USDC transparency](https://www.circle.com/transparency) · [Tether: transparency](https://tether.to/en/transparency/) · [Terra (blockchain) and the UST collapse](https://en.wikipedia.org/wiki/Terra_(blockchain)) · [Federal Reserve: SVB's failure and its impact on stablecoins](https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html) |

## Block 6 · 2 Nov – 8 Nov · Escrow and an on-chain NFT → Projects 3b and 3c

**Goal:** Write your first contract that holds value, then an NFT whose image lives entirely on-chain. End with frontend prep for next week.  
**Ship:** Project 3b (Escrow.sol) and Project 3c (on-chain SVG NFT)  
**Time:** 10.5 h

**By the end of this block you can:**

- Write a contract that holds value (escrow) using checks-effects-interactions, with a test for every path
- Explain re-entrancy and show how your escrow avoids it
- Build an ERC-721 whose metadata and image live on-chain
- Sign and verify EIP-712 typed data with replay protection
- Explain how NFT marketplaces use signed orders, escrow and royalties, and what NFTs are really used for today
- Define the trust stack's interfaces, product policy and rules-to-tests table

**Check yourself** (answer in your log on Saturday):

1. List every state my escrow can be in. Which transitions can only the arbiter trigger?
2. Where exactly would a re-entrancy attack hit my escrow if I sent the money before updating state?
3. What does my NFT actually own, and what would break if its metadata lived on an ordinary web server?
4. What stops an EIP-712 signature being replayed on another chain or another contract?
5. Why did most marketplaces stop enforcing royalties, and what does that say about on-chain rules versus off-chain choices?
6. Should a produce batch be an NFT, or is a record in the trace registry enough? Why?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x6t1` | Tue 3 Nov | Learn | 20 | Solidity docs: Security Considerations (read before writing code that holds money) | [Security considerations](https://docs.soliditylang.org/en/latest/security-considerations.html) |
| ☐ | `x6t2` | Tue 3 Nov | Learn | 20 | Solidity by Example: Sending Ether, Payable, and the Re-entrancy hack | [solidity-by-example.org](https://solidity-by-example.org/) |
| ☐ | `x6t3` | Fri 6 Nov | Build | 135 | Build Escrow: deposit, release by buyer or arbiter, refund after a deadline, dispute. Emit events, use checks-effects-interactions | — |
| ☐ | `x6t4` | Sat 7 Nov | Write | 30 | Log: every state the escrow can be in, as a small state diagram | — |
| ☐ | `x6t5` | Tue 3 Nov | Learn | 20 | Read EIP-721 | [EIP-721](https://eips.ethereum.org/EIPS/eip-721) |
| ☐ | `x6t6` | Tue 3 Nov | Learn | 15 | OpenZeppelin ERC-721 docs and the Wizard | [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) · [Wizard](https://wizard.openzeppelin.com/) |
| ☐ | `x6t7` | Sat 7 Nov | Build | 80 | Build an NFT whose tokenURI returns base64 JSON with an SVG generated in Solidity | — |
| ☐ | `x6t8` | Sat 7 Nov | Write | 20 | Log: what an NFT actually owns, and what lives off-chain in most NFTs | — |
| ☐ | `x6t9` | Tue 3 Nov | Learn | 20 | viem: getting started, reading and writing contracts | [viem.sh](https://viem.sh/) |
| ☐ | `x6t10` | Tue 3 Nov | Learn | 10 | Scaffold-ETH 2 docs: hooks and deploying | [docs.scaffoldeth.io](https://docs.scaffoldeth.io/) · [wagmi](https://wagmi.sh/) |
| ☐ | `x6t11` | Thu 5 Nov | Crypto | 30 | EIP-712 typed-data signatures and replay protection. Sign an escrow release off-chain and verify it in Solidity | [EIP-712](https://eips.ethereum.org/EIPS/eip-712) · [OpenZeppelin EIP712 utilities](https://docs.openzeppelin.com/contracts/5.x/api/utils#EIP712) |
| ☐ | `x6t12` | Sat 7 Nov | Explain | 45 | Explainer #3: write "Replacing a middleman with an escrow contract, and what it can't replace" in blog/ (600–900 words, weeks 5–6). Optional: record a 5-minute video teaching it and link it in the post | — |
| ☐ | `x6t13` | Thu 5 Nov | Apps | 30 | Marketplaces: how on-chain marketplaces work (listings, signed orders, escrow, royalties, disputes). Skim the Seaport contracts and sketch how your escrow and NFT could become a small marketplace | [Seaport (OpenSea's marketplace protocol)](https://github.com/ProjectOpenSea/seaport) |
| ☐ | `x6t14` | Sat 7 Nov | Write | 15 | Write trust-stack/README.md: the four parts (A provenance, B marketplace, C payment rail, D credentials) in your own words, how they connect, and what 'working and tested' means for each | — |
| ☐ | `x6t15` | Sat 7 Nov | Capstone | 30 | Capstone B: copy your escrow into trust-stack/ as Marketplace.sol. list(batchId, price) is allowed only for sellers with a valid credential (check the mock for now), buyers pay in TestUSD into escrow, and completed trades count as reputation. Test it against the mocks | — |
| ☐ | `x6t16` | Sat 7 Nov | Capstone | 30 | Integration design: write trust-stack/INTERFACES.md and the Solidity interfaces the parts talk through (ICredentialRegistry.isValid(account, role), IProvenance.batchStatus(batchId), IMarketplace.list(batchId, price)), plus mock versions of D and A so the marketplace can be tested against them now | — |
| ☐ | `x6t17` | Sat 7 Nov | Capstone | 15 | Traceability design: in trust-stack/POLICY.md, define a batch's journey (harvested → packed → shipped → received), which role may sign each step (farmer, cooperative, transporter, inspector, buyer), and one product policy, e.g. tomatoes: 2–8 °C, at most 48 h in transit, inspection required | — |
| ☐ | `x6t18` | Sat 7 Nov | Capstone | 20 | Rules to tests: for every rule in your POLICY.md, add a row to TESTING.md with a named test (e.g. test_RevertWhen_TransporterSignsInspection) and write the empty test so CI shows what's still missing | — |
| ☐ | `x6t19` | Sat 7 Nov | Capstone | 15 | Demo stages 2–3 with the mocks: issue roles and list batch 1, so make demo now runs stages 01–03 | — |
| ☐ | `x6t20` | Thu 5 Nov | Apps | 30 | NFTs beyond the hype: ERC-1155 (many token types in one contract), the royalty standard EIP-2981 and why marketplaces stopped enforcing royalties, wash trading, and what NFTs are used for now (tickets, credentials, game items, real-world assets). End with a capstone question in your log: should each produce batch be an NFT, or is a record in your trace registry enough? | [ethereum.org: NFTs](https://ethereum.org/en/nft/) · [EIP-1155](https://eips.ethereum.org/EIPS/eip-1155) · [EIP-2981: NFT royalties](https://eips.ethereum.org/EIPS/eip-2981) |

## Block 7 · 9 Nov – 15 Nov · A dApp frontend, then start breaking contracts → Project 3d

**Goal:** Ship a usable escrow frontend, then learn the common vulnerability classes by exploiting them.  
**Ship:** Project 3d (escrow dApp with a 2-minute demo) and Ethernaut levels 0–5  
**Time:** 10.75 h

**By the end of this block you can:**

- Connect a web frontend to your contracts so a non-developer could use it
- Recognise common vulnerability classes by exploiting them (Ethernaut 0–5)
- Run Slither and tell real findings from noise
- Write invariant tests for escrow solvency and token supply
- Store NFT metadata on IPFS, and explain content addressing, ENS and Sign-In with Ethereum

**Check yourself** (answer in your log on Saturday):

1. What happens, step by step, between clicking "Buy" and the transaction being mined?
2. For each Ethernaut level I solved, what was the bug in one line?
3. Which Slither findings were real, and why were the others noise?
4. What must always be true of my escrow, and how does the invariant test try to break it?
5. What does an IPFS CID guarantee, and what doesn't it guarantee?
6. Could a stranger run my demo in Codespaces without asking me anything?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x7t1` | Fri 13 Nov | Build | 150 | Build the frontend: connect wallet, create an escrow, release or refund, and list events | — |
| ☐ | `x7t2` | Sat 14 Nov | Write | 30 | Record a 2-minute demo and write the log | — |
| ☐ | `x7t3` | Tue 10 Nov | Learn | 45 | Updraft Smart Contract Security: the introduction section | [Smart Contract Security](https://updraft.cyfrin.io/courses/security) |
| ☐ | `x7t4` | Tue 10 Nov | Learn | 20 | Read two rekt.news post-mortems: one re-entrancy, one oracle manipulation | [rekt.news](https://rekt.news/) |
| ☐ | `x7t5` | Sat 14 Nov | Build | 105 | Ethernaut levels 0–5 | [ethernaut.openzeppelin.com](https://ethernaut.openzeppelin.com/) |
| ☐ | `x7t6` | Sat 14 Nov | Write | 30 | Log: for each level, the bug in one line | — |
| ☐ | `x7t7` | Sat 14 Nov | Build | 60 | Install Slither and run it on your ERC-20, Escrow and NFT | [Slither](https://github.com/crytic/slither) |
| ☐ | `x7t8` | Tue 10 Nov | Learn | 30 | Foundry docs: invariant testing | [Foundry guides](https://www.getfoundry.sh/guides) |
| ☐ | `x7t9` | Thu 12 Nov | AI | 30 | Give an LLM one vulnerable Ethernaut contract without the hint. Compare its answer with what you found yourself | [Ethernaut](https://ethernaut.openzeppelin.com/) |
| ☐ | `x7t10` | Sat 14 Nov | Capstone | 30 | Capstone B: point your escrow frontend at Marketplace.sol so you can list, buy and release from the browser | — |
| ☐ | `x7t11` | Sat 14 Nov | Capstone | 30 | Integration test v1 (test/Integration.t.sol): mock credential → list → pay in TestUSD → release, passing in CI alongside the demo | — |
| ☐ | `x7t12` | Sat 14 Nov | Capstone | 20 | Demo stage 4 (payment into escrow). Then open your repo in GitHub Codespaces from the README badge and run make demo there, to confirm a stranger can run it with no setup | — |
| ☐ | `x7t13` | Sat 14 Nov | Capstone | 20 | Invariant tests: escrow always holds what it owes, and TestUSD's total supply equals the sum of balances (invariant_EscrowSolvent, invariant_SupplyEqualsBalances) | [Foundry guides (invariant testing)](https://www.getfoundry.sh/guides) |
| ☐ | `x7t14` | Sat 14 Nov | Build | 45 | Decentralised storage and web3 logins: pin your block 6 NFT's metadata to IPFS and compare it with the fully on-chain version, then read how ENS names and Sign-In with Ethereum (EIP-4361) work. Note in your log whether week 12's admin console needs SIWE (hint: the contract already checks the role) | [IPFS: content addressing (CIDs)](https://docs.ipfs.tech/concepts/content-addressing/) · [ENS docs](https://docs.ens.domains/) · [EIP-4361: Sign-In with Ethereum](https://eips.ethereum.org/EIPS/eip-4361) |

## Block 8 · 16 Nov – 22 Nov · Deeper exploits and your own audit → Project 4

**Goal:** Solve harder levels, then treat your earlier contracts as someone else's and write a real findings report.  
**Ship:** Project 4: AUDIT.md with severity-ranked findings, invariant tests and fixes  
**Time:** 10.75 h

**By the end of this block you can:**

- Solve harder exploits, including re-entrancy, storage "privacy" and Damn Vulnerable DeFi's Unstoppable
- Audit your own contracts and write severity-ranked findings with fixes
- Compare what AI, tools and your own review each find
- Write attack tests that fail exactly the way TESTING.md says
- Explain how DAOs govern with token voting, and how governance can be attacked

**Check yourself** (answer in your log on Saturday):

1. Why is "private" state not private on a blockchain?
2. What is the most severe finding in my AUDIT.md, and how did I fix it?
3. What did the LLM find that Slither missed, and what did it get wrong?
4. What breaks if one of my mocks is swapped for a malicious contract?
5. How did the Beanstalk attacker pass a governance vote in one transaction, and which defences (timelocks, vote snapshots) would have stopped it?
6. Who should hold the issuer and arbiter roles in my trust stack, and why?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x8t1` | Fri 20 Nov | Build | 135 | Ethernaut: Re-entrancy, Elevator, Privacy and one more level of your choice | [Ethernaut](https://ethernaut.openzeppelin.com/) |
| ☐ | `x8t2` | Tue 17 Nov | Learn | 45 | ConsenSys best practices: the attacks section | [Smart contract best practices](https://consensys.github.io/smart-contract-best-practices/) |
| ☐ | `x8t3` | Sat 21 Nov | Write | 30 | Log: which Slither findings were real and which were noise | — |
| ☐ | `x8t4` | Fri 20 Nov | Build | 60 | Damn Vulnerable DeFi: challenge 1 (Unstoppable) | [damnvulnerabledefi.xyz](https://www.damnvulnerabledefi.xyz/) |
| ☐ | `x8t5` | Sat 21 Nov | Build | 165 | Audit your Escrow, ERC-20 and NFT: write each finding (severity, description, fix), add invariant tests, and fix the code | — |
| ☐ | `x8t6` | Sat 21 Nov | Write | 30 | Log: the one mistake you'll never make again | — |
| ☐ | `x8t7` | Tue 17 Nov | Learn | 15 | Read one more rekt.news post-mortem and match it to a bug class you now know | [rekt.news](https://rekt.news/) |
| ☐ | `x8t8` | Tue 17 Nov | AI | 30 | AI-assisted audit: run an LLM over your escrow and compare its findings with Slither's and your own. Count true and false positives in AUDIT.md | — |
| ☐ | `x8t9` | Sat 21 Nov | Explain | 45 | Explainer #4: write "What I learned auditing my own smart contracts" in blog/ (600–900 words, weeks 7–8). Optional: record a 5-minute video teaching it and link it in the post | — |
| ☐ | `x8t10` | Sat 21 Nov | Capstone | 15 | Add the integration to your audit: what breaks if a mock is swapped for a malicious contract, or a batch id is reused? Note findings in AUDIT.md | — |
| ☐ | `x8t11` | Sat 21 Nov | Capstone | 30 | Attack tests in test/Attacks.t.sol: replayed signature, reused batch id, re-entrancy on release, a stranger releasing escrow. Each must fail the way TESTING.md says | — |
| ☐ | `x8t12` | Thu 19 Nov | Apps | 45 | DAOs and on-chain governance: how proposals, token voting, quorums and timelocks work (OpenZeppelin Governor), then the Beanstalk attack (April 2022), where a flash loan bought enough votes to drain the treasury in one transaction. In your log, for next week's SPEC.md: who should hold the trust stack's issuer and arbiter roles, you, a Safe multisig, or a DAO of cooperatives? | [ethereum.org: DAOs](https://ethereum.org/en/dao/) · [OpenZeppelin: on-chain governance](https://docs.openzeppelin.com/contracts/governance) · [Beanstalk - REKT](https://rekt.news/beanstalk-rekt) · [Updraft: DAOs (optional build)](https://updraft.cyfrin.io/courses/advanced-foundry/daos/create-governor-contract) |

## Block 9 · 23 Nov – 29 Nov · AMMs, oracles, rollups → Project 5, and the capstone spec

**Goal:** Build x·y=k, see why a spot price is a dangerous oracle, compare rollups by their real risks, and decide exactly what your capstone puts on-chain.  
**Ship:** Project 5 (AMM with a fuzz test), the 'do you need a blockchain?' memo, and SPEC.md for the capstone  
**Time:** 11.5 h

**By the end of this block you can:**

- Build a constant-product AMM and prove with a fuzz test that k never decreases
- Explain why an AMM spot price is a dangerous oracle, and how Chainlink feeds differ
- Compare rollups by their real risks using L2BEAT
- Decide with numbers whether a use case needs a blockchain at all
- Explain why stablecoins matter in Africa, and what regulators worry about
- Write the trust stack's SPEC.md and replace the credential mock with the real registry

**Check yourself** (answer in your log on Saturday):

1. What slippage did my tests show for the same trade on a small pool and a large one?
2. How could an attacker move my AMM's price inside one transaction, and who would lose?
3. What can Base's operator do to my funds today, according to L2BEAT?
4. Sending $200 to Nigeria or Rwanda: which route was cheapest, and what costs remain when the recipient cashes out?
5. For each trust-stack part, what is on-chain, what is off-chain, and why?
6. What does revoking a credential stop, and what can't it undo?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x9t1` | Tue 24 Nov | Learn | 30 | Finematics: the AMM and Uniswap explainers | [Finematics channel](https://www.youtube.com/@Finematics) |
| ☐ | `x9t2` | Tue 24 Nov | Learn | 30 | Uniswap v2 whitepaper, sections 1–3 | [Uniswap v2 whitepaper](https://uniswap.org/whitepaper.pdf) |
| ☐ | `x9t3` | Sat 28 Nov | Build | 75 | Build an AMM with addLiquidity, removeLiquidity and swap with a 0.3% fee. Fuzz-test that k never decreases | — |
| ☐ | `x9t4` | Tue 24 Nov | Learn | 60 | DeFi MOOC lecture: Oracles (Ari Juels) | [Oracles lecture](https://www.youtube.com/watch?v=vFcW18ZpPZ4) |
| ☐ | `x9t5` | Thu 26 Nov | Learn | 30 | Chainlink: Data Feeds overview | [docs.chain.link](https://docs.chain.link/) |
| ☐ | `x9t6` | Thu 26 Nov | Learn | 30 | Vitalik Buterin: An incomplete guide to rollups | [vitalik.eth.limo](https://vitalik.eth.limo/general/2021/01/05/rollup.html) |
| ☐ | `x9t7` | Thu 26 Nov | Learn | 30 | L2BEAT: read the FAQ, then compare two rollups on its risk dashboard | [L2BEAT](https://l2beat.com/) · [L2BEAT FAQ](https://l2beat.com/faq) |
| ☐ | `x9t8` | Sat 28 Nov | Write | 60 | Write a 'do you need a blockchain?' memo for remittances, land registry and cold-chain provenance | — |
| ☐ | `x9t9` | Sat 28 Nov | Write | 90 | Capstone SPEC.md for the whole trust stack: actors, trust assumptions, what is on-chain vs. off-chain for each part, the threat model, and the end-to-end test you'll write in week 11 | — |
| ☐ | `x9t10` | Sat 28 Nov | Write | 30 | Log: slippage on a small pool vs. a large one, with numbers from your tests | — |
| ☐ | `x9t11` | Thu 26 Nov | Crypto | 30 | Commitments and Merkle proofs. Write a Merkle proof verifier in Solidity and test it (you'll reuse it in the capstone) | [OpenZeppelin MerkleProof](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleProof) |
| ☐ | `x9t12` | Fri 27 Nov | Apps | 30 | Payments and remittances in Africa: compare the cost of sending $200 to Nigeria or Rwanda by bank, mobile money and a stablecoin. Add the numbers to your 'do you need a blockchain?' memo | [World Bank: Remittance Prices Worldwide](https://remittanceprices.worldbank.org/) |
| ☐ | `x9t13` | Sat 28 Nov | Capstone | 60 | Capstone D: CredentialRegistry.sol with roles (farmer, cooperative, transporter, inspector, buyer). An issuer signs EIP-712 credentials, each cohort is Merkle-rooted on-chain, and isValid(account, role) replaces the mock in the integration test | [EIP-712](https://eips.ethereum.org/EIPS/eip-712) |
| ☐ | `x9t14` | Sat 28 Nov | Capstone | 15 | Credential tests: a revoked credential can't sign or list (test_RevertWhen_RevokedCredential). Switch demo stage 2 from the mock to the real registry | — |
| ☐ | `x9t15` | Fri 27 Nov | Apps | 45 | Stablecoins II, why they matter and why regulators worry: how people in Sub-Saharan Africa use them (remittances, saving against inflation, trade), the BIS argument that they fail as money, and the rules: EU MiCA, the US GENIUS Act, and what the National Bank of Rwanda and Central Bank of Nigeria currently say. Check the latest; these rules change | [Chainalysis: Sub-Saharan Africa crypto adoption 2025](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2025/) · [BIS Annual Economic Report 2025, ch. III](https://www.bis.org/publ/arpdf/ar2025e3.htm) · [EU MiCA (ESMA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica) · [GENIUS Act resource center (Arnold & Porter)](https://www.arnoldporter.com/en/perspectives/topics/the-genius-act-and-stablecoin-regulation-resource-center) |
| ☐ | `x9t16` | Sat 28 Nov | Explain | 45 | Stablecoin write-up: "Digital dollars for Africa? What stablecoins could fix and what they risk" in blog/ (600–900 words). Cover how they hold their peg, one failure, one real use case with numbers from your remittance comparison, the rules, and your honest verdict. Optional: a 5-minute video | — |

## Block 10 · 30 Nov – 6 Dec · Capstone I: the device signs, the contract verifies

**Goal:** Make an ESP32 hold its own key and sign batched readings, and write the contract that accepts only signatures from registered devices.  
**Ship:** ESP32 firmware that signs Merkle roots of readings, and a tested SensorRegistry contract  
**Time:** 10 h

**By the end of this block you can:**

- Explain how hardware wallets and trusted execution protect keys, and where they fail
- Generate a key on an ESP32 (or a simulator) and sign sensor readings
- Batch readings into a Merkle tree and sign only the root
- Accept on-chain only roots signed by registered devices (ecrecover)
- Explain what anchoring proves (this device signed this data) and what it can't (that the reading is true)

**Check yourself** (answer in your log on Saturday):

1. Where does my ESP32's private key live, and how could someone holding the board extract it?
2. Why sign a Merkle root instead of every reading? What does that save on-chain?
3. Does my firmware reproduce test_vectors.json byte for byte? If not, where do the bytes differ?
4. What does ecrecover return for a tampered reading, and how does my contract reject it?
5. A sensor sitting in ice honestly signs "2 °C" while the tomatoes are warm. What does my system prove, and what does it miss?
6. How does OpenTimestamps anchor millions of hashes with one transaction?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x10t1` | Tue 1 Dec | Learn | 15 | Browse the Trezor firmware repo: the crypto folder and the security docs | [trezor-firmware](https://github.com/trezor/trezor-firmware) |
| ☐ | `x10t2` | Tue 1 Dec | Learn | 15 | SGX.Fail: skim the list of TEE attacks | [sgx.fail](https://sgx.fail/) |
| ☐ | `x10t3` | Tue 1 Dec | Learn | 15 | OpenZeppelin ECDSA and MessageHashUtils docs | [OZ ECDSA](https://docs.openzeppelin.com/contracts/5.x/api/utils#ECDSA) |
| ☐ | `x10t4` | Tue 1 Dec | Learn | 15 | Study how OpenTimestamps anchors many hashes with one transaction | [opentimestamps.org](https://opentimestamps.org/) |
| ☐ | `x10t5` | Thu 3 Dec | Build | 150 | Capstone A: on an ESP32, generate a key with micro-ecc or trezor-crypto, hash a sensor reading with keccak256, and print r, s, v and the address. If the board fights you, start with a Python device simulator and swap the board in later | [micro-ecc](https://github.com/kmackay/micro-ecc) · [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/) |
| ☐ | `x10t6` | Fri 4 Dec | Build | 90 | Batch readings on the device or a gateway: build a Merkle tree and sign the root instead of each reading | [OZ MerkleProof](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleProof) |
| ☐ | `x10t7` | Sat 5 Dec | Build | 165 | Capstone A: ProvenanceAnchor.sol as a trace registry. createBatch(product, policyId); recordEvent(batchId, stage, dataRoot) only by an actor with the right role credential and in the right order; accept sensor Merkle roots only from registered devices (ecrecover). Test with vm.sign, then with a real ESP32 signature | — |
| ☐ | `x10t8` | Sat 5 Dec | Write | 30 | Log: what this proves (the device signed it) and what it doesn't (the reading is true) | — |
| ☐ | `x10t9` | Sat 5 Dec | Explain | 45 | Explainer #5: write "Teaching a sensor to sign its own data" in blog/ (600–900 words, weeks 9–10). Optional: record a 5-minute video teaching it and link it in the post | — |
| ☐ | `x10t10` | Sat 5 Dec | Capstone | 30 | Replace the provenance mock in the integration test: create a batch, record its events and a signed sensor root, list it, pay, release. Update demo.sh | — |
| ☐ | `x10t11` | Sat 5 Dec | Capstone | 30 | Firmware checks: run make vectors, make your ESP32 reproduce test_vectors.json byte for byte, and add firmware/tools/Vectors.t.sol.example to test/ so CI proves tampered and unregistered readings are rejected. Demo stage 5 uses sample_readings.json, so it runs without hardware | — |

## Block 11 · 7 Dec – 13 Dec · Capstone II: connect all four parts and ship

**Goal:** Deploy the whole trust stack to an L2 testnet, prove it works end to end with one test, and publish it.  
**Ship:** All four parts on an L2 testnet, one end-to-end test passing, and a README with an architecture diagram, demo video and post  
**Time:** 10 h

**By the end of this block you can:**

- Deploy and verify all four contracts on Base Sepolia with a keystore, never a plain-text key
- Run the end-to-end flow: credential, batch, journey, listing, payment, then settlement or refund
- Enforce the product policy on-chain, with one compliant and one failing batch
- Publish a demo site and trace page that anyone can use without logging in
- Argue honestly, part by part, whether a blockchain beats a shared database

**Check yourself** (answer in your log on Saturday):

1. Can I run the whole demo from a fresh clone with one command, and does CI agree?
2. What happens to the buyer's TestUSD when a reading is out of range, and which test proves it?
3. Who can do what in my system, and what is the worst thing each role could do?
4. For which of the four parts would a shared database be just as good, and why?
5. Does make smoke pass against the live deployment?
6. Can someone who has never seen my repo follow a batch on the trace page?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x11t1` | Tue 8 Dec | Build | 90 | Deploy all four parts to an L2 testnet such as Base Sepolia: TestUSD, Marketplace, CredentialRegistry and ProvenanceAnchor. Verify each contract on the explorer | [Base docs (Base Sepolia testnet)](https://docs.base.org/) |
| ☐ | `x11t2` | Fri 11 Dec | Build | 150 | End-to-end flow in the integration test and demo.sh: a credentialed farmer creates a batch, a transporter records pickup and delivery with the ESP32's signed readings, the batch is checked against its policy, and the buyer's TestUSD in escrow is released only if the batch is compliant; otherwise the buyer is refunded | — |
| ☐ | `x11t3` | Fri 11 Dec | Build | 15 | Capstone C demo: a script that sends a TestUSD payment with a receipt event and prints its cost and time next to the bank and mobile-money figures from week 9 | — |
| ☐ | `x11t4` | Fri 11 Dec | Build | 45 | Security pass on all four contracts: Slither, your Project 4 checklist, and invariant tests | [Slither](https://github.com/crytic/slither) |
| ☐ | `x11t5` | Sat 12 Dec | Write | 45 | For each of the four parts, argue honestly whether a blockchain beats a shared database, and say so where it doesn't | — |
| ☐ | `x11t6` | Sat 12 Dec | Write | 90 | README with an architecture diagram, a 5-minute demo video of the full flow, and the capstone post | — |
| ☐ | `x11t7` | Sat 12 Dec | Write | 30 | Log: what you'd change with another month | — |
| ☐ | `x11t8` | Tue 8 Dec | AI | 15 | GenAI provenance: read the C2PA overview, then add a paragraph to your capstone README on how the same sign-and-anchor pattern could prove where a photo or AI-generated output came from | [C2PA](https://c2pa.org/) |
| ☐ | `x11t9` | Sat 12 Dec | Capstone | 45 | Compliance check: anyone can mark a batch non-compliant by submitting a signed reading outside the policy range with its Merkle proof, and a missing step or wrong role also fails. Test one compliant batch and one failing batch | — |
| ☐ | `x11t10` | Sat 12 Dec | Capstone | 30 | Demo site v1, open to everyone with no login: Explore (sample batches), Market (listings) and Trace (enter a batch id or scan its QR code to see the journey, who signed each step, the readings summary and compliance status), reading from your deployed contracts. Build it in trust-stack/app/site/ following trust-stack/app/README.md | — |
| ☐ | `x11t11` | Sat 12 Dec | Capstone | 30 | Deploy for real: forge script with your keystore account to Base Sepolia, verify on Basescan, record addresses and read-only checks in deployments/base-sepolia.json (copy the example), and run make smoke until every check is green | [Base docs](https://docs.base.org/) |
| ☐ | `x11t12` | Sat 12 Dec | Capstone | 15 | Make it public: put the trace page in trust-stack/app/site/ so it publishes to GitHub Pages, then check the README's Trust stack badge, Codespaces button and DEMO.md all work from a logged-out browser | — |

## Block 12 · 14 Dec – 20 Dec · Agents with wallets, verifiable AI, and a retrospective → Project 7

**Goal:** Give an LLM agent spending power that a contract limits, try to break it, and learn what zkML can and can't prove.  
**Ship:** Project 7 (guarded agent wallet with a red-team report), an implications memo, and your retrospective  
**Time:** 10 h

**By the end of this block you can:**

- Give an AI agent a contract wallet with limits, and show which limits held under prompt injection
- Explain account abstraction (ERC-4337, EIP-7702) and agent payments (x402)
- Explain what zk-SNARKs and zkML can and can't prove
- Issue verifiable credentials for your own learning, backed by commit hashes
- Seed the live demo and run an admin console gated by an on-chain role
- Reflect on what you learned and choose your next direction

**Check yourself** (answer in your log on Saturday):

1. Which injection prompts fooled the model, and did the contract still block the payment?
2. What does my EZKL proof actually prove about the model, and what doesn't it?
3. What is the difference between an ordinary account, an ERC-4337 smart account and an EIP-7702 delegated account?
4. If someone doubts my week 5 credential, how can they check it themselves?
5. What would I build with one more month, and why?
6. Of tokenised assets, DAOs, prediction markets and DePIN, which has the most honest need for a blockchain?

| | ID | Due | Kind | Min | Task | Resources |
|---|---|---|---|---|---|---|
| ☐ | `x12t1` | Tue 15 Dec | Learn | 30 | Vitalik Buterin: The promise and challenges of crypto + AI applications | [vitalik.eth.limo](https://vitalik.eth.limo/general/2024/01/30/cryptoai.html) |
| ☐ | `x12t2` | Tue 15 Dec | Learn | 30 | ERC-4337 motivation, then EIP-7702 | [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) · [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) |
| ☐ | `x12t3` | Tue 15 Dec | Learn | 30 | x402 docs: the quickstart | [docs.x402.org](https://docs.x402.org/) · [x402 on GitHub](https://github.com/x402-foundation/x402) |
| ☐ | `x12t4` | Tue 15 Dec | Learn | 20 | ERC-8004 abstract and motivation | [ERC-8004](https://eips.ethereum.org/EIPS/eip-8004) |
| ☐ | `x12t5` | Thu 17 Dec | Learn | 20 | Simon Willison on prompt injection: two posts | [Prompt injection series](https://simonwillison.net/series/prompt-injection/) |
| ☐ | `x12t6` | Sat 19 Dec | Build | 105 | Build a guarded agent wallet that pays through your TestUSD rail: a contract wallet with a daily cap and a recipient allowlist, and an LLM with a single 'pay' tool. Try five injection prompts and record what the contract blocked | — |
| ☐ | `x12t7` | Sat 19 Dec | Write | 30 | Log: which defences held in the model and which only held in the contract | — |
| ☐ | `x12t8` | Thu 17 Dec | Learn | 30 | Vitalik Buterin: an approximate introduction to how zk-SNARKs are possible | [vitalik.eth.limo](https://vitalik.eth.limo/general/2021/01/26/snarks.html) |
| ☐ | `x12t9` | Thu 17 Dec | Learn | 30 | EZKL: read the getting-started guide and run its example (the full build is optional) | [EZKL docs](https://docs.ezkl.xyz/getting-started/) · [ezkl on GitHub](https://github.com/zkonduit/ezkl) |
| ☐ | `x12t10` | Sat 19 Dec | Write | 45 | Memo: custody for autonomous agents, accountability, energy, and the current rules in Rwanda, Nigeria and the EU (check these; they change) | [EU MiCA (ESMA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica) |
| ☐ | `x12t11` | Sat 19 Dec | Write | 60 | Retrospective: pick the next direction (ZK, auditing, DePIN, or agent payments) | — |
| ☐ | `x12t12` | Sat 19 Dec | Build | 20 | Proof of learning (Capstone D): issue yourself a credential for each finished week, with that week's folder commit hash as evidence, and verify one on the testnet | — |
| ☐ | `x12t13` | Thu 17 Dec | Crypto | 30 | Zero-knowledge in practice. Read the first chapters of the RareSkills ZK Book, then revisit what your EZKL proof actually proved | [RareSkills ZK Book (free)](https://www.rareskills.io/zk-book) |
| ☐ | `x12t14` | Fri 18 Dec | Apps | 30 | Other applications, one paragraph each on who has to trust whom: tokenised real-world assets, DAOs and on-chain governance, prediction markets, and DePIN networks | [ethereum.org: DAOs](https://ethereum.org/en/dao/) · [Helium docs (DePIN example)](https://docs.helium.com/) |
| ☐ | `x12t15` | Sat 19 Dec | Capstone | 30 | Seed the live demo: put throwaway actor keys in trust-stack/.env (never your real wallet), run make seed so the sample batches, listings and one failing batch exist on Base Sepolia, then make smoke. Rerun make seed any time to top it up | [Foundry: keystores (cast wallet)](https://getfoundry.sh/cast/reference/cast-wallet-import) |
| ☐ | `x12t16` | Sat 19 Dec | Capstone | 60 | Admin console: an Admin tab that appears only when the connected wallet holds the issuer role on-chain. From it, issue a credential, create a batch, record a step and anchor readings, so you can show something new live. The contracts enforce the role; the page only hides the buttons | [viem: writing to contracts](https://viem.sh/docs/contract/writeContract) |
