from unittest import TestCase
from problems.N1557_Minimum_Number_Of_Vertices_To_Reach_All_Nodes import Solution

class TestSolution(TestCase):
    def test_findSmallestSetOfVertices(self):
        n = 6
        edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
        self.assertListEqual([0,3], Solution().findSmallestSetOfVertices(n, edges))

    def test_findSmallestSetOfVertices_1(self):
        n = 5
        edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
        self.assertListEqual([0,2,3], Solution().findSmallestSetOfVertices(n, edges))
