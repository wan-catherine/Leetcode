from unittest import TestCase
from problems.N1253_Reconstruct_A_2_Row_Binary_Matrix import Solution

class TestSolution(TestCase):
    def test_reconstructMatrix(self):
        self.assertListEqual([[1,1,0],[0,0,1]], Solution().reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))

    def test_reconstructMatrix_1(self):
        self.assertListEqual([], Solution().reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))

    def test_reconstructMatrix_2(self):
        self.assertListEqual([[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]], Solution().reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))

    def test_reconstructMatrix_3(self):
        self.assertListEqual([], Solution().reconstructMatrix(9, 2, [0,1,2,0,0,0,0,0,2,1,2,1,2]))