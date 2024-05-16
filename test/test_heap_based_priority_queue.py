import unittest

from src.heap_based_priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_insert(self):
        queue = PriorityQueue()
        queue.insert('A', 0)
        self.assertEqual(queue.peek(), 'A')
        queue.insert('B', 20)
        self.assertEqual(queue.peek(), 'B')
        queue.insert('B', 20)
        self.assertEqual(queue.peek(), 'B')
        queue.insert('D', 15)
        self.assertEqual(queue.peek(), 'B')

    def test_extract_max(self):
        queue = PriorityQueue()
        queue.insert('A', 0)
        queue.insert('B', 20)
        queue.insert('C', 20)
        queue.insert('D', 15)
        max_element = queue.extract_max()
        self.assertEqual(max_element.value, 'C')
        self.assertEqual(queue.peek(), 'B')

    def test_size(self):
        queue = PriorityQueue()
        self.assertEqual(queue.size(), 0)
        queue.insert('A', 0)
        queue.insert('B', 20)
        self.assertEqual(queue.size(), 2)
        queue.extract_max()
        self.assertEqual(queue.size(), 1)


if __name__ == '__main__':
    unittest.main()
