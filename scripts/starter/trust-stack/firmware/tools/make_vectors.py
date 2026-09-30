#!/usr/bin/env python3
"""Generate signing test vectors and sample sensor data for the trust stack.

Writes two files into firmware/:
  test_vectors.json    fixed test keys, readings, digests and signatures. Your
                       ESP32 firmware must produce exactly these signatures for
                       the same key and reading (RFC 6979 makes them deterministic).
  sample_readings.json two signed batches for the demo: batch 1 stays in range
                       (compliant), batch 2 has one 11 °C reading (violation).
                       Demo stage 5 uses these, so the demo runs without hardware.

Reading format (must match your firmware and ProvenanceAnchor.sol):
  digest = keccak256(abi.encodePacked(uint256 batchId, uint32 seq,
                                      uint64 timestamp, int16 centiCelsius))
  signature = personal_sign(digest)   # OpenZeppelin MessageHashUtils.toEthSignedMessageHash
  Merkle leaf = keccak256(bytes.concat(digest)); pairs sorted before hashing (OpenZeppelin MerkleProof)

Requires: pip install eth-account
The keys below are well-known TEST keys. Never use them for anything real.
"""

import json
from pathlib import Path

from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import keccak

HERE = Path(__file__).resolve().parent.parent
DEVICE_KEY = "0x" + "11" * 32          # test-only device key
BAD_DEVICE_KEY = "0x" + "22" * 32      # an unregistered device, for negative tests


def digest(batch_id: int, seq: int, ts: int, centi_c: int) -> bytes:
    return keccak(
        batch_id.to_bytes(32, "big")
        + seq.to_bytes(4, "big")
        + ts.to_bytes(8, "big")
        + centi_c.to_bytes(2, "big", signed=True)
    )


def sign(key: str, d: bytes) -> dict:
    s = Account.sign_message(encode_defunct(primitive=d), private_key=key)
    return {"r": hex(s.r), "s": hex(s.s), "v": s.v, "signature": "0x" + bytes(s.signature).hex()}


def merkle(leaves: list[bytes]) -> tuple[bytes, list[list[str]]]:
    """Sorted-pair Merkle tree (OpenZeppelin style). Returns root and a proof per leaf."""
    layer, proofs = leaves[:], [[] for _ in leaves]
    idx = list(range(len(leaves)))
    while len(layer) > 1:
        nxt = []
        for i in range(0, len(layer), 2):
            a = layer[i]; b = layer[i + 1] if i + 1 < len(layer) else layer[i]
            nxt.append(keccak(min(a, b) + max(a, b)))
        for li, pos in enumerate(idx):
            sib = pos ^ 1
            proofs[li].append("0x" + (layer[sib] if sib < len(layer) else layer[pos]).hex())
            idx[li] = pos // 2
        layer = nxt
    return layer[0], proofs


def batch(batch_id: int, temps_c: list[float], start_ts: int) -> dict:
    readings, leaves = [], []
    for seq, t in enumerate(temps_c):
        centi = round(t * 100)
        ts = start_ts + seq * 1800
        d = digest(batch_id, seq, ts, centi)
        readings.append({"batchId": batch_id, "seq": seq, "timestamp": ts, "centiCelsius": centi,
                         "digest": "0x" + d.hex(), **sign(DEVICE_KEY, d)})
        leaves.append(keccak(d))
    root, proofs = merkle(leaves)
    for r, p in zip(readings, proofs):
        r["proof"] = p
    return {"batchId": batch_id, "device": Account.from_key(DEVICE_KEY).address,
            "merkleRoot": "0x" + root.hex(), "readings": readings}


def main() -> None:
    dev = Account.from_key(DEVICE_KEY).address
    bad = Account.from_key(BAD_DEVICE_KEY).address
    d = digest(1, 0, 1_700_000_000, 450)
    vectors = {
        "format": "digest = keccak256(abi.encodePacked(uint256 batchId, uint32 seq, uint64 timestamp, int16 centiCelsius)); signed with EIP-191 personal_sign",
        "device": {"privateKey": DEVICE_KEY, "address": dev},
        "unregisteredDevice": {"privateKey": BAD_DEVICE_KEY, "address": bad},
        "cases": [
            {"name": "in range 4.50 C", "batchId": 1, "seq": 0, "timestamp": 1_700_000_000, "centiCelsius": 450,
             "digest": "0x" + d.hex(), **sign(DEVICE_KEY, d)},
            {"name": "same reading, unregistered device (must be rejected)", "batchId": 1, "seq": 0,
             "timestamp": 1_700_000_000, "centiCelsius": 450, "digest": "0x" + d.hex(), **sign(BAD_DEVICE_KEY, d)},
            {"name": "tampered: temperature changed after signing (must be rejected)", "batchId": 1, "seq": 0,
             "timestamp": 1_700_000_000, "centiCelsius": 1100, "digest": "0x" + digest(1, 0, 1_700_000_000, 1100).hex(),
             **sign(DEVICE_KEY, d)},
        ],
    }
    samples = {
        "policy": {"minCentiC": 200, "maxCentiC": 800},
        "batches": [
            batch(1, [4.5, 4.8, 5.1, 5.6, 6.0, 5.2], 1_700_000_000),   # compliant
            batch(2, [4.9, 5.3, 7.8, 11.0, 6.1, 5.0], 1_700_100_000),  # one reading above 8 C
        ],
    }
    (HERE / "test_vectors.json").write_text(json.dumps(vectors, indent=2) + "\n")
    (HERE / "sample_readings.json").write_text(json.dumps(samples, indent=2) + "\n")
    print(f"Wrote {HERE/'test_vectors.json'} and {HERE/'sample_readings.json'}")
    print(f"Device address to register on-chain: {dev}")


if __name__ == "__main__":
    main()
