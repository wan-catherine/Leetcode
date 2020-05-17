from unittest import TestCase
from problems.N76_Minimum_Window_Substring import Solution

class TestSolution(TestCase):
    def test_minWindow(self):
        solution = Solution()
        res = solution.minWindow("ADOBECODEBANC", "ABC")
        self.assertEqual("BANC", res)

    def test_minWindow_1(self):
        solution = Solution()
        res = solution.minWindow("aa", "aa")
        self.assertEqual("aa", res)

    def test_minWindow_2(self):
        solution = Solution()
        res = solution.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")
        self.assertEqual("abbbbbcdd", res)
