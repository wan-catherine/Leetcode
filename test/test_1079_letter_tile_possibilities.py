from unittest import TestCase
from problems.N1079_Letter_Tile_Possibilities import Solution

class TestSolution(TestCase):
    def test_numTilePossibilities(self):
        self.assertEqual(8, Solution().numTilePossibilities("AAB"))

    def test_numTilePossibilities_1(self):
        self.assertEqual(188, Solution().numTilePossibilities("AAABBC"))

    def test_numTilePossibilities_2(self):
        self.assertEqual(1, Solution().numTilePossibilities("V"))
