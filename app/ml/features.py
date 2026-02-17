import pandas as pd

def build_features(sales_data):
    df = pd.DataFrame(sales_data, columns=["date", "revenue"])
    df["revenue_lag1"] = df["revenue"].shift(1)
    df["revenue_lag2"] = df["revenue"].shift(2)
    df = df.dropna()
    return df
