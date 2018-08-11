from unittest import TestCase
from problems.BestTimeToBuySellStock import Solution

class TestSolution(TestCase):
    def test_max_profit_with_decline_numbers(self):
        solution = Solution()
        res = solution.maxProfit([7,6,4,3,1])
        self.assertEquals(0, res)

    def test_max_profit_with_random_numbers(self):
        solution = Solution()
        res = solution.maxProfit([7,1,5,3,6,4])
        self.assertEquals(5, res)

    def test_max_profit_with_empty_number(self):
        solution = Solution()
        res = solution.maxProfit([])
        self.assertEquals(0, res)

    def test_max_profit_with_only_one_number(self):
        solution = Solution()
        res = solution.maxProfit([1])
        self.assertEquals(0, res)