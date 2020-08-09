from unittest import TestCase
from problems.N1371_Find_The_Longest_Substring_Containing_Vowels_In_Even_Counts import Solution

class TestSolution(TestCase):
    def test_findTheLongestSubstring(self):
        self.assertEqual(13, Solution().findTheLongestSubstring("eleetminicoworoep"))

    def test_findTheLongestSubstring_1(self):
        self.assertEqual(5, Solution().findTheLongestSubstring("leetcodeisgreat"))

    def test_findTheLongestSubstring_2(self):
        self.assertEqual(6, Solution().findTheLongestSubstring("bcbcbc"))
