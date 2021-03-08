from unittest import TestCase
from problems.N1786_Number_Of_Restricted_Paths_From_First_To_Last_Node import Solution

class TestSolution(TestCase):
    def test_count_restricted_paths(self):
        self.assertEqual(3, Solution().countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))

    def test_count_restricted_paths_1(self):
        self.assertEqual(1, Solution().countRestrictedPaths(n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))

