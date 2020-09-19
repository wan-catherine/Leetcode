from unittest import TestCase
from problems.N931_Minimum_Falling_Path_Sum import Solution

class TestSolution(TestCase):
    def test_minFallingPathSum(self):
        self.assertEqual(12, Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
