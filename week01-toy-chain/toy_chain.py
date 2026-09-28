"""Project 0: a toy blockchain.

Build it in this order, testing each step before the next:
  1. Transaction: sender public key, recipient, amount, ECDSA signature
     (use the ecdsa library with the SECP256k1 curve).
  2. merkle_root(tx_hashes): pairwise SHA-256 up to a single root.
  3. Block: index, timestamp, prev_hash, merkle_root, nonce, transactions.
  4. mine(block, difficulty): proof-of-work on the block header.
  5. validate_chain(chain): check links, proof-of-work, Merkle roots and
     every signature. Return the index of the first bad block, or None.
  6. Tamper test: edit a transaction in block 2 and confirm
     validate_chain reports block 2.
"""
