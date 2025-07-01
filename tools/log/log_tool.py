import datetime

LOG_FILE = "agent_log.txt"

def log_event(event: str):
    """Logs agent event with timestamp."""
    timestamp = datetime.datetime.now(datetime.UTC).isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {event}\n")