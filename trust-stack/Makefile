.PHONY: build test coverage slither demo demo-keep smoke seed fmt vectors \
        docker-build docker-demo docker-test docker-slither docker-shell docker-site

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

# ---- Docker: the same pinned tools on any machine (see ../DOCKER.md) --------
# Your repo is mounted into the container, so edits on your computer are seen
# straight away and files the container writes stay yours.
IMAGE ?= blockchain-learning
DOCKER_BUILD_FLAGS ?=
TTY := $(shell [ -t 0 ] && echo -it)
DOCKER_RUN = docker run --rm $(TTY) --user "$$(id -u):$$(id -g)" -v "$(abspath ..)":/repo -w /repo/trust-stack $(IMAGE)

docker-build:   ; docker build $(DOCKER_BUILD_FLAGS) -t $(IMAGE) ..
docker-demo:    docker-build ; $(DOCKER_RUN) make demo
docker-test:    docker-build ; $(DOCKER_RUN) make test
docker-slither: docker-build ; $(DOCKER_RUN) make slither
docker-shell:   docker-build ; $(DOCKER_RUN) bash
# Preview the demo site (app/site) at http://localhost:8000 (week 11 on)
docker-site:    docker-build ; docker run --rm $(TTY) --user "$$(id -u):$$(id -g)" -p 8000:8000 -v "$(abspath ..)":/repo -w /repo/trust-stack $(IMAGE) python3 -m http.server 8000 --bind 0.0.0.0 -d app/site
