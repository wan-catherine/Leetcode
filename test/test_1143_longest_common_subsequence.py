from unittest import TestCase
from problems.N1143_Longest_Common_Subsequence import Solution

class TestSolution(TestCase):
    def test_longestCommonSubsequence(self):
        self.assertEqual(3, Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))

    def test_longestCommonSubsequence_1(self):
        self.assertEqual(3, Solution().longestCommonSubsequence(text1 = "abc", text2 = "abc"))

    def test_longestCommonSubsequence_2(self):
        self.assertEqual(0, Solution().longestCommonSubsequence(text1 = "abc", text2 = "def"))
