from statistics import mean
from app.intelligence.adaptive_rules import adaptive_thresholds

from app.ml.anomaly_model import predict_anomaly

def anomaly_agent(sales_data):
    return predict_anomaly(sales_data)

def anomaly_agent(sales_data):
    """
    Detect anomalies using adaptive thresholds.
    """

    revenues = [row[1] for row in sales_data]

    if len(revenues) < 3:
        return {
            "anomaly": False,
            "severity": "low",
            "reason": "Insufficient data"
        }

    thresholds = adaptive_thresholds()
    DROP = thresholds["drop_threshold"]
    SPIKE = thresholds["spike_threshold"]

    historical_avg = mean(revenues[:-1])
    latest = revenues[-1]


    # Revenue drop
    if latest < historical_avg * DROP:
        deviation = round((historical_avg - latest) / historical_avg, 2)
        return {
            "anomaly": True,
            "type": "drop",
            "severity": "high" if deviation > 0.3 else "medium",
            "adaptive_thresholds": thresholds,
            "details": {
                "latest_revenue": latest,
                "historical_average": round(historical_avg, 2),
                "deviation_percent": deviation
            }
        }

    if latest > historical_avg * SPIKE:
        deviation = round((latest - historical_avg) / historical_avg, 2)
        return {
            "anomaly": True,
            "type": "spike",
            "severity": "medium",
            "adaptive_thresholds": thresholds,
            "details": {
                "latest_revenue": latest,
                "historical_average": round(historical_avg, 2),
                "deviation_percent": deviation
            }
        }

    return {
        "anomaly": False,
        "severity": "low",
        "adaptive_thresholds": thresholds,
        "details": {
            "latest_revenue": latest,
            "historical_average": round(historical_avg, 2)
        }
    }
