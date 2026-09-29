[↑ Overview](../../README.md) · [Trust stack](../README.md) · [Run the demo](../../DEMO.md)

# Live demo site

A small website that stays online after the plan ends. Anyone can browse it without logging in, and it comes preloaded with sample data. When you connect your admin wallet, an Admin tab lets you add new data live, for example during a talk or a meeting.

- **Where it runs:** GitHub Pages. It's free, and `.github/workflows/pages.yml` publishes `trust-stack/app/site/` on every push that changes it.
- **Where the data lives:** the contracts on Base Sepolia (testnet). The site has no server or database. It reads the chain directly, so what visitors see is exactly what the contracts hold.
- **When it's built:** the read-only pages in week 11, and seeding plus the admin console in week 12.

## What visitors see (no login)

| Page | Shows | Reads from |
|------|-------|-----------|
| **Explore** | The sample batches: product, farmer, current step, compliance status | `ProvenanceAnchor` events |
| **Market** | Listings with price in TestUSD, seller reputation, sold or open | `Marketplace` |
| **Trace** `?batch=1` | The journey step by step, who signed each step (and their role), the readings summary, compliant or not, and why | `ProvenanceAnchor`, `CredentialRegistry` |
| **Verify** | Paste a reading and its proof, and see whether it's part of the anchored root | `ProvenanceAnchor` |

A banner on every page says: *"Testnet demo. Sample data, no real money or produce."* Each trace page has a QR code that links to itself, so a printed label on a crate opens the batch.

"Logging in" here means **connecting a wallet**. Visitors never need to. Someone who wants to try an action (for example buying a listing with TestUSD) can connect a testnet wallet. They'll need a little Base Sepolia ETH, and you can mint them TestUSD from the admin tab.

## What you see as admin

The **Admin** tab appears only when the connected wallet holds the issuer (cooperative) role in `CredentialRegistry`. From it you can:

- issue or revoke a role credential (farmer, transporter, inspector, buyer)
- create a batch under a policy and list it
- record a step for a batch (as the actor wallet that holds that role)
- anchor a set of readings (upload a `readings.json` from the ESP32 or the gateway)
- mint TestUSD to a visitor's address

Each action is a normal transaction, and the page updates once it confirms, so a new batch appears on Explore straight away.

**Security:** hiding the tab only tidies the page. The real protection is in the contracts: every admin function checks the caller's role on-chain, and your tests (`test_RevertWhen_...`) prove a stranger gets rejected. Use a separate admin wallet that only ever holds testnet funds.

## Sample data (seeding)

`make seed` runs the same demo stages as `make demo`, but against Base Sepolia instead of a local chain. It reuses the contracts listed in `deployments/base-sepolia.json` and adds new sample batches each time, so you can run it again whenever the demo needs topping up.

One-time setup:

```bash
cd trust-stack
cast wallet import deployer --interactive     # your admin/deployer key, stored encrypted; never in .env
cp deployments/base-sepolia.example.json deployments/base-sepolia.json   # fill in addresses after deploying
cp .env.example .env    # or create it: FARMER_KEY, TRANSPORTER_KEY, INSPECTOR_KEY, BUYER_KEY
```

The four actor keys in `.env` are **throwaway testnet keys** made for the demo (`cast wallet new`), each funded with a little Base Sepolia ETH. `.env` is git-ignored. Then:

```bash
make seed     # asks for the keystore password, then runs stages 01–08 on Base Sepolia
make smoke    # read-only checks that the deployed contracts look right
```

The seeded data is labelled in the contracts' events (product names start with `SAMPLE:`), so it's never mistaken for real produce.

## Files

```
app/
├── README.md          this file
└── site/              published to GitHub Pages as-is
    ├── index.html     Explore · Market · Trace · Verify · Admin (tabs)
    ├── app.js         reads the chain with viem; wallet connect for actions
    ├── abi/           ABIs copied from out/ after forge build
    └── config.json    { "chainId": 84532, "rpc": "https://sepolia.base.org", "contracts": { ... } }
```

Keep it a static site (plain HTML and JavaScript, or a framework's static export) so Pages can host it. `config.json` holds the same addresses as `deployments/base-sepolia.json`. Copy them over after each deploy.

## Keeping it running

- **Hosting:** GitHub Pages has no server to keep alive.
- **Chain:** Base Sepolia is a public testnet, so the site keeps working. If a testnet is ever retired, redeploy to its replacement and update `config.json`.
- **RPC:** the public endpoint is rate-limited. If the site gets busy, put a free Alchemy or Infura key in `config.json`. Use a key restricted to your Pages domain, because the site is public.
- **Admin gas:** keep a small amount of Base Sepolia ETH in the admin and actor wallets. Faucets are listed in `BOM.md`.
