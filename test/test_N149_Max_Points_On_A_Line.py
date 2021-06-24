from unittest import TestCase
from problems.N149_Max_Points_On_A_Line import Solution

class TestSolution(TestCase):
    def test_max_points(self):
        self.assertEqual(3, Solution().maxPoints(points = [[1,1],[2,2],[3,3]]))

    def test_max_points_1(self):
        self.assertEqual(4, Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))

    def test_max_points_2(self):
        self.assertEqual(5, Solution().maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]))


