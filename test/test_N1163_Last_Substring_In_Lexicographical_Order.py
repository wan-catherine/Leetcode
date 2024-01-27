from unittest import TestCase
from problems.N1163_Last_Substring_In_Lexicographical_Order import Solution

class TestSolution(TestCase):
    def test_last_substring(self):
        self.assertEqual("bab", Solution().lastSubstring("abab"))

    def test_last_substring_1(self):
        self.assertEqual("tcode", Solution().lastSubstring("leetcode"))
