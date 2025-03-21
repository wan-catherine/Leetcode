from unittest import TestCase
from problems.N3108_Minimum_Cost_Walk_In_Weighted_Graph import Solution

class TestSolution(TestCase):
    def test_minimum_cost(self):
        self.assertListEqual([1,-1], Solution().minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))

    def test_minimum_cost_1(self):
        self.assertListEqual([0], Solution().minimumCost(n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]))

    def test_minimum_cost_2(self):
        self.assertListEqual([0, -1, 0], Solution().minimumCost(n = 10, edges = [[7,0,11],[6,3,8],[6,1,3],[7,3,0],[2,3,9],[8,9,12],[0,6,3],[0,2,4]], query = [[7,0],[4,2],[6,2]]))
