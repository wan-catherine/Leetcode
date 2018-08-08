from unittest import TestCase
from problems.MedianOfTwoSortedArrays import Solution

class TestSolution(TestCase):
    def test_find_median_sorted_arrays_simple(self):
        nums1 = [1, 3]
        nums2 = [2]
        solution = Solution()
        res = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(res, 2.0)

    def test_find_median_sorted_arrays_two_same_long_list(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        solution = Solution()
        res = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(res, 2.5)

    def test_find_median_sorted_arrays_two_mix_same_long_list(self):
        nums1 = [1, 2, 8, 9]
        nums2 = [0,1,3, 4, 9, 10]
        solution = Solution()
        res = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(res, 3.5)

    def test_find_median_sorted_arrays_two_after_same_long_list(self):
        nums1 = [ 8, 9]
        nums2 = [0,1]
        solution = Solution()
        res = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(res, 4.5)

    def test_find_median_sorted_arrays_one_empty_list(self):
        nums1 = [1]
        nums2 = []
        solution = Solution()
        res = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEquals(res, 1)