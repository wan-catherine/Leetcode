from unittest import TestCase
from problems.N3196_Maximize_Total_Cost_Of_Alternating_Subarrays import Solution

class TestSolution(TestCase):
    def test_maximum_total_cost(self):
        self.assertEquals(10, Solution().maximumTotalCost([1,-2,3,4]))

    def test_maximum_total_cost_1(self):
        self.assertEquals(4, Solution().maximumTotalCost([1,-1,1,-1]))

    def test_maximum_total_cost_2(self):
        self.assertEquals(0, Solution().maximumTotalCost([0]))

    def test_maximum_total_cost_3(self):
        self.assertEquals(2, Solution().maximumTotalCost([1,-1]))
