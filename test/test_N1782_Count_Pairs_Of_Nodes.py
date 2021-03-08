from unittest import TestCase
from problems.N1782_Count_Pairs_Of_Nodes import Solution

class TestSolution(TestCase):
    def test_count_pairs(self):
        self.assertListEqual([6,5], Solution().countPairs(n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]))

    def test_count_pairs_1(self):
        self.assertListEqual([10,10,9,8,6],
                             Solution().countPairs(n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]))

    def test_count_pairs_2(self):
        self.assertListEqual([10,10,9,8,6], Solution().countPairs(5, [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], [1,2,3,4,5]))