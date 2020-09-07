from unittest import TestCase
from problems.N1328_Break_A_Palindrome import Solution

class TestSolution(TestCase):
    def test_breakPalindrome(self):
        self.assertEqual("aaccba", Solution().breakPalindrome("abccba"))

    def test_breakPalindrome_1(self):
        self.assertEqual("", Solution().breakPalindrome("a"))

    def test_breakPalindrome_2(self):
        self.assertEqual("aabab", Solution().breakPalindrome("aabaa"))
