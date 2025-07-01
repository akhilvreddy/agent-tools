from tools.log.log_tool import log_event

def test_log_event_creates_entry():
    log_event("TEST_LOG_ENTRY")
    with open("agent_log.txt", "r") as f:
        logs = f.read()
        assert "TEST_LOG_ENTRY" in logs