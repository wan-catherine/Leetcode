from unittest import TestCase
from problems.N1392_Longest_Happy_Prefix import Solution

class TestSolution(TestCase):
    def test_longestPrefix(self):
        self.assertEqual("l", Solution().longestPrefix("level"))

    def test_longestPrefix_1(self):
        self.assertEqual("abab", Solution().longestPrefix("ababab"))

    def test_longestPrefix_2(self):
        self.assertEqual("leet", Solution().longestPrefix("leetcodeleet"))

    def test_longestPrefix_3(self):
        self.assertEqual("", Solution().longestPrefix("a"))

    def test_longestPrefix_4(self):
        self.assertEqual("", Solution().longestPrefix("bba"))
