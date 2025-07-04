from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StringType
import random
import string


def random_tweet(length: int) -> str:
    letters = string.ascii_letters + string.digits + " "
    return ''.join(random.choice(letters) for _ in range(length))


def build_dataset(spark: SparkSession = None, num_rows: int = 100) -> 'DataFrame':
    if spark is None:
        from ...utils.spark_session import get_spark
        spark = get_spark("Generator")

    rows = []
    for _ in range(num_rows):
        length = random.randint(10, 350)
        rows.append((random_tweet(length),))
    return spark.createDataFrame(rows, ["tweet"])
