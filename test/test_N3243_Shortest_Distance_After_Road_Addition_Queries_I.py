from unittest import TestCase
from problems.N3243_Shortest_Distance_After_Road_Addition_Queries_I import Solution

class TestSolution(TestCase):
    def test_shortest_distance_after_queries(self):
        self.assertListEqual([3,2,1], Solution().shortestDistanceAfterQueries(n = 5, queries = [[2,4],[0,2],[0,4]]))

    def test_shortest_distance_after_queries_1(self):
        self.assertListEqual([1,1], Solution().shortestDistanceAfterQueries(n = 4, queries = [[0,3],[0,2]]))
