
import yaml
import pandas as pd
import numpy as np

def load_schema(schema_path="config/schema/data_schema.yaml"):
    with open(schema_path, "r") as f:
        return yaml.safe_load(f)

def validate_schema(df: pd.DataFrame, schema: dict, dataset_name="sales_data"):
    issues = []
    expected_cols = schema[dataset_name]["columns"]

    for col_meta in expected_cols:
        name = col_meta["name"]
        dtype = col_meta["dtype"]
        required = col_meta.get("required", False)
        constraints = col_meta.get("constraints", {})

        if required and name not in df.columns:
            issues.append(f"Missing required column: {name}")
            continue

        if name not in df.columns:
            continue  # Skip non-required fields

        col_data = df[name]

        # Type checks
        if dtype == "int" and not pd.api.types.is_integer_dtype(col_data):
            issues.append(f"Column {name} is not int")
        elif dtype == "float" and not pd.api.types.is_float_dtype(col_data):
            issues.append(f"Column {name} is not float")
        elif dtype == "string" and not pd.api.types.is_string_dtype(col_data):
            issues.append(f"Column {name} is not string")
        elif dtype == "datetime" and not pd.api.types.is_datetime64_any_dtype(col_data):
            issues.append(f"Column {name} is not datetime")
        elif dtype == "bool" and not pd.api.types.is_bool_dtype(col_data):
            issues.append(f"Column {name} is not boolean")

        # Constraint checks
        if "min" in constraints:
            if (col_data < constraints["min"]).any():
                issues.append(f"Column {name} has values below min {constraints['min']}")

    if issues:
        raise ValueError("Schema validation failed:\n" + "\n".join(issues))
    return True
