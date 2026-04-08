from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import logging

# Mock functions representing the ETL tasks
def extract_apis_to_s3(**context):
    logging.info("Connecting to 5+ API sources (Salesforce, Zendesk, etc.)...")
    logging.info("Extracting data with pagination and rate limit handling...")
    logging.info("Saving raw JSON payloads to AWS S3 bucket: s3://raw-data-lake/api_export/")
    return "s3://raw-data-lake/api_export/today_extract.json"

def transform_raw_data(**context):
    logging.info("Pulling raw data from S3...")
    logging.info("Applying data cleansing, normalization, and schema mapping using Pandas...")
    logging.info("Pushing transformed Parquet files back to S3 staging zone...")
    return "s3://staging-data-lake/api_export_cleaned/today_extract.parquet"

default_args = {
    'owner': 'data_engineering_team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'api_to_snowflake_etl',
    default_args=default_args,
    description='Scalable ETL pulling from 5+ APIs to Snowflake via S3',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['etl', 'snowflake', 'api'],
) as dag:

    # Task 1: Extract data from APIs and load into S3
    extract_task = PythonOperator(
        task_id='extract_apis_to_s3',
        python_callable=extract_apis_to_s3,
    )

    # Task 2: Transform the raw data
    transform_task = PythonOperator(
        task_id='transform_raw_data',
        python_callable=transform_raw_data,
    )

    # Task 3: Load structured data into Snowflake using COPY INTO
    copy_to_snowflake_task = SnowflakeOperator(
        task_id='load_to_snowflake',
        snowflake_conn_id='snowflake_default',
        sql="""
            COPY INTO analytics.public.api_consolidated_data
            FROM s3://staging-data-lake/api_export_cleaned/
            STORAGE_INTEGRATION = s3_int
            FILE_FORMAT = (TYPE = PARQUET);
        """,
    )

    # Define task dependencies
    extract_task >> transform_task >> copy_to_snowflake_task
