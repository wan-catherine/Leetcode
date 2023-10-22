from unittest import TestCase
from problems.N2902_Count_Of_Sub_Multisets_With_Bounded_Sum import Solution

class TestSolution(TestCase):
    def test_count_sub_multtisets(self):
        self.assertEquals(1, Solution().countSubMulttisets(nums = [1,2,2,3], l = 6, r = 6))

    def test_count_sub_multtisets_1(self):
        self.assertEquals(7, Solution().countSubMulttisets(nums = [2,1,4,2,7], l = 1, r = 5))

    def test_count_sub_multtisets_2(self):
        self.assertEquals(9, Solution().countSubMulttisets(nums = [1,2,1,3,5,2], l = 3, r = 5))
