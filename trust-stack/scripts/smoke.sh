#!/usr/bin/env bash
# Checks a live deployment (default: Base Sepolia) against deployments/<network>.json.
#   ./scripts/smoke.sh                 uses deployments/base-sepolia.json
#   ./scripts/smoke.sh sepolia         uses deployments/sepolia.json
# The file lists contract addresses and read-only checks: {contract, sig, args, expect}.
set -uo pipefail
cd "$(dirname "$0")/.."
NET="${1:-base-sepolia}"; FILE="deployments/$NET.json"
[ -f "$FILE" ] || { echo "No $FILE yet. Deploy first (week 11), then record the addresses there."; exit 1; }
command -v jq >/dev/null || { echo "Needs jq (apt install jq / brew install jq)."; exit 1; }
RPC="${RPC_URL:-$(jq -r '.rpc' "$FILE")}"
echo "Checking $NET via $RPC"
fail=0; n=$(jq '.checks | length' "$FILE")
for i in $(seq 0 $((n - 1))); do
  c=$(jq -r ".checks[$i].contract" "$FILE"); sig=$(jq -r ".checks[$i].sig" "$FILE")
  expect=$(jq -r ".checks[$i].expect" "$FILE"); addr=$(jq -r ".contracts[\"$c\"]" "$FILE")
  mapfile -t args < <(jq -r ".checks[$i].args[]?" "$FILE")
  got=$(cast call "$addr" "$sig" "${args[@]}" --rpc-url "$RPC" 2>&1 | awk '{print $1}')
  if [ "$got" = "$expect" ]; then echo "  ✅ $c.$sig = $got"; else echo "  ❌ $c.$sig: expected $expect, got $got"; fail=1; fi
done
exit $fail
