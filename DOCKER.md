[↑ Overview](README.md) · [Run the demo](DEMO.md) · [Tests](TESTING.md)

# Docker: one pinned toolchain

Everything this repo needs (Foundry, the Solidity compiler, Slither, the Python crypto libraries, jq, make) is in one Docker image with fixed versions. The same image runs on your laptop, in GitHub Codespaces and in CI, so a test that passes in one place passes in the others.

Your code is **not** copied into the image. The repo folder is mounted into the container when it runs, so you edit files on your computer as usual, and anything the container writes (build output, `deployments/local.json`) appears in your folder, owned by you.

## Where the versions live

| File | Pins |
|------|------|
| `toolchain.env` | Foundry (`FOUNDRY_VERSION`) and the Solidity compiler (`SOLC_VERSION`) |
| `requirements-dev.txt` | Python tools: Slither, eth-account, ecdsa, python-bitcoinlib |
| `trust-stack/foundry.toml` | `solc_version`, which must match `toolchain.env` (CI checks this) |
| `Dockerfile` | Ubuntu 24.04 plus the above |

To upgrade a tool, change the version there, run `make docker-build`, and check that `make docker-test` and `make docker-demo` still pass before pushing.

## Set up (once)

1. Install [Docker Desktop](https://docs.docker.com/get-started/get-docker/) (Mac, Windows) or Docker Engine (Linux), and start it.
2. Clone with the submodules:
   ```bash
   git clone --recursive https://github.com/YOUR-GITHUB-USERNAME/blockchain-learning.git
   cd blockchain-learning
   ```
   If you already cloned without `--recursive`, run `git submodule update --init --recursive`.
3. Build the image (a few minutes the first time, then seconds):
   ```bash
   docker build -t blockchain-learning .
   ```

## Run

From `trust-stack/` (macOS, Linux, or Windows with WSL):

| Command | Does |
|---------|------|
| `make docker-demo` | Runs the demo on a fresh local chain |
| `make docker-test` | Unit, fuzz and invariant tests |
| `make docker-slither` | Static analysis |
| `make docker-shell` | Opens a terminal with every tool (forge, cast, anvil, python3, slither, jq) |
| `make docker-site` | Previews the demo site at http://localhost:8000 (week 11 on) |

Each command rebuilds the image first. That takes a second when nothing has changed.

Without `make`, for example in Windows PowerShell, run from the repo root:
```bash
docker run --rm -it -v "${PWD}:/repo" blockchain-learning                  # the demo
docker run --rm -it -v "${PWD}:/repo" blockchain-learning make test        # tests
docker run --rm -it -v "${PWD}:/repo" blockchain-learning bash             # a shell
```
On Linux, add `--user "$(id -u):$(id -g)"` so the files it creates belong to you. The `make` targets already do this.

## Learning with it, week by week

| Weeks | In the container (`make docker-shell`) | On your computer |
|-------|----------------------------------------|------------------|
| 1, 3 | Python scripts: `cd /repo/week01-toy-chain && python3 toy_chain.py` | Editing, git |
| 2 | `python-bitcoinlib` scripts | Bitcoin Core (`bitcoind -regtest`), which isn't in the image |
| 4 | — | Remix and your browser wallet |
| 5 onward | `forge`, `cast`, `anvil`, `make test`, `make demo`, `slither` | Editing, git |
| 7, 11 | `make docker-site` to preview | The browser wallet, and Node for the frontend |
| 10 | `make vectors` and the firmware tests | Flashing the ESP32 over USB (Arduino IDE or PlatformIO) |
| 11, 12 | `make smoke` | `make seed` and anything that uses your keystore |

The last row matters. **Keys stay on your computer.** The container has no access to your Foundry keystore, so deploying (`forge script … --account deployer`) and `make seed` run outside Docker, or in Codespaces with the key imported there. Never bake a key into the image or pass one on the command line.

Git also stays on your computer: commit and push from your usual terminal.

## Three ways to get the same tools

| | Best for | Setup |
|---|---|---|
| **Codespaces** (README badge) | Visitors, or working from any machine | None. It builds this same image |
| **Docker** (this page) | Reproducible local runs, and reviewers who don't want to install Foundry | Docker Desktop |
| **Native install** | Your fastest day-to-day loop | `foundryup --install v1.5.1`, `pip install -r requirements-dev.txt` |

Native is fine for everyday work. CI runs the pinned versions on every push, so if your local tools drift, CI will catch it.

## Troubleshooting

- **"forge-std is missing"**: run `git submodule update --init --recursive` on your computer, not in the container.
- **Permission denied writing `out/` or `cache/` on Linux**: use the `make docker-*` targets, or add `--user "$(id -u):$(id -g)"`. Delete root-owned folders left by an earlier run with `sudo rm -rf out cache`.
- **Apple Silicon**: the image builds natively for arm64. Foundry fetches the arm64 compiler while the image builds, so it still works offline afterwards.
- **Behind a proxy**: `make docker-build DOCKER_BUILD_FLAGS="--build-arg https_proxy=$HTTPS_PROXY"`.
