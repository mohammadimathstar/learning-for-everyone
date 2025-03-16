from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.data_preprocessing import preprocess_data
from scripts.train_model import train_model
from scripts.evaluate_model import evaluate_model
from scripts.deploy_model import deploy_model, check_model_accuracy

default_args = {
    'owner': 'ml_team',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'sla': timedelta(hours=3),
}

dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    description='ML pipeline for training, evaluating, and deploying model',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

data_prep_task = PythonOperator(
    task_id='data_prep',
    python_callable=preprocess_data,
    dag=dag,
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

eval_task = PythonOperator(
    task_id='eval_model',
    python_callable=evaluate_model,
    dag=dag,
)

deploy_task = PythonOperator(
    task_id='deploy_model',
    python_callable=deploy_model,
    dag=dag,
)

monitor_task = PythonOperator(
    task_id='monitor_model',
    python_callable=check_model_accuracy,
    dag=dag,
)

data_prep_task >> train_task >> eval_task >> deploy_task >> monitor_task

