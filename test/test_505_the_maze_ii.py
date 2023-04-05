from unittest import TestCase
from problems.N505_The_Maze_II import Solution

class TestSolution(TestCase):
    def test_shortestDistance(self):
        self.assertEqual(12, Solution().shortestDistance([[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]], (0, 4), (4, 4)))

    def test_shortestDistance_1(self):
        self.assertEqual(-1, Solution().shortestDistance([[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]], (0, 4), (3, 2)))
