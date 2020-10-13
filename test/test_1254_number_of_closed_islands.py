from unittest import TestCase
from problems.N1254_Number_Of_Closed_Islands import Solution

class TestSolution(TestCase):
    def test_closedIsland(self):
        self.assertEqual(2, Solution().closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))

    def test_closedIsland_1(self):
        self.assertEqual(1, Solution().closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))

    def test_closedIsland_2(self):
        grid = [[1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1]]
        self.assertEqual(2, Solution().closedIsland(grid))
