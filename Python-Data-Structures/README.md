# Python Data Structures

Status: Complete

`structures.py` implements a generic stack, a FIFO queue backed by `collections.deque`, and binary search that returns the first matching index. The tests cover ordering, empty-state behavior through the public API, and duplicate search values.

Run the tests with:

```text
python -m unittest discover -s . -p "test_*.py"
```