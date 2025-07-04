from pyspark.sql import DataFrame
from pyspark.sql import functions as F


MAX_LEN = 280


def solve(df: DataFrame) -> DataFrame:
    """Return tweets exceeding MAX_LEN characters."""
    return df.where(F.length(F.col("tweet")) > MAX_LEN)
