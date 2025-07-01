import json
import os

MEMORY_FILE = "agent_memory.json"

def save_memory(key: str, value: str):
    """Save a key-value pair to agent memory."""
    memory = load_memory()
    memory[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def load_memory() -> dict:
    """Load memory from file."""
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)