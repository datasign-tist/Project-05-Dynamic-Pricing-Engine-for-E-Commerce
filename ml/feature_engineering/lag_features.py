def add_lag_features(df, lags=[7, 30]):
    for lag in lags:
        df[f"lag_{lag}"] = df.groupby("product_id")["units_sold"].shift(lag)
    return df
