from unittest import TestCase
from problems.N375_Guess_Number_Higher_Or_Lower_II import Solution

class TestSolution(TestCase):
    def test_getMoneyAmount(self):
        self.assertEqual(16, Solution().getMoneyAmount(10))

    def test_getMoneyAmount_1(self):
        self.assertEqual(0, Solution().getMoneyAmount(1))

    def test_getMoneyAmount_2(self):
        self.assertEqual(1, Solution().getMoneyAmount(2))

