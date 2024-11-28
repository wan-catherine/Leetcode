from unittest import TestCase
from problems.N2290_Minimum_Obstacle_Removal_To_Reach_Corner import Solution

class TestSolution(TestCase):
    def test_minimum_obstacles(self):
        self.assertEquals(2, Solution().minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))

    def test_minimum_obstacles_1(self):
        self.assertEquals(0, Solution().minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))
