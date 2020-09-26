from unittest import TestCase
from problems.N1314_Matrix_Block_Sum import Solution

class TestSolution(TestCase):
    def test_matrixBlockSum(self):
        self.assertListEqual([[12,21,16],[27,45,33],[24,39,28]], Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))

    def test_matrixBlockSum_1(self):
        self.assertListEqual([[45,45,45],[45,45,45],[45,45,45]], Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2))
