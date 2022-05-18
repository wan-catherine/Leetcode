from unittest import TestCase
from problems.N2272_Substring_With_Largest_Variance import Solution

class TestSolution(TestCase):
    def test_largest_variance(self):
        self.assertEqual(3, Solution().largestVariance("aababbb"))

    def test_largest_variance_1(self):
        self.assertEqual(0, Solution().largestVariance("abcde"))