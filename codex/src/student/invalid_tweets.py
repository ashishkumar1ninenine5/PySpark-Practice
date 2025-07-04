from pyspark.sql import DataFrame
from pyspark.sql import functions as F


MAX_LEN = 280


def solve(df: DataFrame) -> DataFrame:
    """Student solution: filter tweets with length > 280."""
    return df.filter(F.length(F.col("tweet")) > MAX_LEN)
