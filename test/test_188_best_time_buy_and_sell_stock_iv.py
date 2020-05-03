from unittest import TestCase
from problems.N188_Best_Time_Buy_Sell_Stock_IV import Solution

class TestSolution(TestCase):
    def test_maxProfit(self):
        res = Solution().maxProfit(2, [2,4,1])
        self.assertEqual(2, res)

    def test_maxProfit_1(self):
        res = Solution().maxProfit(2, [3,2,6,5,0,3])
        self.assertEqual(7, res)

    def test_maxProfit_2(self):
        res = Solution().maxProfit(2, [1,2,4,2,5,7,2,4,9,0])
        self.assertEqual(13, res)

