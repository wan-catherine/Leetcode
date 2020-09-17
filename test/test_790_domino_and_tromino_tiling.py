from unittest import TestCase
from problems.N790_Domino_And_Tromino_Tiling import Solution

class TestSolution(TestCase):
    def test_numTilings(self):
        self.assertEqual(5, Solution().numTilings(3))
