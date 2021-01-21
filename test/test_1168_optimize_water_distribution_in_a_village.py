from unittest import TestCase
from problems.N1168_Optimize_Water_Distribution_In_A_Village import Solution

class TestSolution(TestCase):
    def test_minCostToSupplyWater(self):
        self.assertEqual(3, Solution().minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]))

    def test_minCostToSupplyWater_1(self):
        self.assertEqual(131704, Solution().minCostToSupplyWater(5, [46012,72474,64965,751,33304], [[2,1,6719],[3,2,75312],[5,3,44918]]))
