import importlib

from codex.src.utils.spark_session import get_spark


def test_invalid_tweets():
    spark = get_spark("Test")
    gen = importlib.import_module("codex.src.problems.invalid_tweets.generator")
    ref = importlib.import_module("codex.src.problems.invalid_tweets.reference")
    stu = importlib.import_module("codex.src.student.invalid_tweets")

    df = gen.build_dataset(spark, num_rows=50)
    expected = ref.solve(df).collect()
    actual = stu.solve(df).collect()
    assert expected == actual
