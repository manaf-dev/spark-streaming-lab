from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

EVENT_SCHEMA = StructType(
    [
        StructField("user_id", IntegerType(), False),
        StructField("event_type", StringType(), False),
        StructField("event_timestamp", TimestampType(), False),
        StructField("product_id", StringType(), False),
        StructField("product_name", StringType(), False),
        StructField("product_price", DoubleType(), False),
        StructField("session_id", StringType(), False),
    ]
)
