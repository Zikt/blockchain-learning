# Product policy (example)

Copy this to `POLICY.md` in week 6 and adjust it.

| Field | Tomatoes (example) |
|-------|--------------------|
| Temperature range | 2–8 °C |
| Max time from "shipped" to "received" | 48 hours |
| Required steps, in order | harvested → packed → inspected → shipped → received |
| Who may sign each step | harvested, packed: farmer or cooperative · inspected: inspector · shipped: transporter · received: buyer |
| Evidence per step | a data root (Merkle root of readings or documents) |
| Fails if | any signed reading is outside the range, a step is missing or out of order, a step is signed by the wrong role, or transit takes too long |

Questions to answer in your own words:
- What does the chain prove here, and what still depends on trusting a person or a sensor?
- How would a dishonest transporter try to cheat, and which rule catches it?
