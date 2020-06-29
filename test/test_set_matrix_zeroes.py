from unittest import TestCase
from problems.SetMatrixZeroes import Solution

class TestSolution(TestCase):
    def test_setZeroes(self):
        solution = Solution()
        input = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
        solution.setZeroes(input)
        output = [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
        self.assertEqual(input, output)

    def test_setZeroes_1(self):
        solution = Solution()
        input = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
        solution.setZeroes(input)
        output = [
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
        self.assertEqual(input, output)

    def test_setZeroes_special(self):
        solution = Solution()
        input = [[1], [0]]
        solution.setZeroes(input)
        self.assertEqual([[0],[0]], input)

    def test_setZeroes_single_row(self):
        solution = Solution()
        input = [[1,0,3]]
        solution.setZeroes(input)
        self.assertEqual([[0, 0, 0]], input)

    def test_setZeroes_1(self):
        solution = Solution()
        input = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
        solution.setZeroes(input)
        self.assertEqual([[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 3], [0, 0, 0, 0]], input)