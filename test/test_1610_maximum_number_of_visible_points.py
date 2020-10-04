from unittest import TestCase
from problems.N1610_Maximum_Number_Of_Visible_Points import Solution

class TestSolution(TestCase):
    def test_visiblePoints(self):
        self.assertEqual(3, Solution().visiblePoints(points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]))

    def test_visiblePoints_1(self):
        self.assertEqual(4, Solution().visiblePoints(points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]))

    def test_visiblePoints_2(self):
        self.assertEqual(1, Solution().visiblePoints(points = [[1,0],[2,1]], angle = 13, location = [1,1]))
