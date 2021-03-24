from unittest import TestCase
from problems.N730_Count_Different_Palindromic_Subsequences import Solution

class TestSolution(TestCase):
    def test_count_palindromic_subsequences(self):
        self.assertEqual(6, Solution().countPalindromicSubsequences('bccb'))

    def test_count_palindromic_subsequences_1(self):
        self.assertEqual(104860361, Solution().countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
