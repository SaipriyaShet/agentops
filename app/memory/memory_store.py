import json
from datetime import datetime

MEMORY_FILE = "agent_memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_event(event):
    memory = load_memory()
    event["timestamp"] = datetime.utcnow().isoformat()
    memory.append(event)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)
