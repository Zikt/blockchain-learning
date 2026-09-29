[↑ Trust stack](../README.md)

# Firmware (ESP32)

Your ESP-IDF or PlatformIO project goes here in week 10.

## Test it before trusting it

1. `make vectors` (or `python3 firmware/tools/make_vectors.py`) writes `test_vectors.json` with a fixed test key, readings, digests and signatures.
2. Load the same test key on the ESP32 and sign the same readings. The signatures must match byte for byte (RFC 6979 makes ECDSA deterministic).
3. The negative cases must be rejected by `ProvenanceAnchor`: the unregistered device, and the reading whose temperature was changed after signing.
4. Then use a fresh key generated on the device for real readings. Never flash the test key onto a device you deploy.

`sample_readings.json` holds two signed batches (one compliant, one with an 11 °C reading). Demo stages 5 and 7 use it, so anyone can run the full demo without hardware.
