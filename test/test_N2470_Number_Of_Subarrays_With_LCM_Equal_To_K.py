from unittest import TestCase
from problems.N2470_Number_Of_Subarrays_With_LCM_Equal_To_K import Solution

class TestSolution(TestCase):
    def test_subarray_lcm(self):
        self.assertEqual(1, Solution().subarrayLCM([2,3], 6))

    def test_subarray_lcm_1(self):
        self.assertEqual(4, Solution().subarrayLCM(nums = [3,6,2,7,1], k = 6))

    def test_subarray_lcm_2(self):
        self.assertEqual(0, Solution().subarrayLCM(nums = [3], k = 2))
