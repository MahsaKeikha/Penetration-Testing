# F46 Penetration Testing

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

An authorized, non-destructive multi-agent reference system for security assessment governance. F46 separates authorization and scope control, reconnaissance planning, safe validation, risk assessment, remediation planning, reporting, and human approval into explicit stages that can be independently reviewed and tested.

This repository is designed for legitimate security teams, consultants, researchers, students, and engineering organizations studying how to structure a governed penetration-testing workflow. It does not grant permission to test any system and does not provide a path for destructive action, credential theft, persistence, uncontrolled exploitation, production modification, or activity outside approved scope.

## Purpose

Security testing becomes risky when authorization, scope, technical activity, evidence, and remediation are mixed into one informal process. F46 treats these as separate control problems.

The system is designed to help answer:

- What systems and assets are explicitly authorized for assessment?
- What rules of engagement constrain testing?
- What reconnaissance is allowed before validation begins?
- What forms of validation are permitted and safe?
- What stop conditions apply?
- How is evidence preserved and reviewed?
- How are findings prioritized?
- What remediation and retest work remains?
- Who has authority to approve continuation or completion?

## Multi-agent architecture

```text
authorization + rules of engagement
             |
             v
        Scope Agent
             |
             v
         Recon Agent
             |
             v
      Validation Agent
             |
             v
          Risk Agent
             |
             v
      Reporting Agent
             |
             v
 fail-closed governance gates
             |
             v
      human approval
```

The orchestrator coordinates these stages while preserving explicit scope and authorization boundaries throughout the workflow.

## Agents

| Agent | Responsibility | Core question |
|---|---|---|
| Scope Agent | Validate authorization, in-scope assets, exclusions, and rules of engagement | Is this assessment explicitly authorized and bounded? |
| Recon Agent | Plan passive or otherwise approved reconnaissance inside scope | What information can be gathered without exceeding authorization? |
| Validation Agent | Review or coordinate safe, non-destructive validation | Can the suspected issue be confirmed without causing harm or exceeding scope? |
| Risk Agent | Assess finding severity, confidence, business impact, and remediation priority | How important is the finding, and how certain are we? |
| Reporting Agent | Produce a defensible assessment record and remediation/retest plan | Is the final report complete, evidence-backed, and actionable? |

The roles are intentionally separated so a finding cannot silently bypass scope checks, safe-validation constraints, or evidence review.

## Skills layer

Reusable procedures live under `SKILLS/`:

```text
SKILLS/
├── scope_validation.py
├── attack_surface_reasoning.py
├── safe_validation.py
├── risk_scoring.py
└── remediation_planning.py
```

### Scope validation

Verifies that the engagement has explicit authorization, defined assets, exclusions, time boundaries, and approved rules of engagement.

A production scope record should include:

- authorizing organization or owner
- engagement owner
- authorized domains, IPs, applications, APIs, cloud assets, or environments
- explicitly excluded assets
- testing window
- allowed testing classes
- prohibited testing classes
- data-handling constraints
- emergency contacts
- stop conditions
- approval references

If scope is ambiguous, testing should stop until clarified.

### Attack-surface reasoning

Organizes the authorized assessment surface without implying permission to interact with anything outside that surface.

Useful categories can include:

- exposed applications
- APIs
- identity surfaces
- cloud resources
- externally reachable services
- software dependencies
- configuration boundaries
- data flows

This stage is for planning and prioritization, not uncontrolled exploitation.

### Safe validation

Defines the constraints under which a suspected issue may be confirmed. Validation should prefer the minimum action required to establish evidence.

Examples of safe principles include:

- do not modify production data
- do not create persistence
- do not exfiltrate sensitive information
- do not retrieve secrets unless explicitly permitted and necessary
- do not perform destructive stress or denial-of-service testing without separate authorization
- do not bypass stop conditions
- do not expand scope because a new asset was discovered

When validation could create meaningful risk, require explicit human review before proceeding.

### Risk scoring

Separates technical severity from finding confidence and business impact.

A mature risk record can include:

- severity
- confidence
- affected asset
- exposure
- exploit preconditions
- business impact
- data sensitivity
- compensating controls
- remediation priority
- retest requirement

Scores should not be treated as objective truth. Definitions and thresholds should be documented and reviewed.

### Remediation planning

Converts findings into actionable remediation and retest work without confusing discovery with resolution.

Useful remediation records include:

- finding identifier
- owner
- recommended corrective action
- target date
- compensating control
- exception status
- retest status
- residual risk

## Tools layer

F46 includes explicit workflow utilities under `TOOLS/`:

```text
TOOLS/
├── scope_registry.py
├── evidence_store.py
├── risk_register.py
├── remediation_tracker.py
└── approval_gate.py
```

### Scope registry

Maintains the canonical authorized scope and exclusions. Every downstream stage should reference this source of truth rather than reconstructing scope from memory.

### Evidence store

Preserves the evidence supporting a finding. Production implementations should retain timestamps, source identifiers, analyst identity, tool metadata, hashes where appropriate, and access controls.

### Risk register

Maintains finding severity, confidence, ownership, and disposition.

### Remediation tracker

Tracks corrective actions and retest status so the assessment lifecycle continues beyond report delivery.

### Approval gate

Represents the control boundary between automated eligibility and human authority. In production, approval should be authenticated and auditable.

## End-to-end workflow

A typical F46 engagement follows this sequence:

1. Load the authorization record and rules of engagement.
2. Validate that scope is non-empty, explicit, and approved.
3. Register in-scope and out-of-scope assets.
4. Review permitted reconnaissance activities.
5. Build an authorized attack-surface view.
6. Identify candidate findings or hypotheses.
7. Determine whether each candidate can be validated safely.
8. Block any validation that exceeds scope, violates rules, or lacks stop conditions.
9. Record evidence for validated findings.
10. Assign finding confidence and risk.
11. Create remediation and retest requirements.
12. Produce a report with evidence, limitations, and unresolved questions.
13. Apply fail-closed governance gates.
14. Require explicit human approval before the engagement is treated as complete or any higher-risk action is authorized.

## Authorized scope and rules of engagement

F46 assumes a valid written authorization framework exists before any testing begins.

Rules of engagement should define at minimum:

- who authorized the work
- which assets are in scope
- which assets are excluded
- testing dates and times
- permitted techniques
- prohibited techniques
- production-change restrictions
- credential-handling rules
- data-handling rules
- third-party restrictions
- stop conditions
- emergency contact paths
- notification requirements
- evidence-retention rules

A verbal assumption, inherited access, or technical reachability is not equivalent to authorization.

## Non-destructive validation model

This reference implementation is intentionally limited to safe and bounded validation.

The system should not autonomously:

- execute destructive payloads
- create persistence
- change production configurations
- delete or corrupt data
- disable controls
- perform credential theft
- exfiltrate sensitive data
- launch denial-of-service activity
- pivot to newly discovered assets outside scope
- test third-party infrastructure without explicit authorization

Where proof requires a potentially disruptive action, the workflow should mark the finding as requiring additional human-approved validation rather than attempting it automatically.

## Stop conditions

A professional testing workflow needs explicit stop conditions.

Examples include:

- unexpected production instability
- evidence of actual compromise by a third party
- exposure of highly sensitive data beyond the approved handling plan
- discovery of an out-of-scope system in the interaction path
- unexpected service degradation
- legal or privacy concern
- conflicting authorization
- uncertainty about whether a proposed action is permitted

Stop conditions should trigger immediate escalation, not autonomous workaround behavior.

## Evidence integrity

A finding is only as defensible as its evidence.

Evidence records should preserve:

- finding identifier
- affected asset
- timestamp
- source or observation method
- analyst or system identity
- environment
- relevant configuration or version
- confidence
- redaction state
- hash or integrity metadata where appropriate

Reports should distinguish observed facts from hypotheses, interpretation, and remediation advice.

## Finding confidence

Not every suspected weakness should be reported as confirmed.

Useful confidence states include:

```text
UNVERIFIED
PARTIALLY VERIFIED
VERIFIED WITH SAFE EVIDENCE
REQUIRES ADDITIONAL AUTHORIZED VALIDATION
FALSE POSITIVE
```

The system should never inflate confidence merely because a candidate finding matches a known vulnerability pattern.

## Risk assessment

Risk should combine technical severity with context.

Factors can include:

- exposure
- privilege required
- user interaction required
- exploitability
- affected data
- affected business function
- compensating controls
- detection capability
- blast radius
- persistence potential
- regulatory impact

Risk prioritization should remain reviewable and should not replace the organization's own risk methodology.

## Remediation and retest

A penetration test is incomplete if findings are delivered without a remediation path.

For each material finding, the workflow should track:

- remediation owner
- corrective action
- due date
- interim mitigation
- exception decision
- residual risk
- retest criteria
- retest result

A retest should verify the specific corrective objective rather than repeating the entire assessment by default.

## Human approval model

Human approval is required after automated gates pass. It cannot override an active blocker without the underlying condition first being resolved or formally re-scoped through the real engagement process.

Conceptually:

```text
authorized scope valid
        |
        v
safe validation complete
        |
        v
evidence integrity reviewed
        |
        v
risk and remediation complete
        |
        v
no unresolved governance blockers
        |
        v
HUMAN APPROVAL REQUIRED
```

## Fail-closed governance

F46 is designed to block continuation or completion when required controls are missing.

Examples include:

```text
AUTHORIZATION MISSING
SCOPE EMPTY
RULES OF ENGAGEMENT UNAPPROVED
ASSET OUT OF SCOPE
SAFE VALIDATION DISABLED
DESTRUCTIVE ACTION REQUESTED
STOP CONDITIONS MISSING
EVIDENCE INTEGRITY UNVERIFIED
FINDING CONFIDENCE UNREVIEWED
REMEDIATION PLAN INCOMPLETE
RETEST PLAN INCOMPLETE
HUMAN APPROVAL REQUIRED
```

The system should never guess that an asset is authorized or interpret lack of an explicit prohibition as permission.

## Quick start

Install the project with development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run static checks and tests:

```bash
ruff check .
pytest -q
```

Run the held-out suite:

```bash
python benchmarks/heldout_suite.py
```

Run the examples:

```bash
python examples/minimal.py
python examples/complete.py
python run.py
```

The examples are deterministic reference cases and do not perform real-world exploitation.

## Benchmarks and evaluation

The repository includes:

```text
benchmarks/cases.json
benchmarks/heldout_suite.py
benchmarks/RESULTS.md
evals/evaluate.py
```

Evaluation should focus on governance and assessment quality, not attack success.

Useful dimensions include:

- scope enforcement
- out-of-scope rejection
- rules-of-engagement compliance
- destructive-action refusal
- stop-condition handling
- evidence completeness
- confidence calibration
- risk consistency
- remediation completeness
- retest planning
- human-gate enforcement

Strong held-out cases should include ambiguous authorization, third-party assets, accidental scope expansion, incomplete evidence, conflicting risk assessments, and requests for prohibited destructive validation.

## Observability and auditability

A production implementation should record:

- engagement identifier
- scope version
- authorization reference
- rules-of-engagement version
- agent execution status
- evidence identifiers
- finding status
- risk changes
- remediation updates
- blocked actions
- escalation events
- approval events

This makes it possible to reconstruct why a finding was accepted, rejected, escalated, or deferred.

## CI and reproducibility

The repository includes GitHub Actions under `.github/workflows/ci.yml`.

CI should cover:

- syntax and import integrity
- scope-control tests
- safe-validation tests
- destructive-action rejection
- evidence-state tests
- remediation-tracker tests
- approval-gate tests
- benchmark regressions
- held-out cases

Production systems should additionally validate integrations only against sandbox or explicitly authorized test environments.

## Security boundaries

The repository itself should not become a source of sensitive engagement data. Production deployments should use appropriate controls for:

- secrets
- customer data
- vulnerability evidence
- screenshots and logs
- credentials provided for testing
- regulated information
- third-party data

Apply least privilege, encryption, access controls, retention limits, and redaction requirements consistent with the engagement contract.

## Extending F46

Safe extensions include:

- asset inventory integration
- vulnerability-management integration
- evidence normalization
- finding deduplication
- remediation workflow integration
- ticketing connectors
- retest workflow automation
- reporting templates
- risk-model adapters
- cloud or API assessment modules that remain scope-aware
- sandbox-only validation harnesses

Any extension that can create external side effects should preserve explicit authorization checks and human approval.

## Example use cases

F46 can serve as a reference architecture for:

- internal authorized security assessments
- consultant engagement workflows
- secure-development validation
- cloud security assessment governance
- API security review coordination
- remediation and retest tracking
- teaching penetration-testing governance
- evaluating multi-agent security workflow design

It is not intended for unauthorized testing or offensive automation.

## Repository map

```text
.github/workflows/ci.yml
AGENTS/
├── scope_agent.py
├── recon_agent.py
├── validation_agent.py
├── risk_agent.py
└── reporting_agent.py
SKILLS/
├── scope_validation.py
├── attack_surface_reasoning.py
├── safe_validation.py
├── risk_scoring.py
└── remediation_planning.py
TOOLS/
├── scope_registry.py
├── evidence_store.py
├── risk_register.py
├── remediation_tracker.py
└── approval_gate.py
benchmarks/
config/
docs/
evals/
examples/
memory/
observability/
orchestration/
tests/
run.py
pyproject.toml
CITATION.cff
LICENSE
README.md
SECURITY.md
```

## L3 Gold Standard candidate meaning

The L3 candidate label indicates that the repository is designed to be independently reviewable and reproducible with explicit specialist roles, deterministic governance controls, held-out cases, tests, and documented audit evidence.

It does not imply authorization to test any real system, certification of a testing methodology, or permission to bypass organizational controls.

See `docs/L3_AUDIT.md` and `docs/REPRODUCIBILITY_AND_SAFETY.md` for the repository's maturity evidence and safety assumptions.

## Citation and reuse

The repository includes `CITATION.cff` for academic and technical citation and is MIT licensed subject to the license terms.

## Design principles

1. Authorization before technical activity.
2. Explicit scope and exclusions.
3. Rules of engagement as a hard control boundary.
4. Minimal, non-destructive validation.
5. Evidence before confidence.
6. Risk assessment separate from raw technical findings.
7. Remediation and retest as part of the assessment lifecycle.
8. Fail closed when scope, evidence, or governance is incomplete.
9. Preserve auditability across every stage.
10. Keep consequential testing authority with accountable humans.

## Responsible use

Use F46 only for security assessments that are explicitly authorized by the owner or other legitimate authority. Validate scope, rules of engagement, legal requirements, evidence-handling procedures, and organizational policies independently. This repository is a governance and workflow reference, not permission to access, test, disrupt, or modify systems.