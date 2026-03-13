from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="example_hello",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["example"],
) as dag:
    hello = BashOperator(task_id="say_hello", bash_command="echo 'Hello from Airflow!'")
    date = BashOperator(task_id="print_date", bash_command="date")
    hello >> date
