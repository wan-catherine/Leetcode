from unittest import TestCase
from problems.NQueens import Solution

class TestSolution(TestCase):
    def test_solveNQueens(self):
        solution = Solution()
        res = solution.solveNQueens(4)
        expected = [
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]
        self.assertEqual(res, expected)

