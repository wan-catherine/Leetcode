from unittest import TestCase
from problems.N1091_Shortest_Path_In_Binary_Matrix import Solution

class TestSolution(TestCase):
    def test_shortestPathBinaryMatrix(self):
        self.assertEqual(2, Solution().shortestPathBinaryMatrix([[0,1],[1,0]]))

    def test_shortestPathBinaryMatrix_1(self):
        self.assertEqual(4, Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))

    def test_shortestPathBinaryMatrix_2(self):
        self.assertEqual(-1, Solution().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))

    def test_shortestPathBinaryMatrix_3(self):
        self.assertEqual(1, Solution().shortestPathBinaryMatrix([[0]]))

    def test_shortestPathBinaryMatrix_4(self):
        self.assertEqual(-1, Solution().shortestPathBinaryMatrix([[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]))
