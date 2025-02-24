from unittest import TestCase
from problems.N3429_Paint_House_IV import Solution

class TestSolution(TestCase):
    def test_min_cost(self):
        self.assertEquals(9, Solution().minCost(n = 4, cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]))

    def test_min_cost_1(self):
        self.assertEquals(18, Solution().minCost(n = 6, cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]))
