from unittest import TestCase
from problems.N516_Longest_Palindromic_Subsequence import Solution

class TestSolution(TestCase):
    def test_longestPalindromeSubseq(self):
        self.assertEqual(4, Solution().longestPalindromeSubseq("bbbab"))

    def test_longestPalindromeSubseq_1(self):
        self.assertEqual(2, Solution().longestPalindromeSubseq("cbbd"))

