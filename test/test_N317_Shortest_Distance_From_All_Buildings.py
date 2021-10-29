from unittest import TestCase
from problems.N317_Shortest_Distance_From_All_Buildings import Solution

class TestSolution(TestCase):
    def test_shortest_distance(self):
        self.assertEqual(7, Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]))

    def test_shortest_distance_1(self):
        self.assertEqual(1, Solution().shortestDistance([[1,0]]))

    def test_shortest_distance_2(self):
        self.assertEqual(-1, Solution().shortestDistance([[1]]))
