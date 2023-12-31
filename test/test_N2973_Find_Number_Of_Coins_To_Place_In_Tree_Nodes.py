from unittest import TestCase
from problems.N2973_Find_Number_Of_Coins_To_Place_In_Tree_Nodes import Solution

class TestSolution(TestCase):
    def test_placed_coins(self):
        self.assertListEqual([120,1,1,1,1,1], Solution().placedCoins(edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]))

    def test_placed_coins_1(self):
        self.assertListEqual([280,140,32,1,1,1,1,1,1], Solution().placedCoins(edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]))

    def test_placed_coins_2(self):
        self.assertListEqual([0,1,1], Solution().placedCoins(edges = [[0,1],[0,2]], cost = [1,2,-2]))
