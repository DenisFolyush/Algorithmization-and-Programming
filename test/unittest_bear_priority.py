import unittest

from src.bear_priority import beers


class TestBeersFunction(unittest.TestCase):

    def test_beers_case1(self):
        self.assertEqual(beers(2, 2, "NNNN"), None)

    def test_beers_case2(self):
        self.assertEqual(beers(6, 3, "YNNYNYNYNYYNYYNYNY"), 2)

    def test_beers_case3(self):
        self.assertEqual(beers(0, 3, "YNNYNYNYNYYNYYNYNYYNYN"), None)


if __name__ == '__main__':
    unittest.main()
