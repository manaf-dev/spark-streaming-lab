# Project Overview: Spark Structured Streaming Data Ingestion

## Introduction
This project implements a real-time data ingestion pipeline using Apache Spark Structured Streaming. It monitors a directory for new CSV files, processes the data, and loads it into a PostgreSQL database. This system is designed to handle streaming data efficiently, ensuring that incoming events are transformed and stored for downstream analysis.

## System Architecture & Flow

The data pipeline follows a standard ETL (Extract, Transform, Load) process adapted for streaming:

1.  **Source (Extract)**:
    -   The system monitors the `input_data/` directory.
    -   New CSV files placed in this directory are automatically detected and read as a stream.
    -   This is handled by `etl/extractor.py`.

2.  **Processing (Transform)**:
    -   Raw data is validated against a defined schema (`EVENT_SCHEMA`).
    -   **Data Cleaning & Filtering**:
        -   Rows with missing values are dropped.
        -   `product_price` must be greater than 0.
        -   `event_type` is filtered to allow only: "view", "add_to_cart", "purchase", "remove_from_cart".
    -   **Transformations**:
        -   `user_id` and `product_id` are normalized (trimmed and converted to uppercase).
        -   `event_timestamp` is cast to a proper timestamp format.
        -   A `processed_at` timestamp is added to track ingestion time.
    -   This is handled by `etl/transform.py`.

3.  **Sink (Load)**:
    -   The transformed data is written to a PostgreSQL database.
    -   Data is appended to the `user_events` table.
    -   The database includes constraints to enforce data integrity and views (`purchase_analytics`, `user_activity_summary`) for real-time insights.
    -   This is handled by `etl/load.py` using JDBC.

## Key Components

-   **`spark_streaming_to_postgres.py`**: The main entry point of the application. It initializes the SparkSession, orchestrates the ETL pipeline, and manages the streaming query lifecycle.
-   **`etl/extractor.py`**: Responsible for defining the input stream source (CSV files) and applying the initial schema.
-   **`etl/transform.py`**: Contains the logic for data manipulation and enrichment.
-   **`etl/load.py`**: Manages the connection to PostgreSQL and defines how data batches are written to the database.
-   **`scripts/data_generator.py`**: A utility script to generate synthetic CSV data for testing the pipeline.
-   **`docker-compose.yml`**: Orchestrates the containerized environment, likely including the PostgreSQL database service.

## Technologies Used
-   **Apache Spark**: For distributed stream processing.
-   **Python (PySpark)**: The programming language and API used.
-   **PostgreSQL**: The target relational database.
-   **Docker**: For containerization and environment management.
