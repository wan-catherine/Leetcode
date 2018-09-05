from unittest import TestCase
from problems.CombinationSum import Solution

class TestSolution(TestCase):
    def test_combinationSum(self):
        solution = Solution()
        res = solution.combinationSum([2,3,6,7], 7)
        l = [
  [7],
  [2,2,3]
]
        self.assertTrue(l[0] in res)

    def test_combinationSum_8(self):
        solution = Solution()
        res = solution.combinationSum([2,3,5], 8)
        l = [
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
        self.assertTrue(l[0] in res)

    def test_combinationSum_1(self):
        solution = Solution()
        res = solution.combinationSum([1], 2)
        l = [
  [1,1]
]
        self.assertTrue(l[0] in res)
