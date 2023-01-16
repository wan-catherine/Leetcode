from unittest import TestCase
from problems.N2536_Increment_Submatrices_By_One import Solution

class TestSolution(TestCase):
    def test_range_add_queries(self):
        self.assertListEqual([[1,1,0],[1,2,1],[0,1,1]], Solution().rangeAddQueries(n = 3, queries = [[1,1,2,2],[0,0,1,1]]))

    def test_range_add_queries_1(self):
        self.assertListEqual([[1,1],[1,1]], Solution().rangeAddQueries(n = 2, queries = [[0,0,1,1]]))
