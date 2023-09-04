from unittest import TestCase
from problems.N2846_Minimum_Edge_Weight_Equilibrium_Queries_In_A_Tree import Solution

class TestSolution(TestCase):
    def test_min_operations_queries(self):
        self.assertListEqual([0,0,1,3], Solution().minOperationsQueries(n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]))

    def test_min_operations_queries_1(self):
        self.assertListEqual([1,2,2,3], Solution().minOperationsQueries(n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]))
