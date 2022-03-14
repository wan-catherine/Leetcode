from unittest import TestCase
from problems.N2203_Minimum_Weighted_Subgraph_With_The_Required_Paths import Solution

class TestSolution(TestCase):
    def test_minimum_weight(self):
        self.assertEqual(9, Solution().minimumWeight(n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5))

    def test_minimum_weight_1(self):
        self.assertEqual(-1, Solution().minimumWeight(n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2))

