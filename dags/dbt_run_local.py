from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    dag_id='dbt_run_local',
    default_args=default_args,
    schedule_interval=None,  # Run on demand
    catchup=False,
) as dag:

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /opt/airflow/ae_education_structure && dbt run'
    )
