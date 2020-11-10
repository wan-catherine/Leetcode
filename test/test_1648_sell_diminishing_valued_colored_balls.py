from unittest import TestCase
from problems.N1648_Sell_Diminishing_Valued_Colored_Balls import Solution

class TestSolution(TestCase):
    def test_maxProfit(self):
        self.assertEqual(14, Solution().maxProfit(inventory = [2,5], orders = 4))

    def test_maxProfit_1(self):
        self.assertEqual(19, Solution().maxProfit(inventory = [3,5], orders = 6))

    def test_maxProfit_2(self):
        self.assertEqual(110, Solution().maxProfit(inventory = [2,8,4,10,6], orders = 20))

    def test_maxProfit_3(self):
        self.assertEqual(21, Solution().maxProfit(inventory = [1000000000], orders = 1000000000))

    def test_maxProfit_4(self):
        self.assertEqual(373219333, Solution().maxProfit([497978859,167261111,483575207,591815159], 836556809))
