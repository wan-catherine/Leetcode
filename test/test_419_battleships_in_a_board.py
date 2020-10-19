from unittest import TestCase
from problems.N419_Battleships_In_A_Board import Solution

class TestSolution(TestCase):
    def test_countBattleships(self):
        input = [['X', '.', '.', 'X'], ['.','.','.','X'], ['.','.','.','X']]
        self.assertEqual(2, Solution().countBattleships(input))


