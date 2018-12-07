from unittest import TestCase
from problems.MinimumSizeSubarraySum import Solution

class TestSolution(TestCase):
    def test_minSubArrayLen(self):
        solution = Solution()
        res = solution.minSubArrayLen(7, [2,3,1,2,4,3])
        self.assertEqual(2, res)

    def test_minSubArrayLen_two(self):
        solution = Solution()
        res = solution.minSubArrayLen(15, [5,1,3,5,10,7,4,9,2,8])
        self.assertEqual(2, res)

    def test_minSubArrayLen_three(self):
        solution = Solution()
        res = solution.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12])
        self.assertEqual(8, res)

    def test_minSubArrayLen_four(self):
        solution = Solution()
        res = solution.minSubArrayLen(3, [1,1])
        self.assertEqual(0, res)
