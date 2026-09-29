# One pinned toolchain for this repo: Foundry (forge, cast, anvil), solc,
# Python tools (Slither, eth-account, python-bitcoinlib), jq, make and git.
# The same image runs locally (make docker-demo), in Codespaces, and in CI.
#
#   docker build -t blockchain-learning .
#   docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD":/repo blockchain-learning           # runs the demo
#   docker run --rm -it --user "$(id -u):$(id -g)" -v "$PWD":/repo blockchain-learning bash      # a shell with every tool
#
# Versions live in toolchain.env and requirements-dev.txt.
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates curl git jq make bash python3 python3-venv \
 && rm -rf /var/lib/apt/lists/* \
 && git config --system --add safe.directory '*'

# A home that any user id can write to, so files you create in the mounted
# repo are owned by you (docker run --user "$(id -u):$(id -g)").
RUN useradd -m -u 1000 -s /bin/bash dev 2>/dev/null || { userdel -r ubuntu && useradd -m -u 1000 -s /bin/bash dev; }
ENV HOME=/home/dev

COPY toolchain.env requirements-dev.txt /opt/toolchain/

# Foundry, from its GitHub release (amd64 or arm64).
ARG TARGETARCH
RUN . /opt/toolchain/toolchain.env \
 && arch="${TARGETARCH:-amd64}" \
 && curl -fsSL --retry 5 --retry-all-errors --retry-delay 3 "https://github.com/foundry-rs/foundry/releases/download/${FOUNDRY_VERSION}/foundry_${FOUNDRY_VERSION}_linux_${arch}.tar.gz" \
    | tar -xz -C /usr/local/bin forge cast anvil chisel \
 && forge --version

# solc, installed where Foundry looks for it, so builds work offline.
# amd64 uses the official static build from the Solidity GitHub release;
# arm64 lets Foundry fetch its own build the first time.
RUN . /opt/toolchain/toolchain.env \
 && mkdir -p "$HOME/.svm/$SOLC_VERSION" \
 && if [ "${TARGETARCH:-amd64}" = "amd64" ]; then \
      curl -fsSL --retry 5 --retry-all-errors --retry-delay 3 -o "$HOME/.svm/$SOLC_VERSION/solc-$SOLC_VERSION" \
        "https://github.com/ethereum/solidity/releases/download/v$SOLC_VERSION/solc-static-linux" \
      && chmod +x "$HOME/.svm/$SOLC_VERSION/solc-$SOLC_VERSION"; \
    fi \
 && mkdir -p /tmp/warm/src && cd /tmp/warm \
 && printf '// SPDX-License-Identifier: MIT\npragma solidity %s;\ncontract Warm {}\n' "$SOLC_VERSION" > src/Warm.sol \
 && forge build --use "$SOLC_VERSION" \
 && cd / && rm -rf /tmp/warm

# Python tools in their own environment.
RUN python3 -m venv /opt/venv \
 && /opt/venv/bin/pip install --no-cache-dir -r /opt/toolchain/requirements-dev.txt
ENV PATH=/opt/venv/bin:$PATH

RUN chmod -R a+rwX /home/dev
USER dev
WORKDIR /repo/trust-stack
CMD ["make", "demo"]
