from unittest import TestCase
from problems.N2017_Grid_Game import Solution

class TestSolution(TestCase):
    def test_grid_game(self):
        self.assertEqual(4, Solution().gridGame([[2,5,4],[1,5,1]]))

    def test_grid_game_1(self):
        self.assertEqual(4, Solution().gridGame([[3,3,1],[8,5,2]]))

    def test_grid_game_2(self):
        self.assertEqual(7, Solution().gridGame([[1,3,1,15],[1,3,3,1]]))
