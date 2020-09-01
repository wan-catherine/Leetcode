from unittest import TestCase
from problems.N542_01_Matrix import Solution

class TestSolution(TestCase):
    def test_updateMatrix(self):
        input = [[0,0,0],
 [0,1,0],
 [0,0,0]]
        output = [[0,0,0],
 [0,1,0],
 [0,0,0]]
        self.assertListEqual(output, Solution().updateMatrix(input))

    def test_updateMatrix_1(self):
        input = [[0,0,0],
 [0,1,0],
 [1,1,1]]
        output = [[0,0,0],
 [0,1,0],
 [1,2,1]]
        self.assertListEqual(output, Solution().updateMatrix(input))
