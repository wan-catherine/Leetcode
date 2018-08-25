from unittest import TestCase
from problems.ImplementStrStr import Solution

class TestSolution(TestCase):
    def test_strStr(self):
        solution = Solution()
        res = solution.strStr("hello", "ll")
        self.assertEqual(2, res)

    def test_strStr_0(self):
        solution = Solution()
        res = solution.strStr("hello", "ab")
        self.assertEqual(-1, res)

    def test_strStr_empty(self):
        solution = Solution()
        res = solution.strStr("hello", "")
        self.assertEqual(0, res)

    def test_strStr_single(self):
        solution = Solution()
        res = solution.strStr("mississippi","a")
        self.assertEqual(-1, res)

    def test_strStr_four(self):
        solution = Solution()
        res = solution.strStr("mississippi","issip")
        self.assertEqual(4, res)

    def test_strStr_three(self):
        solution = Solution()
        res = solution.strStr("aaaaa","bba")
        self.assertEqual(-1, res)

    def test_strStr_equal(self):
        solution = Solution()
        res = solution.strStr("aaa","aaa")
        self.assertEqual(0, res)