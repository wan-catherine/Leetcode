from unittest import TestCase
from problems.MaximalRectangle import Solution

class TestSolution(TestCase):
    def test_maximalRectangle(self):
        solution = Solution()
        input = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
        res = solution.maximalRectangle(input)
        self.assertEqual(6, res)
