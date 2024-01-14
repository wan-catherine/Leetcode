from unittest import TestCase
from problems.N2858_Minimum_Edge_Reversals_So_Every_Node_Is_Reachable import Solution

class TestSolution(TestCase):
    def test_min_edge_reversals(self):
        self.assertListEqual([1,1,0,2], Solution().minEdgeReversals(n = 4, edges = [[2,0],[2,1],[1,3]]))

    def test_min_edge_reversals_1(self):
        self.assertListEqual([2,0,1], Solution().minEdgeReversals(n = 3, edges = [[1,2],[2,0]]))
