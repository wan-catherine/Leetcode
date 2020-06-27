from unittest import TestCase
from problems.N297_Perfect_Squares import Solution

class TestSolution(TestCase):
    def test_numSquares(self):
        self.assertEqual(3, Solution().numSquares(12))

    def test_numSquares_1(self):
        self.assertEqual(2, Solution().numSquares(13))
