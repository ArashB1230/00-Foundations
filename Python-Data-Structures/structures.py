"""Small data structures with explicit, testable behavior."""

from __future__ import annotations

from collections import deque
from typing import Deque, Generic, TypeVar


Value = TypeVar("Value")


class Stack(Generic[Value]):
    def __init__(self) -> None:
        self._items: list[Value] = []

    def push(self, value: Value) -> None:
        self._items.append(value)

    def pop(self) -> Value:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)


class Queue(Generic[Value]):
    def __init__(self) -> None:
        self._items: Deque[Value] = deque()

    def enqueue(self, value: Value) -> None:
        self._items.append(value)

    def dequeue(self) -> Value:
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def __len__(self) -> int:
        return len(self._items)


def binary_search(values: list[Value], target: Value) -> int:
    """Return the first matching index in a sorted list, or -1."""
    left, right = 0, len(values) - 1
    result = -1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            result = middle
            right = middle - 1
        elif values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return result