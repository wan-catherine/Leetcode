from unittest import TestCase
from problems.N395_Longest_Substring_With_At_Least_K_Repeating_Characters import Solution

class TestSolution(TestCase):
    def test_longestSubstring(self):
        self.assertEqual(3, Solution().longestSubstring(s = "aaabb", k = 3))

    def test_longestSubstring_1(self):
        self.assertEqual(5, Solution().longestSubstring(s = "ababbc", k = 2))
