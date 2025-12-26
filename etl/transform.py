from pyspark.sql.functions import col, current_timestamp, to_timestamp


def transform_data(stream_df):
    transformed_df = stream_df.withColumn(
        "event_timestamp", to_timestamp(col("event_timestamp"), "yyyy-MM-dd HH:mm:ss")
    )

    transformed_df = transformed_df.withColumn("processed_at", current_timestamp())

    return transformed_df
