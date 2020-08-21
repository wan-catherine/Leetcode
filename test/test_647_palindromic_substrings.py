from unittest import TestCase
from problems.N647_Palindromic_Substrings import Solution

class TestSolution(TestCase):
    def test_countSubstrings(self):
        self.assertEqual(3, Solution().countSubstrings("abc"))

    def test_countSubstrings_1(self):
        self.assertEqual(6, Solution().countSubstrings("aaa"))

    def test_countSubstrings_2(self):
        self.assertEqual(9, Solution().countSubstrings("leetcode"))