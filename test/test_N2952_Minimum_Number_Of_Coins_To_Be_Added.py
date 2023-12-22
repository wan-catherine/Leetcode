from unittest import TestCase
from problems.N2952_Minimum_Number_Of_Coins_To_Be_Added import Solution

class TestSolution(TestCase):
    def test_minimum_added_coins(self):
        self.assertEquals(2, Solution().minimumAddedCoins(coins = [1,4,10], target = 19))

    def test_minimum_added_coins_1(self):
        self.assertEquals(1, Solution().minimumAddedCoins(coins = [1,4,10,5,7,19], target = 19))

    def test_minimum_added_coins_2(self):
        self.assertEquals(3, Solution().minimumAddedCoins(coins = [1,1,1], target = 20))
