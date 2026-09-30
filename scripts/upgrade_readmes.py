#!/usr/bin/env python3
"""Update the week READMEs to the 30 Sep 2026 plan (167 tasks). Run once from the repo root:

    python scripts/upgrade_readmes.py

It does two things, and skips anything that's already there, so it's safe to run twice:
1. Adds any of these tasks that are missing, as the last checkbox of their week, so their
   IDs match the tracker: x4t13 web3, x5t15 stablecoins I, x6t20 NFTs, x7t14 IPFS/ENS,
   x8t12 DAOs, x9t15 stablecoins II, x9t16 stablecoin write-up.
2. Adds an "Objectives and check-yourself" section to every week README, just below the plan.
   It uses plain bullets (no checkboxes), so it doesn't change any task counts.
Then it rebuilds the progress table and progress.json.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDER_RE = re.compile(r"^week(\d+)(?:-(\d+))?-")
BOX_RE = re.compile(r"^\s*[-*] \[( |x|X)\] ", re.M)
WEEK_HEAD_RE = re.compile(r"^## Week (\d+):", re.M)
SECTION = "## Objectives and check-yourself"
DATA = json.loads(r"""{"obj": {"1": {"obj": ["Explain how hash pointers link blocks, and why editing one block breaks every block after it", "Explain what proof-of-work costs an attacker, and measure how the work grows with each extra leading zero", "Sign and verify a transaction on secp256k1, and say what a signature proves and what it doesn't", "Build a Merkle root and explain how it proves one transaction is in a block"], "q": ["If I change one transaction in block 2 of 10, which check fails first, and why do all later blocks fail too?", "Each extra leading hex zero multiplies the expected work by how much? What did my timings show?", "Which hash property (preimage, second-preimage or collision resistance) does proof-of-work rely on, and why that one?", "What exactly does a valid signature prove? Name one thing it doesn't prove.", "How many hashes do I need to prove one transaction is in a block of 1,024 transactions?", "Can I explain the chain to a non-technical friend in two minutes, without notes?"]}, "2": {"obj": ["Explain the UTXO model and why Bitcoin has no account balances", "Run a regtest node and move coins with bitcoin-cli", "Build, sign, broadcast and decode a raw transaction, and explain every field", "Explain difficulty retargeting, the most-work chain rule, and what a 51% attacker can and can't do", "Explain in one paragraph what Schnorr signatures and Taproot add to ECDSA"], "q": ["Where is \"my balance\" actually stored, and how does a wallet work it out?", "In my raw transaction, which script locks the output and which one unlocks it?", "Why did I have to mine 101 blocks before I could spend anything?", "What can a 51% attacker do to recent transactions, and why can't they take my coins?", "Where is the fee in my transaction? (It isn't a field.)", "If half the miners switched off tomorrow, what would happen to block times, and for how long?"]}, "3": {"obj": ["State the consensus problem (state machine replication) and its safety and liveness properties", "Explain why classic Byzantine agreement needs identities and a two-thirds honest majority, and how proof-of-work avoids identities", "Observe forks and reorgs in your own simulation and relate them to network delay", "Explain how proof-of-stake picks proposers, what finality means in Gasper, and what slashing punishes", "Compare PoW and PoS on security, finality, energy and who can take part"], "q": ["What is the difference between safety and liveness? Which one did the partition in my simulation break?", "How did longer network delays change the fork rate in my simulation, and why?", "What does selfish mining show about the \"honest majority\" assumption?", "How does proof-of-stake stop someone creating a million fake validators?", "What does \"finalised\" mean on Ethereum, and roughly how long does it take?", "Who actually decided Bitcoin's block-size dispute and Ethereum's DAO fork? What does that say about \"code is law\"?"]}, "4": {"obj": ["Explain accounts (externally owned vs contract), gas and fees, and how the EVM runs a transaction", "Deploy a contract to Sepolia from a testnet-only wallet", "Write small contracts with mappings, modifiers, events and custom errors from memory", "Derive an Ethereum address from a public key with Keccak-256", "Compare custodial wallets, self-custody, centralised exchanges and DEXs", "Explain what \"web3\" claims, and the strongest case against it"], "q": ["How does an Ethereum account differ from a Bitcoin UTXO?", "Why does a failed transaction still cost gas?", "What is the difference between storage and memory, and which costs more?", "From memory: how do I get from a private key to an address?", "What did the FTX collapse show about \"not your keys, not your coins\"?", "Which web3 claims will this plan let me test myself, and what do I think of them today?"]}, "5": {"obj": ["Set up a Foundry project and write unit and fuzz tests", "Implement ERC-20 from the spec, including allowances, and explain the approval race", "Deploy with forge script and verify the source on Etherscan", "Compare your token with OpenZeppelin's and explain the differences", "Explain how fiat-backed, crypto-backed and algorithmic stablecoins hold their peg, and why UST failed", "Start the capstone: TestUSD with tests, demo stage 1, and the Trust stack workflow green"], "q": ["What does approve plus transferFrom let a spender do, and what is the known approval race?", "What did my fuzz tests find, or why did they find nothing, and what would be a stronger property to test?", "Why does TestUSD use 6 decimals, and what goes wrong when two tokens' decimals differ?", "What would have to back TestUSD for it to be a real stablecoin?", "Why did UST collapse for good while USDC got its peg back?", "Is the Trust stack workflow green, and can I say what each job checks?"]}, "6": {"obj": ["Write a contract that holds value (escrow) using checks-effects-interactions, with a test for every path", "Explain re-entrancy and show how your escrow avoids it", "Build an ERC-721 whose metadata and image live on-chain", "Sign and verify EIP-712 typed data with replay protection", "Explain how NFT marketplaces use signed orders, escrow and royalties, and what NFTs are really used for today", "Define the trust stack's interfaces, product policy and rules-to-tests table"], "q": ["List every state my escrow can be in. Which transitions can only the arbiter trigger?", "Where exactly would a re-entrancy attack hit my escrow if I sent the money before updating state?", "What does my NFT actually own, and what would break if its metadata lived on an ordinary web server?", "What stops an EIP-712 signature being replayed on another chain or another contract?", "Why did most marketplaces stop enforcing royalties, and what does that say about on-chain rules versus off-chain choices?", "Should a produce batch be an NFT, or is a record in the trace registry enough? Why?"]}, "7": {"obj": ["Connect a web frontend to your contracts so a non-developer could use it", "Recognise common vulnerability classes by exploiting them (Ethernaut 0–5)", "Run Slither and tell real findings from noise", "Write invariant tests for escrow solvency and token supply", "Store NFT metadata on IPFS, and explain content addressing, ENS and Sign-In with Ethereum"], "q": ["What happens, step by step, between clicking \"Buy\" and the transaction being mined?", "For each Ethernaut level I solved, what was the bug in one line?", "Which Slither findings were real, and why were the others noise?", "What must always be true of my escrow, and how does the invariant test try to break it?", "What does an IPFS CID guarantee, and what doesn't it guarantee?", "Could a stranger run my demo in Codespaces without asking me anything?"]}, "8": {"obj": ["Solve harder exploits, including re-entrancy, storage \"privacy\" and Damn Vulnerable DeFi's Unstoppable", "Audit your own contracts and write severity-ranked findings with fixes", "Compare what AI, tools and your own review each find", "Write attack tests that fail exactly the way TESTING.md says", "Explain how DAOs govern with token voting, and how governance can be attacked"], "q": ["Why is \"private\" state not private on a blockchain?", "What is the most severe finding in my AUDIT.md, and how did I fix it?", "What did the LLM find that Slither missed, and what did it get wrong?", "What breaks if one of my mocks is swapped for a malicious contract?", "How did the Beanstalk attacker pass a governance vote in one transaction, and which defences (timelocks, vote snapshots) would have stopped it?", "Who should hold the issuer and arbiter roles in my trust stack, and why?"]}, "9": {"obj": ["Build a constant-product AMM and prove with a fuzz test that k never decreases", "Explain why an AMM spot price is a dangerous oracle, and how Chainlink feeds differ", "Compare rollups by their real risks using L2BEAT", "Decide with numbers whether a use case needs a blockchain at all", "Explain why stablecoins matter in Africa, and what regulators worry about", "Write the trust stack's SPEC.md and replace the credential mock with the real registry"], "q": ["What slippage did my tests show for the same trade on a small pool and a large one?", "How could an attacker move my AMM's price inside one transaction, and who would lose?", "What can Base's operator do to my funds today, according to L2BEAT?", "Sending $200 to Nigeria or Rwanda: which route was cheapest, and what costs remain when the recipient cashes out?", "For each trust-stack part, what is on-chain, what is off-chain, and why?", "What does revoking a credential stop, and what can't it undo?"]}, "10": {"obj": ["Explain how hardware wallets and trusted execution protect keys, and where they fail", "Generate a key on an ESP32 (or a simulator) and sign sensor readings", "Batch readings into a Merkle tree and sign only the root", "Accept on-chain only roots signed by registered devices (ecrecover)", "Explain what anchoring proves (this device signed this data) and what it can't (that the reading is true)"], "q": ["Where does my ESP32's private key live, and how could someone holding the board extract it?", "Why sign a Merkle root instead of every reading? What does that save on-chain?", "Does my firmware reproduce test_vectors.json byte for byte? If not, where do the bytes differ?", "What does ecrecover return for a tampered reading, and how does my contract reject it?", "A sensor sitting in ice honestly signs \"2 °C\" while the tomatoes are warm. What does my system prove, and what does it miss?", "How does OpenTimestamps anchor millions of hashes with one transaction?"]}, "11": {"obj": ["Deploy and verify all four contracts on Base Sepolia with a keystore, never a plain-text key", "Run the end-to-end flow: credential, batch, journey, listing, payment, then settlement or refund", "Enforce the product policy on-chain, with one compliant and one failing batch", "Publish a demo site and trace page that anyone can use without logging in", "Argue honestly, part by part, whether a blockchain beats a shared database"], "q": ["Can I run the whole demo from a fresh clone with one command, and does CI agree?", "What happens to the buyer's TestUSD when a reading is out of range, and which test proves it?", "Who can do what in my system, and what is the worst thing each role could do?", "For which of the four parts would a shared database be just as good, and why?", "Does make smoke pass against the live deployment?", "Can someone who has never seen my repo follow a batch on the trace page?"]}, "12": {"obj": ["Give an AI agent a contract wallet with limits, and show which limits held under prompt injection", "Explain account abstraction (ERC-4337, EIP-7702) and agent payments (x402)", "Explain what zk-SNARKs and zkML can and can't prove", "Issue verifiable credentials for your own learning, backed by commit hashes", "Seed the live demo and run an admin console gated by an on-chain role", "Reflect on what you learned and choose your next direction"], "q": ["Which injection prompts fooled the model, and did the contract still block the payment?", "What does my EZKL proof actually prove about the model, and what doesn't it?", "What is the difference between an ordinary account, an ERC-4337 smart account and an EIP-7702 delegated account?", "If someone doubts my week 5 credential, how can they check it themselves?", "What would I build with one more month, and why?", "Of tokenised assets, DAOs, prediction markets and DePIN, which has the most honest need for a blockchain?"]}}, "tasks": {"x4t13": {"marker": "What \"web3\" means", "line": "- [ ] Apps (30 min): What \"web3\" means, and the case against it: read ethereum.org's introduction to web3, then Moxie Marlinspike's \"My first impressions of web3\". In your log, list which web3 claims this plan lets you test yourself, and your view today  \n  [ethereum.org: what is web3?](https://ethereum.org/en/web3/) · [Moxie Marlinspike: My first impressions of web3](https://moxie.org/2022/01/07/web3-first-impressions.html)", "week": 4, "num": 13}, "x5t15": {"marker": "Stablecoins I", "line": "- [ ] Apps (45 min): Stablecoins I, how they hold $1: fiat-backed (USDC, USDT) and what their reserve reports actually show; crypto-collateralised (DAI); algorithmic. Then two failures: TerraUST's collapse (May 2022) and USDC's brief depeg when Silicon Valley Bank failed (March 2023). Note in your log which design TestUSD copies, and what would have to back it for real  \n  [ethereum.org: stablecoins](https://ethereum.org/en/stablecoins/) · [Circle: USDC transparency](https://www.circle.com/transparency) · [Tether: transparency](https://tether.to/en/transparency/) · [Terra (blockchain) and the UST collapse](https://en.wikipedia.org/wiki/Terra_(blockchain)) · [Federal Reserve: SVB's failure and its impact on stablecoins](https://www.federalreserve.gov/econres/notes/feds-notes/in-the-shadow-of-bank-run-lessons-from-the-silicon-valley-bank-failure-and-its-impact-on-stablecoins-20251217.html)", "week": 5, "num": 15}, "x6t20": {"marker": "NFTs beyond the hype", "line": "- [ ] Apps (30 min): NFTs beyond the hype: ERC-1155 (many token types in one contract), the royalty standard EIP-2981 and why marketplaces stopped enforcing royalties, wash trading, and what NFTs are used for now (tickets, credentials, game items, real-world assets). End with a capstone question in your log: should each produce batch be an NFT, or is a record in your trace registry enough?  \n  [ethereum.org: NFTs](https://ethereum.org/en/nft/) · [EIP-1155](https://eips.ethereum.org/EIPS/eip-1155) · [EIP-2981: NFT royalties](https://eips.ethereum.org/EIPS/eip-2981)", "week": 6, "num": 20}, "x7t14": {"marker": "Decentralised storage and web3 logins", "line": "- [ ] Build (45 min): Decentralised storage and web3 logins: pin your block 6 NFT's metadata to IPFS and compare it with the fully on-chain version, then read how ENS names and Sign-In with Ethereum (EIP-4361) work. Note in your log whether week 12's admin console needs SIWE (hint: the contract already checks the role)  \n  [IPFS: content addressing (CIDs)](https://docs.ipfs.tech/concepts/content-addressing/) · [ENS docs](https://docs.ens.domains/) · [EIP-4361: Sign-In with Ethereum](https://eips.ethereum.org/EIPS/eip-4361)", "week": 7, "num": 14}, "x8t12": {"marker": "DAOs and on-chain governance", "line": "- [ ] Apps (45 min): DAOs and on-chain governance: how proposals, token voting, quorums and timelocks work (OpenZeppelin Governor), then the Beanstalk attack (April 2022), where a flash loan bought enough votes to drain the treasury in one transaction. In your log, for next week's SPEC.md: who should hold the trust stack's issuer and arbiter roles, you, a Safe multisig, or a DAO of cooperatives?  \n  [ethereum.org: DAOs](https://ethereum.org/en/dao/) · [OpenZeppelin: on-chain governance](https://docs.openzeppelin.com/contracts/governance) · [Beanstalk - REKT](https://rekt.news/beanstalk-rekt) · [Updraft: DAOs (optional build)](https://updraft.cyfrin.io/courses/advanced-foundry/daos/create-governor-contract)", "week": 8, "num": 12}, "x9t15": {"marker": "Stablecoins II", "line": "- [ ] Apps (45 min): Stablecoins II, why they matter and why regulators worry: how people in Sub-Saharan Africa use them (remittances, saving against inflation, trade), the BIS argument that they fail as money, and the rules: EU MiCA, the US GENIUS Act, and what the National Bank of Rwanda and Central Bank of Nigeria currently say. Check the latest; these rules change  \n  [Chainalysis: Sub-Saharan Africa crypto adoption 2025](https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2025/) · [BIS Annual Economic Report 2025, ch. III](https://www.bis.org/publ/arpdf/ar2025e3.htm) · [EU MiCA (ESMA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica) · [GENIUS Act resource center (Arnold & Porter)](https://www.arnoldporter.com/en/perspectives/topics/the-genius-act-and-stablecoin-regulation-resource-center)", "week": 9, "num": 15}, "x9t16": {"marker": "Stablecoin write-up", "line": "- [ ] Explain (45 min): Stablecoin write-up: \"Digital dollars for Africa? What stablecoins could fix and what they risk\" in blog/ (600–900 words). Cover how they hold their peg, one failure, one real use case with numbers from your remittance comparison, the rules, and your honest verdict. Optional: a 5-minute video", "week": 9, "num": 16}}}""")


def folders() -> dict[int, Path]:
    out = {}
    for p in ROOT.iterdir():
        m = FOLDER_RE.match(p.name)
        if p.is_dir() and m:
            a, b = int(m.group(1)), int(m.group(2) or m.group(1))
            for w in range(a, b + 1):
                out[w] = p
    return out


def plan_span(text: str, week: int) -> tuple[int, int]:
    end = text.find("\n---\n")
    end = len(text) if end < 0 else end
    start = 0
    head = next((m for m in WEEK_HEAD_RE.finditer(text) if int(m.group(1)) == week), None)
    if head:
        start = head.end()
        nxt = next((m for m in WEEK_HEAD_RE.finditer(text, head.end())), None)
        end = min(end, nxt.start()) if nxt else end
    return start, end


def add_task(path: Path, tid: str, t: dict) -> None:
    text = path.read_text(encoding="utf-8")
    start, end = plan_span(text, t["week"])
    if t["marker"] in text[start:end]:
        print(f"{tid}: already there")
        return
    have = len(list(BOX_RE.finditer(text, start, end)))
    if have != t["num"] - 1:
        print(f"{tid}: week {t['week']} has {have} tasks, expected {t['num'] - 1}; skipped. Add it by hand as task {t['num']}.")
        return
    head = text[:end].rstrip("\n")
    text = head + "\n" + t["line"] + "\n\n" + text[end:].lstrip("\n")
    path.write_text(text, encoding="utf-8")
    print(f"{tid}: added to {path.parent.name}/README.md")


def add_objectives(path: Path, weeks: list[int]) -> None:
    text = path.read_text(encoding="utf-8")
    if SECTION in text:
        print(f"{path.parent.name}: objectives already there")
        return
    parts = [SECTION, ""]
    for w in weeks:
        o = DATA["obj"][str(w)]
        if len(weeks) > 1:
            parts += [f"### Block {w}", ""]
        parts += ["**By the end of this block you can:**", ""] + [f"- {x}" for x in o["obj"]]
        parts += ["", "**Check yourself** (answer these in LEARNING_LOG.md on Saturday):", ""]
        parts += [f"{i}. {q}" for i, q in enumerate(o["q"], 1)] + [""]
    block = "\n".join(parts) + "\n"
    i = text.find("\n---\n")
    if i < 0:
        text = text.rstrip("\n") + "\n\n" + block
    else:
        cut = i + len("\n---\n")
        text = text[:cut] + "\n" + block + text[cut:]
    path.write_text(text, encoding="utf-8")
    print(f"{path.parent.name}: added objectives and check-yourself questions")


def main() -> None:
    fs = folders()
    for tid in sorted(DATA["tasks"], key=lambda k: (DATA["tasks"][k]["week"], DATA["tasks"][k]["num"])):
        t = DATA["tasks"][tid]
        if t["week"] not in fs:
            print(f"{tid}: no folder for week {t['week']}, skipped")
            continue
        add_task(fs[t["week"]] / "README.md", tid, t)
    by_folder: dict[Path, list[int]] = {}
    for w, p in sorted(fs.items()):
        by_folder.setdefault(p, []).append(w)
    for p, weeks in by_folder.items():
        if (p / "README.md").exists():
            add_objectives(p / "README.md", weeks)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "update_progress.py")], check=True)


if __name__ == "__main__":
    main()
