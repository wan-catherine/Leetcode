from unittest import TestCase
from problems.N1976_Number_Of_Ways_To_Arrive_At_Destination import Solution

class TestSolution(TestCase):
    def test_count_paths(self):
        self.assertEqual(4, Solution().countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))

    def test_count_paths_1(self):
        self.assertEqual(1, Solution().countPaths(n = 2, roads = [[1,0,10]]))

    def test_count_paths_2(self):
        self.assertEqual(2, Solution().countPaths(5,[[0,1,1],[1,2,4],[0,4,3],[3,2,5],[3,4,1],[3,0,5],[1,3,1]]))