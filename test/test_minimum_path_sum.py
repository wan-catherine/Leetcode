from unittest import TestCase
from problems.MinimumPathSum import Solution

class TestSolution(TestCase):
    def test_minPathSum(self):
        solution = Solution()
        input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
        res = solution.minPathSum(input)
        self.assertEqual(7, res)
