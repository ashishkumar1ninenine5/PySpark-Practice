from pyspark.sql import SparkSession


def get_spark(app_name: str = "Codex") -> SparkSession:
    return (SparkSession.builder
            .master("local[2]")
            .appName(app_name)
            .getOrCreate())
