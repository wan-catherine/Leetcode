from unittest import TestCase
from problems.N2867_Count_Valid_Paths_In_A_Tree import Solution

class TestSolution(TestCase):
    def test_count_paths(self):
        self.assertEquals(4, Solution().countPaths(n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]))

    def test_count_paths_1(self):
        self.assertEquals(6, Solution().countPaths(n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]))

    def test_count_paths_2(self):
        self.assertEquals(4, Solution().countPaths(n = 4, edges = [[1,2],[4,1],[3,4]]))
