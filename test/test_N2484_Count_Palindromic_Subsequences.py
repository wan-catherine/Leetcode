from unittest import TestCase
from problems.N2484_Count_Palindromic_Subsequences import Solution

class TestSolution(TestCase):
    def test_count_palindromes(self):
        self.assertEqual(2, Solution().countPalindromes("103301"))

    def test_count_palindromes_1(self):
        self.assertEqual(21, Solution().countPalindromes("0000000"))

    def test_count_palindromes_2(self):
        self.assertEqual(2, Solution().countPalindromes("9999900000"))
