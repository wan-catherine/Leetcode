from unittest import TestCase
from problems.N1510_Stone_Game_IV import Solution

class TestSolution(TestCase):
    def test_winnerSquareGame(self):
        self.assertTrue(Solution().winnerSquareGame(1))

    def test_winnerSquareGame_1(self):
        self.assertTrue(Solution().winnerSquareGame(4))

    def test_winnerSquareGame_2(self):
        self.assertFalse(Solution().winnerSquareGame(2))

    def test_winnerSquareGame_3(self):
        self.assertFalse(Solution().winnerSquareGame(7))

    def test_winnerSquareGame_4(self):
        self.assertFalse(Solution().winnerSquareGame(17))

    def test_winnerSquareGame_5(self):
        self.assertTrue(Solution().winnerSquareGame(8))