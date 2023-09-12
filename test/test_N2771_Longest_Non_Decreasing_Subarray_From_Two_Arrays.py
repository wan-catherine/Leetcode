from unittest import TestCase
from problems.N2771_Longest_Non_Decreasing_Subarray_From_Two_Arrays import Solution

class TestSolution(TestCase):
    def test_max_non_decreasing_length(self):
        self.assertEquals(2, Solution().maxNonDecreasingLength(nums1 = [2,3,1], nums2 = [1,2,1]))

    def test_max_non_decreasing_length_1(self):
        self.assertEquals(4, Solution().maxNonDecreasingLength(nums1 = [1,3,2,1], nums2 = [2,2,3,4]))

    def test_max_non_decreasing_length_2(self):
        self.assertEquals(2, Solution().maxNonDecreasingLength(nums1 = [1,1], nums2 = [2,2]))
