from app.memory.memory_store import load_memory
from app.intelligence.adaptive_rules import adaptive_thresholds
from app.config.system_mode import SYSTEM_MODE
from app.memory.memory_analyzer import analyze_memory

def system_state():
    """
    Returns a snapshot of the current system state.
    """

    memory = load_memory()
    memory_analysis = analyze_memory(window_days=7)
    thresholds = adaptive_thresholds()

    return {
        "system_mode": SYSTEM_MODE,
        "memory_size": len(memory),
        "recent_memory_analysis": memory_analysis,
        "adaptive_thresholds": thresholds,
        "last_events": memory[-5:] if len(memory) >= 5 else memory
    }
