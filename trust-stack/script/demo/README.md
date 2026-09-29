[↑ Trust stack](../../README.md)

# Demo stages

`scripts/demo.sh` runs these Foundry scripts in order on a local chain. Add one as each part gets built; the demo runs as far as the stages you have.

| File | Week | What it should do |
|------|------|-------------------|
| `01_TestUSD.s.sol` | 5 | Deploy TestUSD, mint 1,000 to the buyer |
| `02_Credentials.s.sol` | 6 (mock), 9 (real) | Deploy the registry, issue farmer, transporter, inspector and buyer roles |
| `03_List.s.sol` | 6 | Deploy the provenance mock (real one from week 10) and Marketplace; farmer creates batch 1 under the tomato policy and lists it |
| `04_Pay.s.sol` | 7 | Buyer approves and pays into escrow |
| `05_Journey.s.sol` | 10 | Record packed → inspected → shipped → received, with the sensor root from `firmware/sample_readings.json` |
| `06_Settle.s.sol` | 11 | Check compliance, release payment, print the seller's reputation |
| `07_Violation.s.sol` | 11 | Batch 2 with an 11 °C reading: submit the violation proof, buyer is refunded |
| `08_Trace.s.sol` | 11 | Print each batch's journey, who signed each step, and its status |

## Rules every stage follows

- **Keep addresses in the deployments file.** Read its path from the `DEPLOYMENTS` environment variable (demo.sh sets it: `deployments/local.json` locally, `deployments/base-sepolia.json` when seeding the live demo). Store contracts under `.contracts.<Name>`.
- **Reuse before deploying.** If the contract is already in the file, use it; only deploy when it's missing. That's what lets the same stages seed the live testnet demo again and again without redeploying.
- **Use the cast of characters:** 0 deployer and credential issuer, 1 farmer, 2 transporter, 3 inspector, 4 buyer. Locally these are Anvil's public test keys (the defaults below). For the live demo, set `FARMER_KEY`, `TRANSPORTER_KEY`, `INSPECTOR_KEY` and `BUYER_KEY` in `trust-stack/.env` to throwaway testnet keys with a little test ETH. `.env` is never committed.
- **Print what happened in plain words** with `console.log`, e.g. `Batch 1 listed at 120 TestUSD by 0x7099…`. That output is what people see.
- **Fail loudly.** If something isn't as expected, `require` it, so the demo shows ❌ instead of pretending.
- **Label sample data.** On the live demo, give sample batches names like "Sample batch: tomatoes, Musanze → Kigali" so visitors know it's dummy data.

## Template

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Script, console} from "forge-std/Script.sol";
import {TestUSD} from "../../src/TestUSD.sol";

contract Stage01 is Script {
    // Anvil's public test key for account 4, used only when BUYER_KEY isn't set.
    uint256 constant ANVIL_BUYER = 0x47e179ec197488593b187f80a00eb0da91f1b9d0b13f8733639f19c30a34926a;

    function run() external {
        string memory file = vm.envOr("DEPLOYMENTS", string("deployments/local.json"));
        string memory json = vm.readFile(file);
        address buyer = vm.addr(vm.envOr("BUYER_KEY", ANVIL_BUYER));

        vm.startBroadcast();
        TestUSD usd;
        if (vm.keyExistsJson(json, ".contracts.TestUSD")) {
            usd = TestUSD(vm.parseJsonAddress(json, ".contracts.TestUSD"));
            console.log("Using TestUSD at", address(usd));
        } else {
            usd = new TestUSD();
            console.log("TestUSD deployed at", address(usd));
        }
        usd.mint(buyer, 1_000e6);
        vm.stopBroadcast();

        vm.writeJson(vm.toString(address(usd)), file, ".contracts.TestUSD");
        console.log("Buyer funded with 1000 TestUSD");
    }
}
```
