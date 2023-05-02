from unittest import TestCase
from problems.N2662_Minimum_Cost_Of_A_Path_With_Special_Roads import Solution

class TestSolution(TestCase):
    def test_minimum_cost(self):
        self.assertEqual(5, Solution().minimumCost(start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]))

    def test_minimum_cost_1(self):
        self.assertEqual(7, Solution().minimumCost(start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]))


