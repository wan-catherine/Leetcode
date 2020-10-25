from unittest import TestCase
from problems.N214_Shortest_Palindrome import Solution

class TestSolution(TestCase):
    def test_shortestPalindrome(self):
        self.assertEqual("aaaceecaaa", Solution().shortestPalindrome("aaceecaaa"))

    def test_shortestPalindrome_1(self):
        self.assertEqual("dcbabcd", Solution().shortestPalindrome("abcd"))