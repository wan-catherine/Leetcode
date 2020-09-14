from unittest import TestCase
from problems.N1504_Count_Submatrices_With_All_Ones import Solution

class TestSolution(TestCase):
    def test_numSubmat(self):
        mat = [[1, 0, 1],
               [1, 1, 0],
               [1, 1, 0]]
        self.assertEqual(13, Solution().numSubmat(mat))

    def test_numSubmat_1(self):
        mat = [[0, 1, 1, 0],
               [0, 1, 1, 1],
               [1, 1, 1, 0]]
        self.assertEqual(24, Solution().numSubmat(mat))

    def test_numSubmat_2(self):
        mat = [[1, 1, 1, 1, 1, 1]]
        self.assertEqual(21, Solution().numSubmat(mat))

    def test_numSubmat_3(self):
        mat = mat = [[1,0,1],[0,1,0],[1,0,1]]
        self.assertEqual(5, Solution().numSubmat(mat))