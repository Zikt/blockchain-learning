[↑ Overview](README.md)

# Run the demo

The trust stack tells one story: a batch of tomatoes goes from a credentialed farmer to a buyer, every handoff is signed, a sensor records the temperature, and the payment is released only if the batch stayed within its rules. The demo runs as far as the parts built so far.

## 1. Watch it (no install)

- **Latest demo run:** open the [Trust stack workflow](https://github.com/zikt/blockchain-learning/actions/workflows/trust-stack.yml), pick the newest run, and read the stage table on its summary page.
- **Live demo site** (from week 11): https://zikt.github.io/blockchain-learning/. Browse sample batches, market listings and each batch's trace page on Base Sepolia. No login or wallet needed. ([How it works](trust-stack/app/README.md))

## 2. Run it in your browser (no install)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/zikt/blockchain-learning)

Wait for setup to finish (a few minutes the first time), then in the terminal:

```bash
cd trust-stack
make demo
```

## 3. Run it on your own computer

```bash
curl -L https://getfoundry.sh/install | bash && foundryup   # installs forge, cast, anvil
git clone --recursive https://github.com/zikt/blockchain-learning.git
cd blockchain-learning/trust-stack
make demo
```

## What you'll see

Each stage prints what happened in plain words, then a summary:

| Stage | What happens |
|-------|--------------|
| 01 | TestUSD is deployed and the buyer is funded |
| 02 | The farmer, transporter, inspector and buyer get role credentials |
| 03 | The farmer creates batch 1 under the tomato policy and lists it |
| 04 | The buyer pays in TestUSD into escrow |
| 05 | Packed, inspected, shipped and received are recorded, with signed sensor readings |
| 06 | The batch is compliant: payment is released and the farmer's reputation goes up |
| 07 | Batch 2 has an 11 °C reading: the proof is submitted and its buyer is refunded |
| 08 | Each batch's journey, signers and status are printed |

Stages not built yet show as "not built yet" with the week they arrive. No real money is involved: the demo uses a local chain and public test accounts.

## Other checks

```bash
make test       # every test, including fuzz, invariant and attack tests
make smoke      # read-only checks against the deployed contracts on Base Sepolia
```
