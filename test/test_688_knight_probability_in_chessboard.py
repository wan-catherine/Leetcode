from unittest import TestCase
from problems.N688_Knight_Probability_In_Chessboard import Solution

class TestSolution(TestCase):
    def test_knightProbability(self):
        self.assertEqual(0.0625, Solution().knightProbability(3, 2, 0, 0))

    def test_knightProbability_1(self):
        self.assertEqual(1, Solution().knightProbability(1, 0, 0, 0))

    def test_knightProbability_2(self):
        self.assertEqual(0.015625, Solution().knightProbability(3, 3, 0, 0))
