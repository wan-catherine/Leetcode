from unittest import TestCase
from problems.MultiplyStrings import Solution

class TestSolution(TestCase):
    def test_multiply(self):
        solution = Solution()
        res = solution.multiply("2","3")
        self.assertEqual(res, "6")

    def test_multiply_more(self):
        solution = Solution()
        res = solution.multiply("123","456")
        self.assertEqual(res, "56088")
