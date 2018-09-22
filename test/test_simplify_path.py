from unittest import TestCase
from problems.SimplifyPath import Solution

class TestSolution(TestCase):
    def test_simplifyPath(self):
        solution = Solution()
        res = solution.simplifyPath( "/home/")
        self.assertEqual(res, "/home")

    def test_simplifyPath_cornor(self):
        solution = Solution()
        res = solution.simplifyPath( "/../")
        self.assertEqual(res, "/")

    def test_simplifyPath_1(self):
        solution = Solution()
        res = solution.simplifyPath( "/a/./b/../../c/")
        self.assertEqual(res, "/c")

    def test_simplifyPath_2(self):
        solution = Solution()
        res = solution.simplifyPath( "/a/../../b/../c//.//")
        self.assertEqual(res, "/c")

    def test_simplifyPath_3(self):
        solution = Solution()
        res = solution.simplifyPath( "/a//b////c/d//././/..")
        self.assertEqual(res, "/a/b/c")
