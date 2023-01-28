from unittest import TestCase
from problems.N2499_Minimum_Total_Cost_To_Make_Arrays_Unequal import Solution

class TestSolution(TestCase):
    def test_minimum_total_cost(self):
        self.assertEqual(10, Solution().minimumTotalCost(nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]))

    def test_minimum_total_cost_1(self):
        self.assertEqual(10, Solution().minimumTotalCost(nums1 = [2,2,2,1,3], nums2 = [1,2,2,3,3]))

    def test_minimum_total_cost_2(self):
        self.assertEqual(-1, Solution().minimumTotalCost(nums1 = [1,2,2], nums2 = [1,2,2]))
