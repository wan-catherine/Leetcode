from unittest import TestCase
from problems.N2920_Maximum_Points_After_Collecting_Coins_From_All_Nodes import Solution

class TestSolution(TestCase):
    def test_maximum_points(self):
        self.assertEqual(11, Solution().maximumPoints(edges = [[0,1],[1,2],[2,3]], coins = [10,10,3,3], k = 5))

    def test_maximum_points_1(self):
        self.assertEqual(16, Solution().maximumPoints(edges = [[0,1],[0,2]], coins = [8,4,4], k = 0))
