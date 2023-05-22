from unittest import TestCase
from problems.N2608_Shortest_Cycle_In_A_Graph import Solution

class TestSolution(TestCase):
    def test_find_shortest_cycle(self):
        self.assertEqual(3, Solution().findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))

    def test_find_shortest_cycle_1(self):
        self.assertEqual(-1, Solution().findShortestCycle(n = 4, edges = [[0,1],[0,2]]))