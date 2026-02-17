from app.memory.memory_analyzer import analyze_memory

def circuit_open():
    analysis = analyze_memory(window_days=1)

    # Too many recent anomalies → open circuit
    if analysis["recent_anomalies"] >= 3:
        return True

    return False
