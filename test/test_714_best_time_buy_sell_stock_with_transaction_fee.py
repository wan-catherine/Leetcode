from unittest import TestCase
from problems.N714_Best_Time_Buy_Sell_Stock_With_Tracsaction_Fee import Solution

class TestSolution(TestCase):
    def test_maxProfit(self):
        res = Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
        self.assertEqual(8, res)
