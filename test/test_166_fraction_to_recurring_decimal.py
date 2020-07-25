from unittest import TestCase
from problems.N166_Fraction_To_Recurring_Decimal import Solution

class TestSolution(TestCase):
    def test_fractionToDecimal(self):
        self.assertEqual("0.5", Solution().fractionToDecimal(1, 2))

    def test_fractionToDecimal_1(self):
        self.assertEqual("2", Solution().fractionToDecimal(2, 1))

    def test_fractionToDecimal_2(self):
        self.assertEqual("0.(6)", Solution().fractionToDecimal(2, 3))

    def test_fractionToDecimal_3(self):
        self.assertEqual("-6.25", Solution().fractionToDecimal(-50, 8))
