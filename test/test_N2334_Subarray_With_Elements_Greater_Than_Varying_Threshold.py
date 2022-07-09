from unittest import TestCase
from problems.N2334_Subarray_With_Elements_Greater_Than_Varying_Threshold import Solution

class TestSolution(TestCase):
    def test_valid_subarray_size(self):
        self.assertEqual(3, Solution().validSubarraySize(nums = [1,3,4,3,1], threshold = 6))

    def test_valid_subarray_size_1(self):
        self.assertEqual(1, Solution().validSubarraySize([1000000000], 1))
