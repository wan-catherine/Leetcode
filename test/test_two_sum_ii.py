from unittest import TestCase
from problems.TwoSumII import Solution

class TestSolution(TestCase):
    def test_twoSum(self):
        solution = Solution()
        res = solution.twoSum([2,7,11,15], 9)
        self.assertEqual([1,2], res)
