from unittest import TestCase
from problems.N1605_Find_Valid_Matrix_Given_Row_And_Column_Sums import Solution

class TestSolution(TestCase):
    def test_restoreMatrix(self):
        self.assertListEqual([[3,0],[1,7]], Solution().restoreMatrix(rowSum = [3,8], colSum = [4,7]))

    def test_restoreMatrix_1(self):
        self.assertListEqual([[0,5,0],[6,1,0],[2,0,8]], Solution().restoreMatrix(rowSum = [5,7,10], colSum = [8,6,8]))

    def test_restoreMatrix_2(self):
        self.assertListEqual([[0,9,5],[6,0,3]], Solution().restoreMatrix(rowSum = [14,9], colSum = [6,9,8]))

    def test_restoreMatrix_3(self):
        self.assertListEqual([[1],[0]], Solution().restoreMatrix(rowSum = [1,0], colSum = [1]))

    def test_restoreMatrix_4(self):
        self.assertListEqual([[0]], Solution().restoreMatrix(rowSum = [0], colSum = [0]))
