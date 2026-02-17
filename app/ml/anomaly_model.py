from sklearn.ensemble import IsolationForest
from app.ml.features import build_features

_model = None

def train_anomaly_model(sales_data):
    global _model
    df = build_features(sales_data)
    _model = IsolationForest(contamination=0.15, random_state=42)
    _model.fit(df[["revenue", "revenue_lag1", "revenue_lag2"]])
    return _model


def predict_anomaly(sales_data):
    if not _model:
        train_anomaly_model(sales_data)

    df = build_features(sales_data)
    latest = df.tail(1)[["revenue", "revenue_lag1", "revenue_lag2"]]
    score = _model.predict(latest)[0]

    return {
        "anomaly": score == -1,
        "model": "IsolationForest",
        "score": int(score)
    }
