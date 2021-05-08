from unittest import TestCase
from problems.N906_Super_Palindromes import Solution

class TestSolution(TestCase):
    def test_superpalindromes_in_range(self):
        self.assertEqual(4, Solution().superpalindromesInRange(left = "4", right = "1000"))

    def test_superpalindromes_in_range_1(self):
        self.assertEqual(1, Solution().superpalindromesInRange(left = "1", right = "2"))
