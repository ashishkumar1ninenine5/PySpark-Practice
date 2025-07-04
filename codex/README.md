# Codex PySpark Judge

This is a minimal setup for practicing PySpark problems offline.

## Structure

```
codex/
  src/
    problems/
      <problem-name>/
        generator.py
        reference.py
        readme.md
    student/
      <problem-name>.py
    utils/
      spark_session.py
  tests/
    test_<problem-name>.py
  judge.py
```

## Usage

Run tests with `pytest`:

```
pytest -q
```

Run a single problem using the CLI:

```
python judge.py --problem invalid_tweets
```
