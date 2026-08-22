import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run  # noqa: E402


def case(**updates):
    value = {
        "authorized": True,
        "human_approval": True,
        "scope_assets": ["test.example.internal"],
        "rules_of_engagement_approved": True,
        "safe_validation_only": True,
        "non_destructive": True,
        "production_changes_forbidden": True,
        "stop_conditions_defined": True,
        "evidence": [{"id": "finding-1"}],
        "evidence_integrity_verified": True,
        "findings": [{"title": "configuration issue", "severity": "medium"}],
        "finding_confidence_reviewed": True,
        "remediation_plan_reviewed": True,
        "retest_plan_defined": True,
        "conflicts": [],
        "unresolved_questions": [],
    }
    value.update(updates)
    return value


SCENARIOS = [
    ("authorized_safe_assessment", case(), "approved_for_authorized_assessment"),
    ("unauthorized", {"authorized": False}, "blocked"),
    ("scope_missing", case(scope_assets=[]), "review_required"),
    ("rules_missing", case(rules_of_engagement_approved=False), "review_required"),
    ("unsafe_validation", case(safe_validation_only=False), "review_required"),
    ("evidence_unverified", case(evidence_integrity_verified=False), "review_required"),
    ("unresolved_governance", case(unresolved_questions=["Is this asset authorized?"]), "review_required"),
    ("awaiting_human_approval", case(human_approval=False), "awaiting_human_approval"),
]


def main():
    rows = []
    for name, payload, expected in SCENARIOS:
        actual = run(payload)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {"system_id": "F46", "version": "1.0.0", "scenario_count": len(rows), "passed": passed, "pass_rate": passed / len(rows), "scenarios": rows}
    Path("benchmarks/heldout_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
