[↑ Overview](README.md)

# Testing

How I check that the trust stack does what it claims, and keeps doing it. Every rule in `trust-stack/POLICY.md` and every security property below has a named test. CI runs all of it on each push.

## Commands

```bash
cd trust-stack
make test        # unit, fuzz, invariant and attack tests
make coverage    # line and branch coverage (target: 90%+ on src/)
make slither     # static analysis, fails on high-severity findings
make demo        # the whole story on a fresh local chain
make smoke       # read-only checks against the live Base Sepolia deployment
make vectors     # firmware signing test vectors + sample readings
```

## Layers

| Layer | What it catches | Where |
|-------|-----------------|-------|
| Unit tests | Each function, including every revert path, access check and event | `test/*.t.sol` |
| Fuzz tests | Edge cases in amounts, ids and timestamps | `testFuzz_*` functions |
| Invariant tests | Properties that must hold after any sequence of actions | `test/invariant/` |
| Attack tests | Deliberate misuse: replay, wrong role, forged readings, re-entrancy | `test/Attacks.t.sol` |
| Integration test | The whole story across all four contracts | `test/Integration.t.sol` |
| Demo | The same story, readable, on a live local chain | `scripts/demo.sh`, `script/demo/` |
| Firmware vectors | The ESP32 signs exactly like the verifier expects; tampering is rejected | `firmware/test_vectors.json` |
| Static analysis | Known bug patterns | Slither in CI |
| Live smoke test | The deployed contracts answer as expected | `scripts/smoke.sh`, `deployments/base-sepolia.json` |

## Rules and properties → tests

Fill in the test name as you write each one, and tick it when it passes in CI.

| # | Rule or property | Source | Test | ✓ |
|---|------------------|--------|------|---|
| R1 | Only a credentialed farmer or cooperative can create a batch | POLICY | `test_RevertWhen_UncredentialedCreatesBatch` | ☐ |
| R2 | Steps happen in order: harvested → packed → inspected → shipped → received | POLICY | `test_RevertWhen_StepOutOfOrder` | ☐ |
| R3 | Each step is signed by the role allowed for it | POLICY | `test_RevertWhen_TransporterSignsInspection` | ☐ |
| R4 | Sensor roots are accepted only from registered devices | POLICY | `test_RevertWhen_UnregisteredDeviceRoot` | ☐ |
| R5 | A signed reading outside 2–8 °C, with a valid proof, fails the batch | POLICY | `test_ViolationProofFailsBatch` | ☐ |
| R6 | Transit longer than 48 h fails the batch | POLICY | `test_TransitTooLongFailsBatch` | ☐ |
| R7 | Only credentialed sellers can list | SPEC | `test_RevertWhen_UncredentialedSellerLists` | ☐ |
| R8 | A compliant batch releases payment and increments reputation | SPEC | `test_CompliantBatchReleases` | ☐ |
| R9 | A non-compliant batch refunds the buyer | SPEC | `test_NonCompliantBatchRefunds` | ☐ |
| R10 | A revoked credential can no longer sign steps or list | SPEC | `test_RevertWhen_RevokedCredential` | ☐ |
| I1 | Escrow always holds at least what it owes | Invariant | `invariant_EscrowSolvent` | ☐ |
| I2 | TestUSD total supply equals the sum of balances | Invariant | `invariant_SupplyEqualsBalances` | ☐ |
| I3 | A batch's stage never goes backwards | Invariant | `invariant_StagesMonotonic` | ☐ |
| I4 | A non-compliant batch can never release payment | Invariant | `invariant_NoReleaseWhenNonCompliant` | ☐ |
| A1 | A signed credential or order can't be replayed (nonce, chain id, deadline) | Attack | `test_RevertWhen_SignatureReplayed` | ☐ |
| A2 | A batch id can't be reused or hijacked | Attack | `test_RevertWhen_BatchIdReused` | ☐ |
| A3 | Release can't be re-entered | Attack | `test_ReentrancyOnRelease` | ☐ |
| A4 | Only the buyer or the arbiter can release; nobody else | Attack | `test_RevertWhen_StrangerReleases` | ☐ |
| A5 | A reading changed after signing is rejected | Firmware | `test_RevertWhen_TamperedReading` (uses `test_vectors.json`) | ☐ |

## Limits

These tests show the contracts enforce the rules they're given. They can't show that a sensor was placed in the right crate, or that a person told the truth. A mainnet version holding real money would also need an external audit, reviewed key management and legal checks.
