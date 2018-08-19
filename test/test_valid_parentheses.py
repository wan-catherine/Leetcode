from unittest import TestCase
from problems.ValidParentheses import Solution

class TestSolution(TestCase):
    def test_isValid_with_two(self):
        solution = Solution()
        res = solution.isValid("()")
        self.assertEqual(True, res)

    def test_isValid_with_6(self):
        solution = Solution()
        res = solution.isValid("()[]{}")
        self.assertEqual(True, res)

    def test_isValid_with_two_false(self):
        solution = Solution()
        res = solution.isValid("(]")
        self.assertEqual(False, res)

    def test_isValid_with_4(self):
        solution = Solution()
        res = solution.isValid("([)]")
        self.assertEqual(False, res)

    def test_isValid_with_empty(self):
        solution = Solution()
        res = solution.isValid("")
        self.assertEqual(True, res)

    def test_isValid_with_only_right(self):
        solution = Solution()
        res = solution.isValid("]")
        self.assertEqual(False, res)

    def test_isValid_with_only_left(self):
        solution = Solution()
        res = solution.isValid("[")
        self.assertEqual(False, res)
