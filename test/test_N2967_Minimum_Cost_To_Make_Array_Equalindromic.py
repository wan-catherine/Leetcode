from unittest import TestCase
from problems.N2967_Minimum_Cost_To_Make_Array_Equalindromic import Solution

class TestSolution(TestCase):
    def test_minimum_cost(self):
        self.assertEquals(6, Solution().minimumCost([1,2,3,4,5]))

    def test_minimum_cost_1(self):
        self.assertEquals(11, Solution().minimumCost([10,12,13,14,15]))

    def test_minimum_cost_2(self):
        self.assertEquals(22, Solution().minimumCost([22,33,22,33,22]))
