from unittest import TestCase
from problems.N1872_Stone_Game_VIII import Solution

class TestSolution(TestCase):
    def test_stone_game_viii(self):
        self.assertEqual(5, Solution().stoneGameVIII([-1,2,-3,4,-5]))

    def test_stone_game_viii_1(self):
        self.assertEqual(13, Solution().stoneGameVIII(stones = [7,-6,5,10,5,-2,-6]))

    def test_stone_game_viii_2(self):
        self.assertEqual(-22, Solution().stoneGameVIII([-10,-12]))
