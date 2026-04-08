# Cloud ETL & Data Warehouse Orchestration

This repository contains the architecture and codebase for a highly scalable ETL (Extract, Transform, Load) pipeline. It demonstrates the ability to extract data from multiple disparate API sources, transform large volumes of raw logs, and load the structured data into a Snowflake data warehouse for downstream analytics and reporting.

## 🚀 Project Overview

- **Objective:** Consolidate data from 5+ different API sources into a centralized Snowflake warehouse.
- **Volume:** Capable of transforming over 2TB of raw logs.
- **Orchestration:** Directed and scheduled using Apache Airflow.
- **Languages & Tools:** Python, Airflow, Snowflake, AWS S3.

## 🏗 Architecture Workflow

1. **Extraction:** Python scripts fetch data from multiple REST APIs (e.g., Salesforce, Zendesk, Stripe, Custom Internal APIs).
2. **Data Lake Storage:** Raw JSON/CSV logs are dumped into an **AWS S3** bucket (Raw Zone).
3. **Transformation:** Airflow triggers Python/Pandas jobs (or Snowflake Snowpark) to clean, normalize, and validate the raw data.
4. **Data Warehouse (Load):** The transformed data is loaded into **Snowflake** utilizing `COPY INTO` commands and Snowpipe for structured reporting.
5. **Orchestration:** **Apache Airflow** DAGs manage dependencies, retries, and failure alerts across the entire pipeline.

## 📂 Repository Structure

```text
cloud-etl-data-warehouse/
├── dags/                     # Apache Airflow DAG definitions
│   └── api_to_snowflake_dag.py
├── scripts/                  # Python extraction and transformation scripts
│   ├── extract_apis.py
│   └── transform_logic.py
├── sql/                      # Snowflake SQL scripts for schema definition and COPY INTO
│   ├── setup_warehouse.sql
│   └── load_tables.sql
├── tests/                    # Unit tests for data quality and pipeline validation
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🛠 Tech Stack

- **Orchestration:** Apache Airflow
- **Cloud Storage:** AWS S3
- **Data Warehouse:** Snowflake
- **Language:** Python 3.10+ (requests, pandas, snowflake-connector-python)

## 💡 Highlighted Skills
- Advanced Python scripting for API pagination and rate-limit handling.
- Designing idempotent Airflow DAGs.
- Cloud storage integration (S3 boto3).
- Data warehousing strategy (Star Schema, Fact/Dimension tables) in Snowflake.
