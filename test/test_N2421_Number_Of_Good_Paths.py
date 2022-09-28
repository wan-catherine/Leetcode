from unittest import TestCase
from problems.N2421_Number_Of_Good_Paths import Solution

class TestSolution(TestCase):
    def test_number_of_good_paths(self):
        self.assertEqual(6, Solution().numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))

    def test_number_of_good_paths_1(self):
        self.assertEqual(7, Solution().numberOfGoodPaths(vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]))

    def test_number_of_good_paths_2(self):
        self.assertEqual(1, Solution().numberOfGoodPaths(vals = [1], edges = []))
