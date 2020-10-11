from unittest import TestCase
from problems.N1310_XOR_Queries_Of_A_Subarray import Solution

class TestSolution(TestCase):
    def test_xorQueries(self):
        self.assertListEqual([2,7,14,8], Solution().xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))

    def test_xorQueries_1(self):
        self.assertListEqual([8,0,4,4], Solution().xorQueries(arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]))