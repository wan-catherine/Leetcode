from unittest import TestCase
from problems.N1489_Find_Critical_And_Pseudo_Critical_Edges_In_Minimum_Spanning_Tree import Solution

class TestSolution(TestCase):
    def test_findCriticalAndPseudoCriticalEdges(self):
        self.assertListEqual([[0,1],[2,3,4,5]], Solution().findCriticalAndPseudoCriticalEdges(n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))

    def test_findCriticalAndPseudoCriticalEdges_1(self):
        self.assertListEqual([[],[0,1,2,3]], Solution().findCriticalAndPseudoCriticalEdges(n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))
