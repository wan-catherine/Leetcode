from unittest import TestCase
from problems.N1879_Minimum_XOR_Sum_Of_Two_Arrays import Solution

class TestSolution(TestCase):
    def test_minimum_xorsum(self):
        self.assertIs(2, Solution().minimumXORSum(nums1 = [1,2], nums2 = [2,3]))

    def test_minimum_xorsum_1(self):
        self.assertIs(8, Solution().minimumXORSum(nums1 = [1,0,3], nums2 = [5,3,4]))
