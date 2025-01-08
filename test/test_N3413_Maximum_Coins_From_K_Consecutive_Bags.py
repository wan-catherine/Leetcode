from unittest import TestCase
from problems.N3413_Maximum_Coins_From_K_Consecutive_Bags import Solution

class TestSolution(TestCase):
    def test_maximum_coins(self):
        self.assertEquals(10, Solution().maximumCoins(coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4))

    def test_maximum_coins_1(self):
        self.assertEquals(6, Solution().maximumCoins(coins = [[1,10,3]], k = 2))

    def test_maximum_coins_2(self):
        self.assertEquals(226, Solution().maximumCoins(coins = [[8,12,13],[29,32,2],[13,15,2],[40,41,18],[42,48,18],[33,36,11],[37,38,6]], k = 28))
