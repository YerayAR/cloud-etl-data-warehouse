-- Setup Snowflake Database and Schema
CREATE DATABASE IF NOT EXISTS analytics;
USE DATABASE analytics;
CREATE SCHEMA IF NOT EXISTS public;
USE SCHEMA public;

-- Create Storage Integration for AWS S3
CREATE STORAGE INTEGRATION IF NOT EXISTS s3_int
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = 'S3'
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::123456789012:role/snowflake_role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://staging-data-lake/');

-- Create File Format for Parquet
CREATE OR REPLACE FILE FORMAT my_parquet_format
  TYPE = PARQUET;

-- Create target structured table
CREATE OR REPLACE TABLE api_consolidated_data (
    record_id VARCHAR(255) PRIMARY KEY,
    source_system VARCHAR(50),
    user_email VARCHAR(255),
    event_timestamp TIMESTAMP_NTZ,
    event_type VARCHAR(100),
    event_payload VARIANT,
    processed_at TIMESTAMP_NTZ DEFAULT CURRENT_TIMESTAMP()
);

-- Example Query for Business Analytics
-- SELECT source_system, count(*) as event_count FROM api_consolidated_data GROUP BY 1;
