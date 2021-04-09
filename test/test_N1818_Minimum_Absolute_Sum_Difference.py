from unittest import TestCase
from problems.N1818_Minimum_Absolute_Sum_Difference import Solution

class TestSolution(TestCase):
    def test_min_absolute_sum_diff(self):
        self.assertEqual(3, Solution().minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5]))

    def test_min_absolute_sum_diff_1(self):
        self.assertEqual(0, Solution().minAbsoluteSumDiff(nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]))

    def test_min_absolute_sum_diff_2(self):
        self.assertEqual(20, Solution().minAbsoluteSumDiff(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]))

    def test_min_absolute_sum_diff_3(self):
        self.assertEqual(9, Solution().minAbsoluteSumDiff([1,28,21], [9,21,20]))
