from pyspark.sql import SparkSession

from config import get_logger
from etl.extractor import read_events
from etl.load import load_to_postgres
from etl.transform import transform_data

logger = get_logger(__name__)


def initiate_spark():
    spark = (
        SparkSession.builder.appName("SparkStreaming")
        .config("spark.jars", "/streaming/spark/jars/postgresql-42.7.6.jar")
        .config(
            "spark.sql.streaming.checkpointLocation", "/streaming/spark/checkpoints"
        )
        .config("spark.sql.shuffle.partitions", "4")
        .master("local[*]")
        .getOrCreate()
    )
    return spark


def main():
    spark = initiate_spark()
    try:
        logger.info("Starting ETL process...")
        stream_df = read_events(spark)
        transformed_df = transform_data(stream_df)
        streaming_query = (
            transformed_df.writeStream.foreachBatch(load_to_postgres)
            .outputMode("append")
            .trigger(processingTime="10 seconds")
            .start()
        )
        logger.info("ETL process is running. Waiting for termination...")
        streaming_query.awaitTermination()

    except KeyboardInterrupt:
        logger.info("Exiting ETL process...")
        for query in spark.streams.active:
            query.stop()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        spark.stop()
        logger.info("ETL process completed.")


if __name__ == "__main__":
    main()
