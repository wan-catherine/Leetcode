from unittest import TestCase
from problems.N847_Shortest_Path_Visiting_All_Nodes import Solution

class TestSolution(TestCase):
    def test_shortest_path_length(self):
        self.assertEqual(4, Solution().shortestPathLength([[1,2,3],[0],[0],[0]]))

    def test_shortest_path_length_1(self):
        self.assertEqual(4, Solution().shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))
