# F46 Held-Out Reproducibility Results

Gold Standard validation was executed from a clean GitHub Actions checkout on the `l3-gold-standard` branch.

- Final evidence source run before this record: `32545128976`
- Head: `14d3d51fcc78f767a6833087e705a34c87d33a05`
- Python: 3.10, 3.11, 3.12 all green
- Held-out authorized assessment scenarios: 8/8 expected behaviors passed
- Pass rate: 1.0
- Artifact: `f46-heldout-results`
- Artifact digest: `sha256:d7f42ad96194c6c5447f04d13d525b2bc1c7ea1d17bcbbf42c4afcb5055dac1d`

The suite validates authorization, scope and rules-of-engagement gating, non-destructive defaults, stop conditions, evidence integrity, finding review, remediation/retest governance, conflict handling, and final human approval. It does not execute real-world exploitation or unauthorized access.
