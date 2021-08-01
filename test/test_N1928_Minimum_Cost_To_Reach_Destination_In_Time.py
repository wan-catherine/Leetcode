from unittest import TestCase
from problems.N1928_Minimum_Cost_To_Reach_Destination_In_Time import Solution

class TestSolution(TestCase):
    def test_min_cost(self):
        self.assertEqual(11, Solution().minCost(maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]))

    def test_min_cost_1(self):
        self.assertEqual(48, Solution().minCost(maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]))

    def test_min_cost_2(self):
        self.assertEqual(-1, Solution().minCost(maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]))

    def test_min_cost_3(self):
        self.assertEqual(7, Solution().minCost(100, [[0,1,100]], [2,5]))
