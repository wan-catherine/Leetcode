from unittest import TestCase
from problems.N1577_Number_Of_Ways_Where_Square_Of_Number_Is_Equal_To_Product_Of_Two_Numbers import Solution

class TestSolution(TestCase):
    def test_numTriplets(self):
        self.assertEqual(1, Solution().numTriplets(nums1 = [7,4], nums2 = [5,2,8,9]))

    def test_numTriplets_1(self):
        self.assertEqual(9, Solution().numTriplets(nums1 = [1,1], nums2 = [1,1,1]))

    def test_numTriplets_2(self):
        self.assertEqual(2, Solution().numTriplets(nums1 = [7,7,8,3], nums2 = [1,2,9,7]))

    def test_numTriplets_3(self):
        self.assertEqual(0, Solution().numTriplets(nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]))
