# Cloud ETL & Data Warehouse Orchestration

Portfolio project focused on data engineering patterns for ingesting API data, orchestrating ETL jobs, and loading analytics-ready structures into a warehouse.

## What This Project Demonstrates

- Designing an Airflow DAG for scheduled ingestion and dependency management.
- Structuring a cloud ETL flow from API extraction to warehouse loading.
- Modeling a Snowflake-ready schema for downstream reporting.
- Thinking in terms of idempotency, retries, observability, and operational reliability.

## Business Scenario

The use case simulates a pipeline that consolidates data from multiple operational APIs into a centralized analytics layer. The goal is to reduce fragmented reporting, standardize transformations, and make curated data available for BI and decision-making.

## Tech Stack

- Python
- Apache Airflow
- Snowflake
- AWS S3
- SQL

## Repository Structure

```text
cloud-etl-data-warehouse/
|-- dags/
|   `-- api_to_snowflake_dag.py
|-- sql/
|   `-- setup_warehouse.sql
|-- requirements.txt
`-- README.md
```

## Current Contents

- [dags/api_to_snowflake_dag.py](./dags/api_to_snowflake_dag.py): orchestration logic for the ETL flow.
- [sql/setup_warehouse.sql](./sql/setup_warehouse.sql): warehouse setup script with the reporting schema.
- [requirements.txt](./requirements.txt): Python dependencies for the project skeleton.

## End-to-End Flow

1. Extract data from external and internal APIs.
2. Land raw payloads in cloud storage.
3. Transform and validate records before loading.
4. Load curated data into Snowflake.
5. Orchestrate retries, scheduling, and dependencies with Airflow.

## Why It Matters

This project is meant to show data engineering judgment rather than only code volume: pipeline structure, warehouse thinking, and how to frame ETL work so it is maintainable in production.

## Next Improvements

- Add extraction scripts with pagination and rate-limit handling.
- Add tests for schema and data quality checks.
- Add a local mock pipeline for easier reproducibility.
