# Spark Streaming Lab

This project demonstrates a real-time data processing pipeline using Apache Spark Streaming, Python, and PostgreSQL. It's designed to simulate an ETL (Extract, Transform, Load) process where data is continuously streamed, processed, and stored in a relational database.

## Features

-   **Spark Streaming**: Processes incoming data streams in near real-time.
-   **ETL Pipeline**: Includes components for extracting, transforming, and loading data.
-   **PostgreSQL Integration**: Stores processed data in a PostgreSQL database.
-   **Dockerized Environment**: Easily set up and run the entire stack using Docker.
-   **Data Generation**: Script for generating sample data to feed into the streaming pipeline.

## Project Structure

-   `spark_streaming_to_postgres.py`: The main Spark Streaming application.
-   `etl/`: Contains Python modules for ETL logic (extractor, transformer, loader, schemas).
-   `db/`: Database-related files, including `postgres_setup.sql` for initial schema setup.
-   `scripts/`: Utility scripts, such as `data_generator.py` for producing sample data.
-   `docker-compose.yml`: Defines the multi-service Docker application (Spark, PostgreSQL).
-   `Dockerfile`: Dockerfile for building the Spark application image.
-   `requirements.txt`: Python dependencies.
-   `docs/`: Project documentation and architecture details.

## Setup and Usage

For detailed setup and usage instructions, please refer to the [User Guide](./docs/user_guide.md).

