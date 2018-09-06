from unittest import TestCase
from problems.CombinationSumII import Solution

class TestSolution(TestCase):
    def test_combinationSum2(self):
        solution = Solution()
        res = solution.combinationSum2([10,1,2,7,6,1,5], 8)
        l = [
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
        self.assertTrue(l[0] in res)
