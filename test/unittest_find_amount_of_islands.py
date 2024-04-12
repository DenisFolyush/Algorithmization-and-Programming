import unittest
from src.find_amount_of_islands import IslandCounter


class TestIslandCounter(unittest.TestCase):
    def setUp(self):
        self.island_counter = IslandCounter()

    def test_numIslands(self):
        grid = [['1', '0', '1', '0', '0', '0', '1', '1', '1', '1'],
                ['0', '0', '1', '0', '1', '0', '1', '0', '0', '0'],
                ['1', '1', '1', '1', '0', '0', '1', '0', '0', '0'],
                ['1', '0', '0', '1', '0', '1', '0', '0', '0', '0'],
                ['1', '1', '1', '1', '0', '0', '0', '1', '1', '1'],
                ['0', '1', '0', '1', '0', '0', '1', '1', '1', '1'],
                ['0', '0', '0', '0', '0', '1', '1', '1', '0', '0'],
                ['0', '0', '0', '1', '0', '0', '1', '1', '1', '0'],
                ['1', '0', '1', '0', '1', '0', '0', '1', '0', '0'],
                ['1', '1', '1', '1', '0', '0', '0', '1', '1', '1']]
        self.assertEqual(self.island_counter.num_islands(grid), 5)

    def test_empty_grid(self):
        empty_grid = []
        self.assertEqual(self.island_counter.num_islands(empty_grid), 0)

    def test_no_island(self):
        no_island_grid = [['0']]
        self.assertEqual(self.island_counter.num_islands(no_island_grid), 0)

    def test_one_island(self):
        one_island_grid = [['1']]
        self.assertEqual(self.island_counter.num_islands(one_island_grid), 1)

if __name__ == '__main__':
    unittest.main()