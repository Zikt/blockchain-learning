.PHONY: build test coverage slither demo demo-keep smoke seed fmt vectors

build:      ; forge build
test:       ; forge test -vv
coverage:   ; forge coverage --report summary
slither:    ; slither . --filter-paths "lib|test|script" --fail-high
demo:       ; ./scripts/demo.sh
demo-keep:  ; ./scripts/demo.sh --keep
smoke:      ; ./scripts/smoke.sh base-sepolia
# Seed or top up the live demo on Base Sepolia (week 12). Needs deployments/base-sepolia.json
# and a keystore account: cast wallet import deployer --interactive
seed:       ; ./scripts/demo.sh --network base-sepolia --account deployer
fmt:        ; forge fmt
vectors:    ; python3 firmware/tools/make_vectors.py
