from unittest import TestCase
from problems.N879_Profitable_Schemes import Solution

class TestSolution(TestCase):
    def test_profitable_schemes(self):
        self.assertEqual(2, Solution().profitableSchemes(n = 5, minProfit = 3, group = [2,2], profit = [2,3]))

    def test_profitable_schemes_1(self):
        self.assertEqual(7, Solution().profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]))
