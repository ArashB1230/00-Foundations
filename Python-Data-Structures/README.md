# Python Data Structures

This project focuses on the core data structures that appear repeatedly in algorithmic and ML work: stacks, queues, and search logic.

## Goal

The goal is to implement and validate simple generic data structures with correct behavior and predictable performance. This project is designed to strengthen the fundamentals behind more complex algorithms and data pipelines.

## What you will practice

- building a stack with LIFO behavior,
- building a queue with FIFO behavior,
- implementing generic data structures in Python,
- testing edge cases and correct ordering,
- understanding binary search and duplicate handling.

## Topics covered

### Stack
A stack stores elements in last-in, first-out order. It is useful in recursion, parsing, and backtracking problems.

### Queue
A queue stores elements in first-in, first-out order. It is helpful for scheduling, breadth-first traversal, and processing pipelines.

### Binary search
Binary search is used to efficiently find a target value in sorted data. In this project, it is also used to understand duplicate-handling behavior and how to return a meaningful result when a value is absent.

## Why this matters

ML pipelines, algorithm design, and data processing often rely on these ideas indirectly. Even if the final project is a model, the logic behind the pipeline is frequently built on these structures.

## Validation

Run the tests from this folder:

```bash
python -m unittest discover -s . -p "test_*.py"
```

## Learning takeaway

A strong foundation in data structures makes later work in optimization, search, pipelines, and modeling easier to reason about and debug.
