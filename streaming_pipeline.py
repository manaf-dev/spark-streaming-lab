from pyspark.sql import SparkSession

from etl.extractor import read_events
from etl.transform import transform_data


def initiate_spark():
    spark = (
        SparkSession.builder.appName("SparkStreaming")
        .config("spark.jars", "/streaming/spark/jars")
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
    stream_df = read_events(spark)
    transformed_df = transform_data(stream_df)


if __name__ == "__main__":
    main()
