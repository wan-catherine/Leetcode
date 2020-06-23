from unittest import TestCase
from problems.N695_Max_Area_Of_Island import Solution

class TestSolution(TestCase):
    def test_maxAreaOfIsland(self):
        grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        self.assertEqual(6, Solution().maxAreaOfIsland(grid))

    def test_maxAreaOfIsland_1(self):
        grid = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(0, Solution().maxAreaOfIsland(grid))
