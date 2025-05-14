def run_full_etl():
    from ml.data_sources.db_data_source import PostgresSalesDataSource
    from ml.feature_engineering.lag_features import add_lag_features

    raw_df = PostgresSalesDataSource("<conn_string>").load_data()
    transformed = add_lag_features(raw_df)
    transformed.to_csv("data/processed_data.csv", index=False)
