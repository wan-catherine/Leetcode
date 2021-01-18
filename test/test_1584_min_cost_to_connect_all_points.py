from unittest import TestCase
from problems.N1584_Min_Cost_To_Connect_All_Points import Solution

class TestSolution(TestCase):
    def test_minCostConnectPoints(self):
        self.assertEqual(20, Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))

    def test_minCostConnectPoints_1(self):
        self.assertEqual(18, Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))

    def test_minCostConnectPoints_2(self):
        self.assertEqual(4, Solution().minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))

    def test_minCostConnectPoints_3(self):
        self.assertEqual(4000000, Solution().minCostConnectPoints([[-1000000,-1000000],[1000000,1000000]]))

    def test_minCostConnectPoints_4(self):
        self.assertEqual(0, Solution().minCostConnectPoints([[0,0]]))

    def test_minCostConnectPoints_5(self):
        self.assertEqual(143, Solution().minCostConnectPoints([[5,8],[18,-6],[-18,13],[-8,-13],[-13,3],[-15,2],[-12,17],[14,16],[-4,3],[-17,-7],[8,9],[17,14],[-13,2],[-3,-1],[4,-20]]))
