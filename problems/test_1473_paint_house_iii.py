from unittest import TestCase
from problems.N1473_Paint_House_III import Solution

class TestSolution(TestCase):
    def test_minCost(self):
        self.assertEqual(9, Solution().minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))

    def test_minCost_1(self):
        self.assertEqual(11, Solution().minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))

    def test_minCost_2(self):
        self.assertEqual(5, Solution().minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5))

    def test_minCost_3(self):
        self.assertEqual(-1, Solution().minCost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3))
