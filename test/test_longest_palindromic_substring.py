from unittest import TestCase
from problems.LongestPalindromicSubstring import Solution

class TestSolution(TestCase):
    def test_longestPalindrome(self):
        solution = Solution()
        res = solution.longestPalindrome("babad")
        self.assertEqual("bab", res)

    def test_longestPalindrome_one(self):
        solution = Solution()
        res = solution.longestPalindrome("cbbd")
        self.assertEqual("bb", res)


    def test_longestPalindrome_two(self):
        solution = Solution()
        res = solution.longestPalindrome("aaaa")
        self.assertEqual("aaaa", res)