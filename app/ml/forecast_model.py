from sklearn.linear_model import LinearRegression
from app.ml.features import build_features

_model = None

def train_forecast_model(sales_data):
    global _model
    df = build_features(sales_data)
    X = df[["revenue_lag1", "revenue_lag2"]]
    y = df["revenue"]
    _model = LinearRegression()
    _model.fit(X, y)
    return _model


def forecast_next(sales_data):
    if not _model:
        train_forecast_model(sales_data)

    df = build_features(sales_data)
    latest = df.tail(1)[["revenue", "revenue_lag1"]]
    prediction = _model.predict(latest)[0]

    return {
        "forecast_next_period": round(float(prediction), 2),
        "model": "LinearRegression"
    }
