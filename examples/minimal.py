import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import run  # noqa: E402

case = {
    "authorized": True,
    "scope_assets": ["test.example.internal"],
    "rules_of_engagement_approved": True,
    "safe_validation_only": True,
    "non_destructive": True,
    "production_changes_forbidden": True,
    "stop_conditions_defined": True,
    "evidence_integrity_verified": True,
    "finding_confidence_reviewed": True,
    "remediation_plan_reviewed": True,
    "retest_plan_defined": True,
    "human_approval": False,
}
result = run(case)
assert result["status"] == "awaiting_human_approval"
print(result["status"])
