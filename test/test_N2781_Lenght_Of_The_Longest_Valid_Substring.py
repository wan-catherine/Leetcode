from unittest import TestCase
from problems.N2781_Length_Of_The_Longest_Valid_Substring import Solution

class TestSolution(TestCase):
    def test_longest_valid_substring(self):
        self.assertEquals(4, Solution().longestValidSubstring(word = "cbaaaabc", forbidden = ["aaa","cb"]))

    def test_longest_valid_substring_1(self):
        self.assertEquals(4, Solution().longestValidSubstring(word = "leetcode", forbidden = ["de","le","e"]))
