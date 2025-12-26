from decouple import config

jdbc_properties = {
    "user": config("POSTGRES_USER", default="postgres"),
    "password": config("POSTGRES_PASSWORD", default="postgres"),
    "driver": "org.postgresql.Driver",
}

postgres_properties = {
    "host": config("POSTGRES_HOST", default="localhost"),
    "port": 5432,
    "database": config("POSTGRES_DB", default="postgresdb"),
}

url = f"jdbc:postgresql://{postgres_properties['host']}:{postgres_properties['port']}/{postgres_properties['database']}"


def load_to_postgres(transformed_df):
    transformed_df.write.jdbc(
        url=url,
        table="user_events",
        mode="append",
        properties=jdbc_properties,
    )

    return True
