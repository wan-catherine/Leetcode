from unittest import TestCase
from problems.N2831_Find_The_Longest_Equal_Subarray import Solution

class TestSolution(TestCase):
    def test_longest_equal_subarray(self):
        self.assertEquals(3, Solution().longestEqualSubarray(nums = [1,3,2,3,1,3], k = 3))

    def test_longest_equal_subarray_1(self):
        self.assertEquals(4, Solution().longestEqualSubarray(nums = [1,1,2,2,1,1], k = 2))

    def test_longest_equal_subarray_2(self):
        self.assertEquals(1, Solution().longestEqualSubarray(nums = [1,2,1], k = 0))
