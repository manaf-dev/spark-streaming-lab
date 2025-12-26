def read_events(spark):
    stream_df = (
        spark.readStream.format("csv")
        .option("header", "true")
        .option("maxFilesPerTrigger", 1)
        .load("/data/input_data")
    )
    return stream_df
