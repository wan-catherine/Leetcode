from unittest import TestCase
from problems.N713_Subarray_Product_Less_Than_K import Solution

class TestSolution(TestCase):
    def test_numSubarrayProductLessThanK(self):
        nums = [10, 5, 2, 6]
        k = 100
        self.assertEqual(8, Solution().numSubarrayProductLessThanK(nums, k))

    def test_numSubarrayProductLessThanK_1(self):
        nums = [10,5,10]
        k = 10
        self.assertEqual(1, Solution().numSubarrayProductLessThanK(nums, k))

    def test_numSubarrayProductLessThanK_2(self):
        nums = [1,2,3]
        k = 0
        self.assertEqual(0, Solution().numSubarrayProductLessThanK(nums, k))

