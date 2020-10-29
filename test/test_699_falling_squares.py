from unittest import TestCase
from problems.N699_Falling_Squares import Solution

class TestSolution(TestCase):
    def test_fallingSquares(self):
        self.assertListEqual([2, 5, 5], Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))

    def test_fallingSquares_1(self):
        self.assertListEqual([100,100], Solution().fallingSquares([[100,100],[200,100]]))
