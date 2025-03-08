from unittest import TestCase
from problems.N2730_Find_The_Longest_Semi_Repetitive_Substring import Solution

class TestSolution(TestCase):
    def test_longest_semi_repetitive_substring(self):
        self.assertEquals(4, Solution().longestSemiRepetitiveSubstring("52233"))

    def test_longest_semi_repetitive_substring_1(self):
        self.assertEquals(4, Solution().longestSemiRepetitiveSubstring("5494"))

    def test_longest_semi_repetitive_substring_2(self):
        self.assertEquals(2, Solution().longestSemiRepetitiveSubstring("1111111"))

    def test_longest_semi_repetitive_substring_3(self):
        self.assertEquals(3, Solution().longestSemiRepetitiveSubstring("001"))

    def test_longest_semi_repetitive_substring_4(self):
        self.assertEquals(3, Solution().longestSemiRepetitiveSubstring("0001"))
