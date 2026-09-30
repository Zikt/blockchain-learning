"""Week 1: find a nonce whose SHA-256 hash starts with N hex zeros.

TODO:
  1. Hash "hello" + str(nonce) with hashlib.sha256 until the hex digest
     starts with "0000".
  2. Time how long 4, 5 and 6 zeros take. Write the numbers in the README.
"""

import hashlib
import time


def mine(data: str, difficulty: int) -> tuple[int, str]:
    """Return (nonce, hash) where hash starts with `difficulty` zeros."""
    raise NotImplementedError


if __name__ == "__main__":
    for d in (4, 5, 6):
        t0 = time.perf_counter()
        nonce, h = mine("hello", d)
        print(f"difficulty {d}: nonce={nonce} hash={h} in {time.perf_counter() - t0:.2f}s")
