from unittest import TestCase
from problems.N1074_Number_Of_Submatrices_That_Sum_To_Target import Solution

class TestSolution(TestCase):
    def test_num_submatrix_sum_target(self):
        self.assertEqual(4, Solution().numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0))

    def test_num_submatrix_sum_target_1(self):
        self.assertEqual(5, Solution().numSubmatrixSumTarget([[1,-1],[-1,1]], target = 0))

    def test_num_submatrix_sum_target_2(self):
        self.assertEqual(0, Solution().numSubmatrixSumTarget(matrix = [[904]], target = 0))
