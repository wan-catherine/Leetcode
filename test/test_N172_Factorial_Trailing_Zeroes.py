from unittest import TestCase
from problems.N172_Factorial_Trailing_Zeroes import Solution

class TestSolution(TestCase):
    def test_trailing_zeroes(self):
        self.assertEqual(0, Solution().trailingZeroes(3))

    def test_trailing_zeroes_1(self):
        self.assertEqual(1, Solution().trailingZeroes(5))

    def test_trailing_zeroes_2(self):
        self.assertEqual(0, Solution().trailingZeroes(0))
