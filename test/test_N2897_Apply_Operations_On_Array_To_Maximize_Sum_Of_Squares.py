from unittest import TestCase
from problems.N2897_Apply_Operations_On_Array_To_Maximize_Sum_Of_Squares import Solution

class TestSolution(TestCase):
    def test_max_sum(self):
        self.assertEquals(261, Solution().maxSum(nums = [2,6,5,8], k = 2))

    def test_max_sum_1(self):
        self.assertEquals(90, Solution().maxSum(nums = [4,5,4,7], k = 3))
