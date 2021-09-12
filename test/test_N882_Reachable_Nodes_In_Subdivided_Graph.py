from unittest import TestCase
from problems.N882_Reachable_Nodes_In_Subdivided_Graph import Solution

class TestSolution(TestCase):
    def test_reachable_nodes(self):
        self.assertEqual(13, Solution().reachableNodes(edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3))

    def test_reachable_nodes_1(self):
        self.assertEqual(23, Solution().reachableNodes(edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4))

    def test_reachable_nodes_2(self):
        self.assertEqual(1, Solution().reachableNodes(edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5))
