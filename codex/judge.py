import argparse
import importlib

from codex.src.utils.spark_session import get_spark


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", required=True)
    args = parser.parse_args()

    spark = get_spark("CodexJudge")

    gen = importlib.import_module(f"codex.src.problems.{args.problem}.generator")
    ref = importlib.import_module(f"codex.src.problems.{args.problem}.reference")
    stu = importlib.import_module(f"codex.src.student.{args.problem}")

    df = gen.build_dataset(spark)
    expected = ref.solve(df).collect()
    actual = stu.solve(df).collect()

    if expected == actual:
        print(f"✅ PASS: {args.problem}")
    else:
        print(f"❌ FAIL: {args.problem}")
        print(f"Expected: {expected}")
        print(f"Got:      {actual}")


if __name__ == "__main__":
    main()
