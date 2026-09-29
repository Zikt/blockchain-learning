[↑ Overview](README.md)

# What I need

Everything except the hardware is free. Order the hardware by early November so it arrives before week 10. Prices vary by seller, so check local electronics shops or AliExpress/Amazon.

## Hardware (capstone part A, weeks 10–11)

| Item | Qty | Why |
|------|-----|-----|
| ESP32 dev board (ESP32-S3-DevKitC-1 preferred; any ESP32-DevKitC works) | 1 + 1 spare | Holds the device key and signs readings. The S3 has more memory and hardware crypto acceleration. |
| Temperature sensor: DS18B20 waterproof probe, or SHT31/SHT41 breakout | 1–2 | The reading the device signs. SHT3x/SHT4x also give humidity. |
| 4.7 kΩ resistor | 2 | Pull-up for the DS18B20. Not needed for SHT sensors. |
| Half-size breadboard and jumper wires (male-male, male-female) | 1 set | Wiring without soldering. |
| USB data cable matching the board (USB-C or micro-USB) | 1 | Flashing and serial output. Charge-only cables won't work. |
| *Optional:* 0.96" SSD1306 OLED | 1 | Shows the reading and signature status in demos. |
| *Optional:* ATECC608A secure-element breakout | 1 | Keeps the private key in dedicated hardware. |
| *Optional:* microSD module and a USB power bank | 1 each | Offline buffering, and running the device away from the laptop. |

## Accounts and software

| What | Needed from | Notes |
|------|-------------|-------|
| GitHub account | Week 1 | Repo, Actions, and later Pages. |
| Python 3.11+, Git, VS Code | Week 1 | Add `pip install ecdsa python-bitcoinlib slither-analyzer` as each week needs them. |
| Bitcoin Core | Week 2 | Regtest only. No full-chain download. |
| Cyfrin Updraft; Coursera (optional) | Week 4 (Coursera week 1) | Free. Coursera courses can be audited free. |
| Browser wallet (MetaMask or Rabby) in a separate browser profile | Week 4 | Testnet only. Never reuse a wallet that holds real funds. |
| Sepolia test ETH | Week 4 | The Google Cloud faucet needs a Google account. Some faucets ask for a small mainnet balance; try another if refused. |
| Node.js 20+ and Foundry | Week 5 | Foundry installs with one command. |
| RPC provider (Alchemy or Infura, free tier) and an Etherscan API key | Week 5 | Scripted deploys and contract verification. |
| LLM API key (e.g. Anthropic or OpenAI) | Week 12 | A few dollars of credit for the agent wallet. Chat apps are fine for the earlier AI tasks. |
| YouTube or Loom; OBS Studio | Week 2 | Optional explainer videos. |
| ESP-IDF or PlatformIO | Before week 10 | Flash a "hello world" early. |
| Base Sepolia test ETH | Week 11 | Bridge from Sepolia or use a Base Sepolia faucet. |

**Computer:** 8 GB RAM (16 GB is more comfortable), about 20 GB free disk; macOS, Linux, or Windows with WSL2.
