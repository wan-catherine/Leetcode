from unittest import TestCase
from problems.N115_Distinct_Subsequences import Solution

class TestSolution(TestCase):
    def test_numDistinct(self):
        self.assertEqual(3, Solution().numDistinct(s = "rabbbit", t = "rabbit"))

    def test_numDistinct_1(self):
        self.assertEqual(5, Solution().numDistinct(s = "babgbag", t = "bag"))
