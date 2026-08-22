from __future__ import annotations

from copy import deepcopy

from AGENTS import recon_agent, reporting_agent, risk_agent, scope_agent, validation_agent


SYSTEM_ID = "F46"
SYSTEM_NAME = "Penetration Testing"
VERSION = "1.0.0"


def run(ctx: dict) -> dict:
    """Coordinate authorized, non-destructive security assessment governance."""
    state = _normalize(ctx)
    trace = []

    if not state["authorized"]:
        return _result(state, {}, ["authorization_required"], "blocked", trace)

    analyses = {}
    for step, agent in enumerate(
        [scope_agent, recon_agent, validation_agent, risk_agent, reporting_agent], 1
    ):
        analyses[agent.__name__.split(".")[-1]] = agent.run(state)
        trace.append({"step": step, "actor": agent.__name__.split(".")[-1], "event": "completed"})

    blockers = _blockers(state)
    if blockers:
        status = "review_required"
    elif state["human_approval"]:
        status = "approved_for_authorized_assessment"
    else:
        status = "awaiting_human_approval"

    trace.append({"step": len(trace) + 1, "actor": "assessment_authorization_gate", "event": status, "blockers": blockers})
    return _result(state, analyses, blockers, status, trace)


def _normalize(ctx: dict) -> dict:
    state = deepcopy(ctx)
    state.setdefault("authorized", False)
    state.setdefault("human_approval", False)
    state.setdefault("scope_assets", [])
    state.setdefault("rules_of_engagement_approved", False)
    state.setdefault("safe_validation_only", True)
    state.setdefault("non_destructive", True)
    state.setdefault("production_changes_forbidden", True)
    state.setdefault("stop_conditions_defined", False)
    state.setdefault("evidence", [])
    state.setdefault("evidence_integrity_verified", False)
    state.setdefault("findings", [])
    state.setdefault("finding_confidence_reviewed", False)
    state.setdefault("remediation_plan_reviewed", False)
    state.setdefault("retest_plan_defined", False)
    state.setdefault("conflicts", [])
    state.setdefault("unresolved_questions", [])
    return state


def _blockers(state: dict) -> list[str]:
    blockers = []
    if not state["scope_assets"]:
        blockers.append("scope_missing")
    if not state["rules_of_engagement_approved"]:
        blockers.append("rules_of_engagement_missing")
    if not state["safe_validation_only"]:
        blockers.append("unsafe_validation_requested")
    if not state["non_destructive"]:
        blockers.append("destructive_testing_requested")
    if not state["production_changes_forbidden"]:
        blockers.append("production_change_not_forbidden")
    if not state["stop_conditions_defined"]:
        blockers.append("stop_conditions_missing")
    if not state["evidence_integrity_verified"]:
        blockers.append("evidence_integrity_unverified")
    if not state["finding_confidence_reviewed"]:
        blockers.append("finding_confidence_unreviewed")
    if not state["remediation_plan_reviewed"]:
        blockers.append("remediation_plan_unreviewed")
    if not state["retest_plan_defined"]:
        blockers.append("retest_plan_missing")
    if state["conflicts"]:
        blockers.append("unresolved_conflict")
    if state["unresolved_questions"]:
        blockers.append("unresolved_question")
    return blockers


def _result(state: dict, analyses: dict, blockers: list[str], status: str, trace: list[dict]) -> dict:
    return {
        "system_id": SYSTEM_ID,
        "system_name": SYSTEM_NAME,
        "version": VERSION,
        "maturity": "L3 Gold Standard",
        "scope": "authorized non-destructive security assessment only",
        "state": state,
        "analyses": analyses,
        "blockers": blockers,
        "ready_for_approval": not blockers and state["authorized"],
        "status": status,
        "human_authority": "Assessment actions require explicit authorized human approval",
        "trace": trace,
    }
