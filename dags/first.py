from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'me',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='example',
    start_date=datetime(2023, 5, 16, 2),
    schedule_interval='@daily'

) as dag:
    task1 = BashOperator(
        task_id='123',
        bash_command="echo example of 1st task"
    )

task1
