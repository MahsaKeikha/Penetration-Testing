# F46 Penetration Testing

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

An authorized, non-destructive multi-agent security assessment reference system. Five specialized agents cover scope, reconnaissance planning, safe validation, risk assessment, and reporting. The orchestration layer keeps testing inside explicit authorization and rules of engagement and fails closed when scope, evidence integrity, stop conditions, remediation planning, or human approval is incomplete.

## Authorized assessment scope

F46 is intended only for systems the assessor is explicitly authorized to evaluate. It does not automate destructive actions, persistence, credential theft, uncontrolled exploitation, production modification, or activity outside approved scope. Validation is designed to remain non-destructive and evidence-focused.

## Fail-closed governance

Assessment cannot proceed when authorization is absent, scope is empty, rules of engagement are unapproved, safe-validation constraints are disabled, destructive testing is requested, production changes are not forbidden, stop conditions are missing, evidence integrity is unverified, finding confidence has not been reviewed, remediation/retest planning is incomplete, or governance conflicts/questions remain unresolved. Human approval is required after all automated gates pass.

## Reproduce

```bash
python -m pip install -e '.[dev]'
ruff check .
pytest -q
python benchmarks/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

CI validates Python 3.10, 3.11, and 3.12 and publishes held-out results from Python 3.12.

## Structure

- `AGENTS/`: scope, reconnaissance planning, validation, risk, and reporting roles
- `SKILLS/`: scope validation, safe validation, risk scoring, remediation planning
- `TOOLS/`: scope registry, evidence store, risk register, remediation tracker, approval gate
- `orchestration/`: fail-closed assessment authorization flow
- `benchmarks/`: held-out authorized-assessment suite
- `examples/`: clean-checkout minimal and complete examples
- `tests/`: authorization and governance red-team tests
- `docs/`: architecture, safety, reproducibility, and L3 audit evidence

L3 denotes an independently reviewable and reproducible authorized-assessment reference implementation. It does not grant permission to test any system and does not replace contracts, rules of engagement, organizational approval, legal review, or human security judgment.
