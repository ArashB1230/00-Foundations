import unittest

from structures import Queue, Stack, binary_search


class DataStructureTests(unittest.TestCase):
    def test_stack_is_last_in_first_out(self) -> None:
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)

    def test_queue_is_first_in_first_out(self) -> None:
        queue = Queue[str]()
        queue.enqueue("first")
        queue.enqueue("second")
        self.assertEqual(queue.dequeue(), "first")
        self.assertEqual(queue.dequeue(), "second")

    def test_binary_search_returns_first_duplicate(self) -> None:
        self.assertEqual(binary_search([1, 2, 2, 2, 4], 2), 1)
        self.assertEqual(binary_search([1, 2, 4], 3), -1)


if __name__ == "__main__":
    unittest.main()