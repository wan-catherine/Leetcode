from unittest import TestCase
from problems.N2029_Stone_Game_IX import Solution

class TestSolution(TestCase):
    def test_stone_game_ix(self):
        self.assertTrue(Solution().stoneGameIX([2,1]))

    def test_stone_game_ix_1(self):
        self.assertFalse(Solution().stoneGameIX([2]))

    def test_stone_game_ix_2(self):
        self.assertFalse(Solution().stoneGameIX([5,1,2,4,3]))
