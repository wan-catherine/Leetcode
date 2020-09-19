from unittest import TestCase
from problems.N1289_Minimum_Falling_Path_Sum_II import Solution

class TestSolution(TestCase):
    def test_minFallingPathSum(self):
        self.assertEqual(13, Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))

    def test_minFallingPathSum_1(self):
        self.assertEqual(7, Solution().minFallingPathSum([[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2]]))
