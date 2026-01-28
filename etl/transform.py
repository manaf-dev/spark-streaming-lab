from pyspark.sql.functions import col, current_timestamp, to_timestamp, trim, upper


def transform_data(stream_df):
    """Transform the streaming DataFrame"""

    stream_df = stream_df.dropna()
    transformed_df = stream_df.filter((col("product_price") > 0))
    transformed_df = transformed_df.filter(
        col("event_type").isin("view", "add_to_cart", "purchase", "remove_from_cart")
    )
    transformed_df = transformed_df.withColumn("user_id", trim(upper(col("user_id"))))
    transformed_df = transformed_df.withColumn(
        "product_id", trim(upper(col("product_id")))
    )
    transformed_df = transformed_df.withColumn(
        "event_timestamp", to_timestamp(col("event_timestamp"), "yyyy-MM-dd HH:mm:ss")
    )
    transformed_df = transformed_df.withColumn("processed_at", current_timestamp())

    return transformed_df
