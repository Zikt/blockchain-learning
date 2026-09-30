<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 09](../week09-amm-and-capstone-spec/) · [Week 12 →](../week12-agent-wallet/)
<!-- NAV:END -->

# Weeks 10–11: Capstone, a four-part trust stack

## Week 10: Capstone I: the device signs, the contract verifies

**Dates:** 30 Nov – 6 Dec 2026 · **Planned time:** 10 h

**Goal:** Make an ESP32 hold its own key and sign batched readings, and write the contract that accepts only signatures from registered devices.

**Ship:** ESP32 firmware that signs Merkle roots of readings, and a tested SensorRegistry contract

### Plan
- [ ] Learn (15 min): Browse the Trezor firmware repo: the crypto folder and the security docs  
  [trezor-firmware](https://github.com/trezor/trezor-firmware)
- [ ] Learn (15 min): SGX.Fail: skim the list of TEE attacks  
  [sgx.fail](https://sgx.fail/)
- [ ] Learn (15 min): OpenZeppelin ECDSA and MessageHashUtils docs  
  [OZ ECDSA](https://docs.openzeppelin.com/contracts/5.x/api/utils#ECDSA)
- [ ] Learn (15 min): Study how OpenTimestamps anchors many hashes with one transaction  
  [opentimestamps.org](https://opentimestamps.org/)
- [ ] Build (150 min): Capstone A: on an ESP32, generate a key with micro-ecc or trezor-crypto, hash a sensor reading with keccak256, and print r, s, v and the address. If the board fights you, start with a Python device simulator and swap the board in later  
  [micro-ecc](https://github.com/kmackay/micro-ecc) · [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [ ] Build (90 min): Batch readings on the device or a gateway: build a Merkle tree and sign the root instead of each reading  
  [OZ MerkleProof](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleProof)
- [ ] Build (165 min): Capstone A: ProvenanceAnchor.sol as a trace registry. createBatch(product, policyId); recordEvent(batchId, stage, dataRoot) only by an actor with the right role credential and in the right order; accept sensor Merkle roots only from registered devices (ecrecover). Test with vm.sign, then with a real ESP32 signature
- [ ] Write (30 min): Log: what this proves (the device signed it) and what it doesn't (the reading is true)
- [ ] Explain (45 min): Explainer #5: write "Teaching a sensor to sign its own data" in blog/ (600–900 words, weeks 9–10). Optional: record a 5-minute video teaching it and link it in the post
- [ ] Capstone (30 min): Replace the provenance mock in the integration test: create a batch, record its events and a signed sensor root, list it, pay, release. Update demo.sh
- [ ] Capstone (30 min): Firmware checks: run make vectors, make your ESP32 reproduce test_vectors.json byte for byte, and add firmware/tools/Vectors.t.sol.example to test/ so CI proves tampered and unregistered readings are rejected. Demo stage 5 uses sample_readings.json, so it runs without hardware

## Week 11: Capstone II: connect all four parts and ship

**Dates:** 7 Dec – 13 Dec 2026 · **Planned time:** 10 h

**Goal:** Deploy the whole trust stack to an L2 testnet, prove it works end to end with one test, and publish it.

**Ship:** All four parts on an L2 testnet, one end-to-end test passing, and a README with an architecture diagram, demo video and post

### Plan
- [ ] Build (90 min): Deploy all four parts to an L2 testnet such as Base Sepolia: TestUSD, Marketplace, CredentialRegistry and ProvenanceAnchor. Verify each contract on the explorer  
  [Base docs (Base Sepolia testnet)](https://docs.base.org/)
- [ ] Build (150 min): End-to-end flow in the integration test and demo.sh: a credentialed farmer creates a batch, a transporter records pickup and delivery with the ESP32's signed readings, the batch is checked against its policy, and the buyer's TestUSD in escrow is released only if the batch is compliant; otherwise the buyer is refunded
- [ ] Build (15 min): Capstone C demo: a script that sends a TestUSD payment with a receipt event and prints its cost and time next to the bank and mobile-money figures from week 9
- [ ] Build (45 min): Security pass on all four contracts: Slither, your Project 4 checklist, and invariant tests  
  [Slither](https://github.com/crytic/slither)
- [ ] Write (45 min): For each of the four parts, argue honestly whether a blockchain beats a shared database, and say so where it doesn't
- [ ] Write (90 min): README with an architecture diagram, a 5-minute demo video of the full flow, and the capstone post
- [ ] Write (30 min): Log: what you'd change with another month
- [ ] AI (15 min): GenAI provenance: read the C2PA overview, then add a paragraph to your capstone README on how the same sign-and-anchor pattern could prove where a photo or AI-generated output came from  
  [C2PA](https://c2pa.org/)
- [ ] Capstone (45 min): Compliance check: anyone can mark a batch non-compliant by submitting a signed reading outside the policy range with its Merkle proof, and a missing step or wrong role also fails. Test one compliant batch and one failing batch
- [ ] Capstone (30 min): Demo site v1, open to everyone with no login: Explore (sample batches), Market (listings) and Trace (enter a batch id or scan its QR code to see the journey, who signed each step, the readings summary and compliance status), reading from your deployed contracts. Build it in trust-stack/app/site/ following trust-stack/app/README.md
- [ ] Capstone (30 min): Deploy for real: forge script with your keystore account to Base Sepolia, verify on Basescan, record addresses and read-only checks in deployments/base-sepolia.json (copy the example), and run make smoke until every check is green  
  [Base docs](https://docs.base.org/)
- [ ] Capstone (15 min): Make it public: put the trace page in trust-stack/app/site/ so it publishes to GitHub Pages, then check the README's Trust stack badge, Codespaces button and DEMO.md all work from a logged-out browser

---

## Objectives and check-yourself

### Block 10

**By the end of this block you can:**

- Explain how hardware wallets and trusted execution protect keys, and where they fail
- Generate a key on an ESP32 (or a simulator) and sign sensor readings
- Batch readings into a Merkle tree and sign only the root
- Accept on-chain only roots signed by registered devices (ecrecover)
- Explain what anchoring proves (this device signed this data) and what it can't (that the reading is true)

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. Where does my ESP32's private key live, and how could someone holding the board extract it?
2. Why sign a Merkle root instead of every reading? What does that save on-chain?
3. Does my firmware reproduce test_vectors.json byte for byte? If not, where do the bytes differ?
4. What does ecrecover return for a tampered reading, and how does my contract reject it?
5. A sensor sitting in ice honestly signs "2 °C" while the tomatoes are warm. What does my system prove, and what does it miss?
6. How does OpenTimestamps anchor millions of hashes with one transaction?

### Block 11

**By the end of this block you can:**

- Deploy and verify all four contracts on Base Sepolia with a keystore, never a plain-text key
- Run the end-to-end flow: credential, batch, journey, listing, payment, then settlement or refund
- Enforce the product policy on-chain, with one compliant and one failing batch
- Publish a demo site and trace page that anyone can use without logging in
- Argue honestly, part by part, whether a blockchain beats a shared database

**Check yourself** (answer these in LEARNING_LOG.md on Saturday):

1. Can I run the whole demo from a fresh clone with one command, and does CI agree?
2. What happens to the buyer's TestUSD when a reading is out of range, and which test proves it?
3. Who can do what in my system, and what is the worst thing each role could do?
4. For which of the four parts would a shared database be just as good, and why?
5. Does make smoke pass against the live deployment?
6. Can someone who has never seen my repo follow a batch on the trace page?


## What I built

<!-- One paragraph, plus a screenshot or terminal output if it helps. -->

## How to run it

```bash
# commands here
```

## What I learned

- 

## What broke, and how I fixed it

- 

## Time spent

| Date | Hours | What |
|------|-------|------|
|      |       |      |
