from sklearn.linear_model import LinearRegression
from app.ml.features import build_features

_model = None
FEATURE_COLUMNS = ["revenue_lag1", "revenue_lag2"]

def train_forecast_model(sales_data):
    global _model
    df = build_features(sales_data)

    X = df[FEATURE_COLUMNS]
    y = df["revenue"]

    _model = LinearRegression()
    _model.fit(X, y)

    return _model


def forecast_next(sales_data):
    global _model

    df = build_features(sales_data)

    if _model is None:
        train_forecast_model(sales_data)

    latest = df.tail(1)[FEATURE_COLUMNS]
    prediction = _model.predict(latest)[0]

    return {
        "forecast_next_period": round(float(prediction), 2),
        "model": "LinearRegression",
        "features_used": FEATURE_COLUMNS
    }
