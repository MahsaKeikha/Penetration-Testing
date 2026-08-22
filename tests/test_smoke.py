from orchestration.orchestrator import run


def test_blocked_without_auth():
    result = run({})
    assert result["status"] == "blocked"
    assert "authorization" in result["blockers"]


def test_authorized_incomplete_case_is_fail_closed():
    result = run({"authorized": True})
    assert result["system_id"] == "F46"
    assert result["status"] == "blocked"
    assert result["human_approval_required"] is True
