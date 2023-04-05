from unittest import TestCase
from problems.N2488_Count_Subarrays_With_Median_K import Solution

class TestSolution(TestCase):
    def test_count_subarrays(self):
        self.assertEqual(3, Solution().countSubarrays(nums = [3,2,1,4,5], k = 4))

    def test_count_subarrays_1(self):
        self.assertEqual(1, Solution().countSubarrays(nums = [2,3,1], k = 3))

    def test_count_subarrays_2(self):
        self.assertEqual(3, Solution().countSubarrays([4,1,3,2], 1))