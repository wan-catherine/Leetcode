from unittest import TestCase
from problems.N2962_Count_Subarrays_Where_Max_Element_Appears_At_Least_K_Times import Solution

class TestSolution(TestCase):
    def test_count_subarrays(self):
        self.assertEquals(6, Solution().countSubarrays(nums = [1,3,2,3,3], k = 2))

    def test_count_subarrays_1(self):
        self.assertEquals(0, Solution().countSubarrays(nums = [1,4,2,1], k = 3))
