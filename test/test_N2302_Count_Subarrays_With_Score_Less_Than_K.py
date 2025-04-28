from unittest import TestCase
from problems.N2302_Count_Subarrays_With_Score_Less_Than_K import Solution

class TestSolution(TestCase):
    def test_count_subarrays(self):
        self.assertEquals(6, Solution().countSubarrays(nums = [2,1,4,3,5], k = 10))

    def test_count_subarrays_1(self):
        self.assertEquals(5, Solution().countSubarrays(nums = [1,1,1], k = 5))
