from unittest import TestCase
from problems.BestTimeBuySellStockIII import Solution

class TestSolution(TestCase):
    def test_maxProfit(self):
        solution = Solution()
        res = solution.maxProfit([3,3,5,0,0,3,1,4])
        self.assertEqual(6, res)

    def test_maxProfit_one(self):
        solution = Solution()
        res = solution.maxProfit([1,2,3,4,5])
        self.assertEqual(4, res)

    def test_maxProfit_two(self):
        solution = Solution()
        res = solution.maxProfit([7,6,4,3,1])
        self.assertEqual(0, res)

    def test_maxProfit_2(self):
        res = Solution().maxProfit([1,2,4,2,5,7,2,4,9,0])
        self.assertEqual(13, res)

    def test_maxProfit_three(self):
        solution = Solution()
        res = solution.maxProfit([2,5,7,1,4,3,1,3])
        self.assertEqual(8, res)
