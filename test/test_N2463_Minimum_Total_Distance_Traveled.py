from unittest import TestCase
from problems.N2463_Minimum_Total_Distance_Traveled import Solution

class TestSolution(TestCase):
    def test_minimum_total_distance(self):
        self.assertEqual(4, Solution().minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]]))

    def test_minimum_total_distance_1(self):
        self.assertEqual(2, Solution().minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]]))
