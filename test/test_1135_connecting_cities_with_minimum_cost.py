from unittest import TestCase
from problems.N1135_Connecting_Cities_With_Minimum_Cost import Solution

class TestSolution(TestCase):
    def test_minimumCost(self):
        self.assertEqual(6, Solution().minimumCost(N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]))

    def test_minimumCost_1(self):
        self.assertEqual(-1, Solution().minimumCost(N = 4, connections = [[1,2,3],[3,4,4]]))

    def test_minimumCost_2(self):
        self.assertEqual(248074, Solution().minimumCost(7, [[2,1,87129],[3,1,14707],[4,2,34505],[5,1,71766],[6,5,2615],[7,2,37352]]))
