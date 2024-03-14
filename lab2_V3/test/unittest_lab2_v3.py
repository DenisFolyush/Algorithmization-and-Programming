import unittest

from ..str.lab2_v3 import find_square, check_capacity


class TestFindSquare(unittest.TestCase):

    def test_FindSquare(self):
        self.assertEqual(find_square(9, 2, 3), 9)

    def test_check_capacity(self):
        self.assertTrue(check_capacity(2, 3, 9, 9))


if __name__ == '__main__':
    unittest.main()
