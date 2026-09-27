# SQL Analytics

Status: Complete

`analytics.py` creates an orders schema and demonstrates parameterized inserts, grouped customer totals, and a window-function ranking query. The tests use an in-memory SQLite database, so they are fast and reproducible.

Run the tests with:

```text
python -m unittest discover -s . -p "test_*.py"
```