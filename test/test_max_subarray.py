from unittest import TestCase
from problems.MaximumSubarray import Solution

class TestSolution(TestCase):
    def test_maxSubArray(self):
        solution = Solution()
        res = solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(6, res)

    def test_maxSubArray_negative(self):
        solution = Solution()
        res = solution.maxSubArray([-2,-1])
        self.assertEqual(-1, res)

    def test_maxSubArray_single(self):
        solution = Solution()
        res = solution.maxSubArray([-2147483647])
        self.assertEqual(-2147483647, res)