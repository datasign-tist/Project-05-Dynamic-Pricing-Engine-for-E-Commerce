def validate_sales(df):
    assert df["units_sold"].ge(0).all(), "Negative sales detected"
    assert df.isnull().mean().max() < 0.2, "Too many missing values"
    return True
