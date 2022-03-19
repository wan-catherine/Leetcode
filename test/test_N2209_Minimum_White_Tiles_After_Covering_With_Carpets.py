from unittest import TestCase
from problems.N2209_Minimum_White_Tiles_After_Covering_With_Carpets import Solution

class TestSolution(TestCase):
    def test_minimum_white_tiles(self):
        self.assertEqual(2, Solution().minimumWhiteTiles(floor = "10110101", numCarpets = 2, carpetLen = 2))

    def test_minimum_white_tiles_1(self):
        self.assertEqual(0, Solution().minimumWhiteTiles(floor = "11111", numCarpets = 2, carpetLen = 3))