def forecast_agent(sales_data):
    revenues = [row[1] for row in sales_data]
from app.ml.forecast_model import forecast_next

def forecast_agent(sales_data):
    return forecast_next(sales_data)

    if len(revenues) < 2:
        return {
            "forecast": None,
            "reason": "Insufficient data for forecasting"
        }

    # Simple moving average forecast
    forecast = sum(revenues[-3:]) / min(3, len(revenues))

    return {
        "forecast_next_period": round(forecast, 2),
        "method": "moving_average"
    }
