from unittest import TestCase
from problems.LongestCommonPrefix import Solution


class TestSolution(TestCase):
    def test_longestCommonPrefix_with_three_words(self):
        solution = Solution()
        res = solution.longestCommonPrefix(["flower","flow","flight"])
        self.assertEquals(res, "fl")

    def test_longestCommonPrefix_with_no_common(self):
        solution = Solution()
        res = solution.longestCommonPrefix(["dog","racecar","car"])
        self.assertEquals(res, "")

    def test_longestCommonPrefix_with_one_common(self):
        solution = Solution()
        res = solution.longestCommonPrefix(["aa","a"])
        self.assertEquals(res, "a")

