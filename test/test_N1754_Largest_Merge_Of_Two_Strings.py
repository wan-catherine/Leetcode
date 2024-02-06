from unittest import TestCase
from problems.N1754_Largest_Merge_Of_Two_Strings import Solution

class TestSolution(TestCase):
    def test_largest_merge(self):
        self.assertEqual("cbcabaaaaa", Solution().largestMerge(word1 = "cabaa", word2 = "bcaaa"))

    def test_largest_merge_1(self):
        self.assertEqual("abdcabcabcaba", Solution().largestMerge(word1 = "abcabc", word2 = "abdcaba"))
