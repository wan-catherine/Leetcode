from unittest import TestCase
from problems.N2850_Minimum_Moves_To_Spread_Stones_Over_Grid import Solution

class TestSolution(TestCase):
    def test_minimum_moves(self):
        self.assertEqual(3, Solution().minimumMoves([[1,1,0],[1,1,1],[1,2,1]]))

    def test_minimum_moves_1(self):
        self.assertEqual(4, Solution().minimumMoves([[1,3,0],[1,0,0],[1,0,3]]))
