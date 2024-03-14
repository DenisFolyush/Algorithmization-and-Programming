import unittest

from Sliding_windiw import sorting


class TestSorting(unittest.TestCase):
    def test_sorting(self):
        self.assertEqual(sorting([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), (3, 9))
        self.assertEqual(sorting([1, 2, 3, 4, 5]), (-1, -1))
        self.assertEqual(sorting([1]), (-1, -1))


if __name__ == '__main__':
    unittest.main()
