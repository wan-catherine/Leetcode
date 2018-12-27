from unittest import TestCase
from problems.RemoveInvalidParentheses import Solution

class TestSolution(TestCase):
    def test_removeInvalidParentheses(self):
        solution = Solution()
        res = solution.removeInvalidParentheses("()())()")
        self.assertEqual(["(())()", "()()()"], res)

    def test_removeInvalidParentheses_one(self):
        solution = Solution()
        res = solution.removeInvalidParentheses("(a)())()")
        self.assertEqual(["(a())()", "(a)()()"], res)

    def test_removeInvalidParentheses_two(self):
        solution = Solution()
        res = solution.removeInvalidParentheses(")(")
        self.assertEqual([""], res)

    def test_removeInvalidParentheses_three(self):
        solution = Solution()
        res = solution.removeInvalidParentheses("n")
        self.assertEqual(["n"], res)

    def test_is_valid(self):
        solution = Solution()
        res = solution.IsValid("()())()")
        self.assertEqual(False, res)

    def test_is_valid_two(self):
        solution = Solution()
        res = solution.IsValid("(a)()()")
        self.assertEqual(True, res)
