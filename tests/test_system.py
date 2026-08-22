from orchestration.orchestrator import run


def base_case(**updates):
    case = {
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
    case.update(updates)
    return case


def test_unauthorized_assessment_is_blocked():
    result = run({"authorized": False})
    assert result["status"] == "blocked"
    assert "authorization_required" in result["blockers"]


def test_authorized_safe_assessment_can_be_approved():
    result = run(base_case())
    assert result["system_id"] == "F46"
    assert result["version"] == "1.0.0"
    assert result["status"] == "approved_for_authorized_assessment"
    assert result["blockers"] == []


def test_human_approval_required_after_gates():
    result = run(base_case(human_approval=False))
    assert result["status"] == "awaiting_human_approval"


def test_destructive_or_unsafe_requests_fail_closed():
    result = run(base_case(safe_validation_only=False, non_destructive=False))
    assert "unsafe_validation_requested" in result["blockers"]
    assert "destructive_testing_requested" in result["blockers"]
    assert result["status"] == "review_required"


def test_scope_evidence_and_governance_gaps_fail_closed():
    result = run(base_case(
        scope_assets=[], rules_of_engagement_approved=False,
        evidence_integrity_verified=False, finding_confidence_reviewed=False,
        conflicts=[{"field": "scope", "values": ["A", "B"]}],
        unresolved_questions=["Is this asset authorized?"],
    ))
    expected = {
        "scope_missing", "rules_of_engagement_missing", "evidence_integrity_unverified",
        "finding_confidence_unreviewed", "unresolved_conflict", "unresolved_question",
    }
    assert expected.issubset(set(result["blockers"]))
