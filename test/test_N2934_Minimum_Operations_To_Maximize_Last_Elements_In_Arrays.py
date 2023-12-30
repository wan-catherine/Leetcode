from unittest import TestCase
from problems.N2934_Minimum_Operations_To_Maximize_Last_Elements_In_Arrays import Solution

class TestSolution(TestCase):
    def test_min_operations(self):
        self.assertEquals(1, Solution().minOperations(nums1 = [1,2,7], nums2 = [4,5,3]))

    def test_min_operations_1(self):
        self.assertEquals(2, Solution().minOperations(nums1 = [2,3,4,5,9], nums2 = [8,8,4,4,4]))

    def test_min_operations_2(self):
        self.assertEquals(-1, Solution().minOperations(nums1 = [1,5,4], nums2 = [2,5,3]))
