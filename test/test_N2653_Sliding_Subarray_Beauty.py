from unittest import TestCase
from problems.N2653_Sliding_Subarray_Beauty import Solution

class TestSolution(TestCase):
    def test_get_subarray_beauty(self):
        self.assertListEqual([-1,-2,-2], Solution().getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2))

    def test_get_subarray_beauty_1(self):
        self.assertListEqual([-1,-2,-3,-4], Solution().getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2))

    def test_get_subarray_beauty_2(self):
        self.assertListEqual([-3,0,-3,-3,-3], Solution().getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1))

    def test_get_subarray_beauty_3(self):
        self.assertListEqual([-34], Solution().getSubarrayBeauty(nums = [-46,-34,-46], k = 3, x = 3))

    def test_get_subarray_beauty_4(self):
        self.assertListEqual([-26,0,0,0,0], Solution().getSubarrayBeauty(nums = [-37,-26,-38,-26,-27,32,42,3,-42], k = 5, x = 5))