from datetime import datetime

def get_timestamp(human_readable: bool = True) -> str:
    """Return the current timestamp."""
    now = datetime.utcnow()
    return now.strftime("%Y-%m-%d %H:%M:%S UTC") if human_readable else str(int(now.timestamp()))