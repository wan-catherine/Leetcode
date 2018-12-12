from unittest import TestCase
from problems.CombinationSumIII import Solution

class TestSolution(TestCase):
    def test_combinationSum3(self):
        solution = Solution()
        res = solution.combinationSum3(3,7)
        self.assertEqual([[1,2,4]], res)

    def test_combinationSum3_two(self):
        solution = Solution()
        res = solution.combinationSum3(3,9)
        self.assertEqual([[1,2,6], [1,3,5], [2,3,4]], res)
