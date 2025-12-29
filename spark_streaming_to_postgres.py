from pyspark.sql import SparkSession

from etl.extractor import read_events
from etl.load import load_to_postgres
from etl.transform import transform_data


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
    print("Starting ETL process...")
    spark = initiate_spark()
    try:
        stream_df = read_events(spark)
        transformed_df = transform_data(stream_df)
        streaming_query = (
            transformed_df.writeStream.foreachBatch(load_to_postgres)
            .outputMode("append")
            .trigger(processingTime="10 seconds")
            .start()
        )
        streaming_query.awaitTermination()

    except KeyboardInterrupt:
        print("Exiting ETL process...")
        for query in spark.streams.active:
            query.stop()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        spark.stop()
        print("ETL process completed.")


if __name__ == "__main__":
    main()
