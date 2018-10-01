from unittest import TestCase
from problems.NQueensII import Solution

class TestSolution(TestCase):
    def test_totalNQueens(self):
        solution = Solution()
        res = solution.totalNQueens(4)
        self.assertEqual(2, res)
