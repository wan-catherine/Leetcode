from unittest import TestCase
from problems.N1293_Shortest_Path_In_A_Grid_With_Obstacles_Elimination import Solution

class TestSolution(TestCase):
    def test_shortest_path(self):
        self.assertEqual(6, Solution().shortestPath(grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1))

    def test_shortest_path_1(self):
        self.assertEqual(-1, Solution().shortestPath(grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1))
