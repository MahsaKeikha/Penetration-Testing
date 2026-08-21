from orchestration.orchestrator import run
def test_blocked_without_auth(): assert run({})[0]['status']=='blocked'
def test_authorized(): assert len(run({'authorized':True}))==5
