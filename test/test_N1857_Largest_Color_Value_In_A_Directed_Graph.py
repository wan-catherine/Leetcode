from unittest import TestCase
from problems.N1857_Largest_Color_Value_In_A_Directed_Graph import Solution

class TestSolution(TestCase):
    def test_largest_path_value(self):
        self.assertEqual(3, Solution().largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]))

    def test_largest_path_value_1(self):
        self.assertEqual(-1, Solution().largestPathValue(colors = "a", edges = [[0,0]]))

    def test_largest_path_value_2(self):
        self.assertEqual(5, Solution().largestPathValue("nnllnzznn", [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]))

    def test_largest_path_value_3(self):
        self.assertEqual(3, Solution().largestPathValue("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]))

    def test_largest_path_value_4(self):
        self.assertEqual(1, Solution().largestPathValue("g", []))