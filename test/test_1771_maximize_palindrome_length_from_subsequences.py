from unittest import TestCase
from problems.N1771_Maximize_Palindrome_Length_From_Subsequences import Solution

class TestSolution(TestCase):
    def test_longestPalindrome(self):
        self.assertEqual(5, Solution().longestPalindrome(word1 = "cacb", word2 = "cbba"))

    def test_longestPalindrome_1(self):
        self.assertEqual(3, Solution().longestPalindrome(word1 = "ab", word2 = "ab"))

    def test_longestPalindrome_2(self):
        self.assertEqual(0, Solution().longestPalindrome(word1 = "aa", word2 = "bb"))
