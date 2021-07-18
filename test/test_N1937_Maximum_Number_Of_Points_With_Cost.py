from unittest import TestCase
from problems.N1937_Maximum_Number_Of_Points_With_Cost import Solution

class TestSolution(TestCase):
    def test_max_points(self):
        self.assertEqual(9, Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]]))

    def test_max_points_1(self):
        self.assertEqual(11, Solution().maxPoints([[1,5],[2,3],[4,2]]))
