from unittest import TestCase
from problems.N1036_Escape_A_Large_Maze import Solution

class TestSolution(TestCase):
    def test_is_escape_possible(self):
        self.assertFalse(Solution().isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]))
