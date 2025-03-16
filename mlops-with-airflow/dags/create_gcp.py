from airflow import DAG
from airflow.providers.google.cloud.operators.gcs import GCSCreateBucketOperator
from datetime import datetime

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 3, 16),
    'retries': 1,
}

# Initialize the DAG
with DAG(
    'gcs_bucket_creation_dag',
    default_args=default_args,
    description='A simple DAG to create a GCS bucket',
    schedule_interval=None,  # Set to None to run manually
    catchup=False,
) as dag:

    # Task to create a GCS bucket
    create_bucket = GCSCreateBucketOperator(
        task_id='create_gcs_bucket',
        bucket_name='your_unique_bucket_name',  # Replace with your desired bucket name
        storage_class='STANDARD',  # Optional: Set storage class (e.g., 'STANDARD', 'NEARLINE', 'COLDLINE', 'ARCHIVE')
        location='US',  # Optional: Set location (e.g., 'US', 'EU', 'asia-east1')
        project_id='your_project_id',  # Optional: Set your GCP project ID
        gcp_conn_id='google_cloud_default',  # Optional: Set your Airflow GCP connection ID
    )

    # Set task dependencies (if you have more tasks, define their order here)
    create_bucket

