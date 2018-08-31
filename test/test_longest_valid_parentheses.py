from unittest import TestCase
from problems.LongestValidParentheses import Solution

class TestSolution(TestCase):
    def test_longestValidParentheses(self):
        solution = Solution()
        res = solution.longestValidParentheses("(()")
        self.assertEqual(2, res)

    def test_longestValidParentheses_four(self):
        solution = Solution()
        res = solution.longestValidParentheses(")()())")
        self.assertEqual(4, res)

    def test_longestValidParentheses_2(self):
        solution = Solution()
        res = solution.longestValidParentheses("()(()")
        self.assertEqual(2, res)

