from app.memory.memory_store import load_memory
from datetime import datetime, timedelta

def analyze_memory(window_days=7):
    """
    Analyze recent memory to detect repeated anomalies.
    """
    memory = load_memory()
    now = datetime.utcnow()

    recent_events = []
    for event in memory:
        ts = datetime.fromisoformat(event["timestamp"])
        if now - ts <= timedelta(days=window_days):
            recent_events.append(event)

    anomaly_events = [
        e for e in recent_events
        if e.get("anomaly", {}).get("anomaly")
    ]

    return {
        "recent_events": len(recent_events),
        "recent_anomalies": len(anomaly_events),
        "severity": (
            "high" if len(anomaly_events) >= 3
            else "medium" if len(anomaly_events) == 2
            else "low"
        )
    }
