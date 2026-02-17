from app.memory.memory_store import load_memory

def adaptive_thresholds(
    base_drop=0.8,
    base_spike=1.2,
    min_drop=0.6,
    max_spike=1.4
):
    """
    Adjust anomaly thresholds based on historical behavior.
    """

    memory = load_memory()
    anomalies = [
        e for e in memory
        if e.get("anomaly", {}).get("anomaly")
    ]

    anomaly_count = len(anomalies)

    # Start with base thresholds
    drop_threshold = base_drop
    spike_threshold = base_spike

    # If many anomalies → become more sensitive
    if anomaly_count >= 5:
        drop_threshold -= 0.05
        spike_threshold += 0.05

    if anomaly_count >= 10:
        drop_threshold -= 0.05
        spike_threshold += 0.05

    # Clamp thresholds (VERY IMPORTANT)
    drop_threshold = max(drop_threshold, min_drop)
    spike_threshold = min(spike_threshold, max_spike)

    return {
        "drop_threshold": round(drop_threshold, 2),
        "spike_threshold": round(spike_threshold, 2),
        "anomaly_history": anomaly_count
    }
