# Reproducibility

Use Python 3.10, 3.11, or 3.12. From a clean checkout run `python -m pip install -e '.[dev]'`, `ruff check .`, `pytest -q`, `python benchmarks/heldout_suite.py`, `python examples/minimal.py`, `python examples/complete.py`, and `python run.py`. The held-out suite writes deterministic JSON to `benchmarks/heldout_results.json`. CI repeats the process on all supported Python versions and publishes the Python 3.12 artifact as `f46-heldout-results`.

# Safety and authorization

F46 is restricted to explicitly authorized, non-destructive security assessment. It does not grant permission to access or test a system. The governance gate blocks unauthorized scope, missing rules of engagement, destructive or unsafe validation, production changes, missing stop conditions, unverified evidence, unreviewed finding confidence, incomplete remediation/retest planning, and unresolved governance. Human approval remains required after blockers clear.
