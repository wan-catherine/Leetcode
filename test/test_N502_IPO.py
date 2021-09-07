from unittest import TestCase
from problems.N502_IPO import Solution

class TestSolution(TestCase):
    def test_find_maximized_capital(self):
        self.assertEqual(4, Solution().findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))

    def test_find_maximized_capital_1(self):
        self.assertEqual(6, Solution().findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))
