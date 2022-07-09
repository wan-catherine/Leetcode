from unittest import TestCase
from problems.N2333_Minimum_Sum_Of_Squared_Difference import Solution

class TestSolution(TestCase):
    def test_min_sum_square_diff(self):
        self.assertEqual(579, Solution().minSumSquareDiff(nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0))

    def test_min_sum_square_diff_1(self):
        self.assertEqual(43, Solution().minSumSquareDiff(nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1))
