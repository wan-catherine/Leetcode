from unittest import TestCase
from problems.N1329_Sort_The_Matrix_Diagonally import Solution

class TestSolution(TestCase):
    def test_diagonalSort(self):
        self.assertListEqual([[1,1,1,1],[1,2,2,2],[1,2,3,3]], Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
