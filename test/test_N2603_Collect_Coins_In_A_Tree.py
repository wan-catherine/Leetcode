from unittest import TestCase
from problems.N2603_Collect_Coins_In_A_Tree import Solution

class TestSolution(TestCase):
    def test_collect_the_coins(self):
        self.assertEqual(2, Solution().collectTheCoins(coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]))

    def test_collect_the_coins_1(self):
        self.assertEqual(2, Solution().collectTheCoins(coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]))
