from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="etl_scrapy_dag",
    start_date=datetime(2026,1,29),
    schedule_interval="@daily",
    catchup=False,
    description="Run Scrapy ETL via Airflow"
) as dag:

    run_scrapy = BashOperator(
        task_id="run_scrapy_etl",
        bash_command="""
        cd /mnt/c/Users/HP/PycharmProjects/ETLProject1/etlproject &&
        source ../airflow_venv/bin/activate &&
        scrapy crawl etl
        """
    )

    run_scrapy
