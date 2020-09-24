from unittest import TestCase
from problems.N1140_Stone_Game_II import Solution

class TestSolution(TestCase):
    def test_stoneGameII(self):
        self.assertEqual(10, Solution().stoneGameII([2,7,9,4,4]))
