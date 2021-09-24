from unittest import TestCase
from problems.N2014_Longest_Subsequence_Repeated_K_Times import Solution

class TestSolution(TestCase):
    def test_longest_subsequence_repeated_k(self):
        self.assertEqual("let", Solution().longestSubsequenceRepeatedK(s = "letsleetcode", k = 2))

    def test_longest_subsequence_repeated_k_1(self):
        self.assertEqual("b", Solution().longestSubsequenceRepeatedK(s = "bb", k = 2))

    def test_longest_subsequence_repeated_k_2(self):
        self.assertEqual("", Solution().longestSubsequenceRepeatedK(s = "ab", k = 2))

    def test_longest_subsequence_repeated_k_3(self):
        self.assertEqual("bbbb", Solution().longestSubsequenceRepeatedK(s = "bbabbabbbbabaababab", k = 3))
