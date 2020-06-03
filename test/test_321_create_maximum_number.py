from unittest import TestCase
from problems.N321_Create_Maximum_Number import Solution

class TestSolution(TestCase):
    def test_maxNumber(self):
        nums1 = [3, 4, 6, 5]
        nums2 = [9, 1, 2, 5, 8, 3]
        k = 5
        self.assertListEqual([9, 8, 6, 5, 3], Solution().maxNumber(nums1,nums2, k))

    def test_maxNumber_1(self):
        nums1 = [6, 7]
        nums2 = [6, 0, 4]
        k = 5
        self.assertListEqual([6, 7, 6, 0, 4], Solution().maxNumber(nums1,nums2, k))

    def test_maxNumber_2(self):
        nums1 = [3, 9]
        nums2 = [8, 9]
        k = 3
        self.assertListEqual([9, 8, 9], Solution().maxNumber(nums1,nums2, k))

    def test_maxNumber_3(self):
        nums1 = [8, 6, 9]
        nums2 = [1, 7, 5]
        k = 3
        self.assertListEqual([9, 7, 5], Solution().maxNumber(nums1,nums2, k))

