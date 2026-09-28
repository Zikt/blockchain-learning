# Weeks 10–11: Capstone, tamper-evident cold-chain provenance

## Week 10: Capstone I: the device signs, the contract verifies

**Dates:** 30 Nov – 6 Dec 2026 · **Planned time:** 10 h

**Goal:** Make an ESP32 hold its own key and sign batched readings, and write the contract that accepts only signatures from registered devices.

**Ship:** ESP32 firmware that signs Merkle roots of readings, and a tested SensorRegistry contract

### Plan

- [ ] Learn (30 min): Browse the Trezor firmware repo: the crypto folder and the security docs  
  [trezor-firmware](https://github.com/trezor/trezor-firmware)
- [ ] Learn (30 min): SGX.Fail: skim the list of TEE attacks  
  [sgx.fail](https://sgx.fail/)
- [ ] Learn (30 min): OpenZeppelin ECDSA and MessageHashUtils docs  
  [OZ ECDSA](https://docs.openzeppelin.com/contracts/5.x/api/utils#ECDSA)
- [ ] Learn (30 min): Study how OpenTimestamps anchors many hashes with one transaction  
  [opentimestamps.org](https://opentimestamps.org/)
- [ ] Build (150 min): On an ESP32, generate a key with micro-ecc or trezor-crypto, hash a sensor reading with keccak256, and print r, s, v and the address  
  [micro-ecc](https://github.com/kmackay/micro-ecc) · [ESP-IDF](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/)
- [ ] Build (120 min): Batch readings on the device or a gateway: build a Merkle tree and sign the root instead of each reading  
  [OZ MerkleProof](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleProof)
- [ ] Build (180 min): Write SensorRegistry: register device addresses, accept a signed Merkle root only if ecrecover matches. Test with vm.sign, then with a real ESP32 signature
- [ ] Write (30 min): Log: what this proves (the device signed it) and what it doesn't (the reading is true)

## Week 11: Capstone II: anchor, verify, ship

**Dates:** 7 Dec – 13 Dec 2026 · **Planned time:** 10 h

**Goal:** Deploy to an L2 testnet, let anyone check a single reading, and publish the project. This week is the mid-December deadline.

**Ship:** The finished capstone: public repo, deployed contract, verification dashboard, README, demo video and write-up

### Plan

- [ ] Build (120 min): Contract: anchor signed roots from registered devices on an L2 testnet, with tests  
  [OZ MerkleProof](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleProof) · [Base docs](https://docs.base.org/)
- [ ] Build (150 min): Dashboard: paste any reading, show its Merkle proof and the anchoring transaction
- [ ] Build (60 min): Optional if time is short: a small anomaly detector that flags temperature excursions before signing
- [ ] Build (60 min): Security pass: Slither, your Project 4 checklist, and invariant tests  
  [Slither](https://github.com/crytic/slither)
- [ ] Write (60 min): Argue blockchain vs. shared database for this use case, and be willing to conclude it isn't needed
- [ ] Write (120 min): README, a 3-minute demo video, and a short post on what you built
- [ ] Write (30 min): Log: what you'd change with another month

---

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
