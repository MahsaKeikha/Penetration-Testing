from orchestration.orchestrator import run


def test_missing_authorization_is_blocked():
    result = run({})
    assert result["status"] == "blocked"
    assert result["blockers"] == ["authorization_required"]


def test_incomplete_authorized_assessment_requires_review():
    result = run({"authorized": True})
    assert result["system_id"] == "F46"
    assert result["status"] == "review_required"
    assert result["human_approval_required"] is True
