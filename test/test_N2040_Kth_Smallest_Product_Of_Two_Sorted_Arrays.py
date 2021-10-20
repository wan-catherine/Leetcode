from unittest import TestCase
from problems.N2040_Kth_Smallest_Product_Of_Two_Sorted_Arrays import Solution

class TestSolution(TestCase):
    def test_kth_smallest_product(self):
        self.assertEqual(8, Solution().kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2))

    def test_kth_smallest_product_1(self):
        self.assertEqual(0, Solution().kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6))

    def test_kth_smallest_product_2(self):
        self.assertEqual(-6, Solution().kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3))

    def test_kth_smallest_product_3(self):
        self.assertEqual(-5, Solution().kthSmallestProduct(nums1 = [-5], nums2 = [1], k = 1))
