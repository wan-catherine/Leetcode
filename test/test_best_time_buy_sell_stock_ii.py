from unittest import TestCase
from problems.BestTimeToBuySellStockII import Solution

class TestSolution(TestCase):
    def test_maxProfit(self):
        solution = Solution()
        res = solution.maxProfit([7,1,5,3,6,4])
        self.assertEqual(7, res)

    def test_maxProfit_one(self):
        solution = Solution()
        res = solution.maxProfit([1,2,3,4,5])
        self.assertEqual(4, res)

    def test_maxProfit_two(self):
        solution = Solution()
        res = solution.maxProfit([7,6,4,3,1])
        self.assertEqual(0, res)

    def test_maxProfit_three(self):
        solution = Solution()
        res = solution.maxProfit([8,6,4,3,3,2,3,5,8,3,8,2,6])
        self.assertEqual(15, res)

    def test_maxProfit_four(self):
        solution = Solution()
        res = solution.maxProfit([1,9,6,9,1,7,1,1,5,9,9,9])
        self.assertEqual(25, res)