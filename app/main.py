from ml.utils.schema_validator import load_schema, validate_schema
import pandas as pd

df = pd.read_csv("data/sales_data.csv", parse_dates=["timestamp"])
schema = load_schema("config/schema/data_schema.yaml")

validate_schema(df, schema)
print("✅ Schema validation passed.")


# git checkout -b phase-2-data-prep
# git add .
# git commit -m "✨ Added OOP data connectors, feature engineering, and ETL flow"
# git push origin phase-2-data-prep
