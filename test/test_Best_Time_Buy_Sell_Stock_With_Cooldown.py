from unittest import TestCase
from problems.BestTimeBuySellStockWithCooldown import Solution

class TestSolution(TestCase):
    def test_maxProfit(self):
        solution = Solution()
        res = solution.maxProfit([1,2,3,0,2])
        self.assertEqual(res, 3)
