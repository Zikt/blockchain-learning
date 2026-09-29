<!-- NAV:START -->
[↑ Overview](../README.md) · [← Week 04](../week04-first-contracts/) · [Week 06 →](../week06-escrow-nft/)
<!-- NAV:END -->

# Week 05: Foundry and your ERC-20

**Dates:** 26 Oct – 1 Nov 2026 · **Planned time:** 10 h

**Goal:** Move to a real toolchain, write a token from the spec, fuzz it, deploy it and verify it.

**Ship:** Project 3a: an ERC-20 with unit and fuzz tests, verified on Sepolia Etherscan

### Plan
- [ ] Learn (45 min): Foundry: getting started, then forge test basics. Install the pinned version the repo uses: foundryup --install v1.5.1 (see toolchain.env)  
  [Foundry getting started](https://www.getfoundry.sh/introduction/getting-started)
- [ ] Learn (60 min): Updraft Foundry Fundamentals: the first section  
  [Foundry Fundamentals](https://updraft.cyfrin.io/courses/foundry)
- [ ] Build (120 min): Write an ERC-20 by reading the spec only. Test transfer, approve, transferFrom and the failure cases  
  [EIP-20](https://eips.ethereum.org/EIPS/eip-20)
- [ ] Write (30 min): Log: what the allowance pattern protects, and its known approval race
- [ ] Learn (20 min): Compare your token with OpenZeppelin's ERC20 source  
  [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) · [OpenZeppelin Wizard](https://wizard.openzeppelin.com/)
- [ ] Learn (20 min): Foundry docs: fuzz testing and forge scripts  
  [Foundry guides](https://www.getfoundry.sh/guides)
- [ ] Build (150 min): Add fuzz tests, deploy with forge script to Sepolia, verify the contract on Etherscan  
  [Sepolia Etherscan](https://sepolia.etherscan.io/)
- [ ] Learn (15 min): Updraft Foundry Fundamentals: continue  
  [Foundry Fundamentals](https://updraft.cyfrin.io/courses/foundry)
- [ ] Write (30 min): Log: one bug the fuzzer found, or why it found none
- [ ] AI (30 min): Have an LLM write fuzz tests for your ERC-20, then check which ones actually test something. Keep the good ones and note the useless ones in your log
- [ ] Capstone (30 min): Capstone C: turn your ERC-20 into TestUSD, the stablecoin for the payment rail. Use 6 decimals, add a capped faucet mint for testers, write tests, and keep it in trust-stack/ (the shared capstone project)
- [ ] Capstone (20 min): Demo stage 1: add forge-std as a submodule (see trust-stack/README.md), write script/demo/01_TestUSD.s.sol from the template in script/demo/README.md, run make demo, push, and check the Trust stack run on GitHub shows stage 01 passed  
  [Foundry: scripting](https://www.getfoundry.sh/guides)
- [ ] Capstone (15 min): Testing setup: run python scripts/set_github_user.py <your-username>, open TESTING.md, and start the rules-to-tests table with TestUSD's tests. Check coverage and Slither pass in CI  
  [Slither](https://github.com/crytic/slither)
- [ ] Capstone (15 min): Docker check (optional, see DOCKER.md): install Docker Desktop, then from trust-stack/ run make docker-test and make docker-demo. They should match your normal run, and the docker job in the Trust stack run on GitHub should be green  
  [Docker: get started](https://docs.docker.com/get-started/get-docker/)

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
