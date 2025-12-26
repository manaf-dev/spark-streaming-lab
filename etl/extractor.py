from etl.schemas import EVENT_SCHEMA


def read_events(spark):
    stream_df = (
        spark.readStream.format("csv")
        .schema(EVENT_SCHEMA)
        .option("header", "true")
        .option("maxFilesPerTrigger", 1)
        .load("input_data/")
    )
    return stream_df
