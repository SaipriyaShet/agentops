def anomaly_confidence(anomaly_result):
    if not anomaly_result.get("anomaly"):
        return 0.2

    deviation = anomaly_result.get("details", {}).get("deviation_percent", 0)

    if deviation >= 0.4:
        return 0.9
    elif deviation >= 0.25:
        return 0.75
    elif deviation >= 0.15:
        return 0.6
    else:
        return 0.4


def forecast_confidence(forecast_result, memory_analysis):
    base = 0.6

    if memory_analysis["recent_events"] >= 5:
        base += 0.15

    if memory_analysis["severity"] == "high":
        base -= 0.1

    return round(min(max(base, 0.3), 0.9), 2)


def action_confidence(anomaly_conf, forecast_conf):
    return round((anomaly_conf * 0.6 + forecast_conf * 0.4), 2)
