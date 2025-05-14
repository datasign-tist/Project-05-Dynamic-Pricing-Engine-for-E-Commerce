from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.run_etl import run_full_etl

with DAG("daily_dynamic_pricing_etl", start_date=datetime(2023, 1, 1), schedule_interval="@daily") as dag:
    task = PythonOperator(
        task_id="run_etl",
        python_callable=run_full_etl
    )
