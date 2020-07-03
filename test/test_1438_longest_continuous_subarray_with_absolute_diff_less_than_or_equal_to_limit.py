from unittest import TestCase
from problems.N1438_Longest_Continuous_Subarray_With_Absolute_Diff_Less_Than_Or_Equal_To_Limit import Solution

class TestSolution(TestCase):
    def test_longestSubarray(self):
        nums = [8, 2, 4, 7]
        limit = 4
        self.assertEqual(2, Solution().longestSubarray(nums, limit))

    def test_longestSubarray_1(self):
        nums = [10,1,2,4,7,2]
        limit = 5
        self.assertEqual(4, Solution().longestSubarray(nums, limit))

    def test_longestSubarray_2(self):
        nums = [4,2,2,2,4,4,2,2]
        limit = 0
        self.assertEqual(3, Solution().longestSubarray(nums, limit))
