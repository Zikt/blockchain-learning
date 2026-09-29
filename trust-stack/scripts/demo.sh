#!/usr/bin/env bash
# Trust-stack demo runner.
#
# Runs the story stage by stage on a local chain, using whatever you have
# built so far. Each stage is one Foundry script in script/demo/. Stages that
# don't exist yet are listed as "not built yet", and the demo stops there.
#
#   ./scripts/demo.sh              run every stage that exists
#   ./scripts/demo.sh --upto 4     stop after stage 4
#   ./scripts/demo.sh --keep       leave the local chain running afterwards
#   ./scripts/demo.sh --rpc URL    use a chain that's already running
#   ./scripts/demo.sh --network base-sepolia --account deployer
#                                  seed the live testnet demo with sample data:
#                                  reuses the contracts in deployments/base-sepolia.json,
#                                  signs with your Foundry keystore account
#                                  (it asks for the keystore password once per stage;
#                                  FORGE_EXTRA_ARGS="--password ..." skips the prompt)
set -uo pipefail
cd "$(dirname "$0")/.."

STAGES=(
  "01|TestUSD: deploy the test stablecoin and fund the demo buyer|5|01_TestUSD.s.sol"
  "02|Credentials: issue farmer, transporter, inspector and buyer roles|6 (mock), 9 (real)|02_Credentials.s.sol"
  "03|Marketplace: the credentialed farmer creates and lists a batch|6|03_List.s.sol"
  "04|Payment: the buyer pays in TestUSD into escrow|7|04_Pay.s.sol"
  "05|Journey: packed, inspected, shipped, received, with signed sensor readings|10|05_Journey.s.sol"
  "06|Settlement: the compliant batch releases payment and reputation goes up|11|06_Settle.s.sol"
  "07|Violation: a second batch with a proven 11 °C reading refunds its buyer|11|07_Violation.s.sol"
  "08|Trace: print each batch's journey, signers and status|11|08_Trace.s.sol"
)

UPTO=99; KEEP=0; RPC=""; NETWORK=""; ACCOUNT=""
while [ $# -gt 0 ]; do
  case "$1" in
    --upto) UPTO="$2"; shift 2 ;;
    --keep) KEEP=1; shift ;;
    --rpc)  RPC="$2"; shift 2 ;;
    --network) NETWORK="$2"; shift 2 ;;
    --account) ACCOUNT="$2"; shift 2 ;;
    -h|--help) awk 'NR>1 && /^#/{sub(/^# ?/,"");print;next} NR>1{exit}' scripts/demo.sh; exit 0 ;;
    *) echo "Unknown option: $1"; exit 2 ;;
  esac
done

bold() { printf '\033[1m%s\033[0m\n' "$*"; }
summary=()   # rows for the final table

if ! command -v forge >/dev/null || ! command -v anvil >/dev/null; then
  echo "Foundry isn't installed. Install it with:"
  echo "  curl -L https://getfoundry.sh/install | bash && foundryup"
  echo "or open this repo in GitHub Codespaces, where it's preinstalled."
  exit 1
fi
if ! ls src/*.sol >/dev/null 2>&1; then
  echo "No contracts in trust-stack/src yet: the trust stack starts in week 5."
  exit 0
fi
if [ ! -d lib/forge-std/src ]; then
  echo "forge-std is missing. From the repo root, run:"
  echo "  git submodule update --init --recursive"
  echo "(or, the first time: git submodule add https://github.com/foundry-rs/forge-std trust-stack/lib/forge-std)"
  exit 1
fi

bold "Building…"
forge build --quiet || { echo "Build failed. Fix the compile errors above."; exit 1; }

mkdir -p deployments
if [ -n "$NETWORK" ]; then
  export DEPLOYMENTS="deployments/$NETWORK.json"
  [ -f "$DEPLOYMENTS" ] || { echo "No $DEPLOYMENTS yet. Copy deployments/$NETWORK.example.json and fill it in after deploying."; exit 1; }
  [ -n "$RPC" ] || RPC=$(sed -n 's/.*"rpc": *"\([^"]*\)".*/\1/p' "$DEPLOYMENTS" | head -1)
  [ -n "$ACCOUNT" ] || { echo "On a real network, sign with your keystore: --account <name> (see: cast wallet import)."; exit 1; }
  bold "Seeding $NETWORK via $RPC, signing as keystore account '$ACCOUNT'…"
else
  export DEPLOYMENTS="deployments/local.json"
  echo '{"contracts":{}}' > "$DEPLOYMENTS"
fi

ANVIL_PID=""
if [ -z "$RPC" ]; then
  PORT="${DEMO_PORT:-8545}"
  RPC="http://127.0.0.1:${PORT}"
  bold "Starting a local chain on port ${PORT}…"
  anvil --port "$PORT" --silent >/dev/null 2>&1 &
  ANVIL_PID=$!
  for _ in $(seq 1 50); do cast chain-id --rpc-url "$RPC" >/dev/null 2>&1 && break; sleep 0.2; done
  if [ "$KEEP" = 0 ]; then trap 'kill $ANVIL_PID 2>/dev/null' EXIT; fi
fi
# Anvil's first default account. It's a public test key: never use it anywhere real.
DEMO_KEY="${DEMO_KEY:-0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80}"

status=0; stopped=0
for row in "${STAGES[@]}"; do
  IFS='|' read -r num title week file <<<"$row"
  n=$((10#$num))
  if [ "$n" -gt "$UPTO" ]; then break; fi
  if [ "$stopped" = 1 ]; then summary+=("| $num | $title | ⏸ waiting for earlier stages |"); continue; fi
  if [ ! -f "script/demo/$file" ]; then
    summary+=("| $num | $title | ⬜ not built yet (week $week) |")
    stopped=1; continue
  fi
  echo; bold "Stage $num · $title"
  if [ -n "$ACCOUNT" ]; then SIGN=(--account "$ACCOUNT"); else SIGN=(--private-key "$DEMO_KEY"); fi
  # FORGE_EXTRA_ARGS lets CI or advanced users pass extra flags (e.g. --password for a keystore)
  out=$(forge script "script/demo/$file" --rpc-url "$RPC" "${SIGN[@]}" --broadcast ${FORGE_EXTRA_ARGS:-} 2>&1)
  code=$?
  # show only the stage's own console.log output
  printf '%s\n' "$out" | sed -n '/== Logs ==/,/^$/p' | sed '1d;/^$/d;s/^ */  /'
  if [ $code -eq 0 ]; then
    summary+=("| $num | $title | ✅ passed |")
  else
    printf '%s\n' "$out" | tail -25
    summary+=("| $num | $title | ❌ failed |")
    status=1; stopped=1
  fi
done

echo
bold "Demo summary"
table=("| Stage | What happens | Result |" "|---|---|---|" "${summary[@]}")
printf '%s\n' "${table[@]}"
if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
  { echo "## Trust-stack demo"; echo; printf '%s\n' "${table[@]}"; } >> "$GITHUB_STEP_SUMMARY"
fi
if [ "$KEEP" = 1 ] && [ -n "$ANVIL_PID" ]; then
  echo; echo "Local chain still running at $RPC (pid $ANVIL_PID). Contract addresses: deployments/local.json"
fi
exit $status
