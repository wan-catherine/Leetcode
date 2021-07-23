from unittest import TestCase
from problems.N1927_Sum_Game import Solution

class TestSolution(TestCase):
    def test_sum_game(self):
        self.assertFalse(Solution().sumGame("5023"))

    def test_sum_game_1(self):
        self.assertTrue(Solution().sumGame("25??"))

    def test_sum_game_2(self):
        self.assertFalse(Solution().sumGame("?3295???"))

    def test_sum_game_3(self):
        self.assertTrue(Solution().sumGame("2582?9"))
