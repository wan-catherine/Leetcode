from unittest import TestCase
from problems.N1044_Longest_Duplicate_Substring import Solution

class TestSolution(TestCase):
    def test_longestDupSubstring(self):
        self.assertEqual('ana', Solution().longestDupSubstring("banana"))

    def test_longestDupSubstring_1(self):
        self.assertEqual('', Solution().longestDupSubstring("abcd"))
