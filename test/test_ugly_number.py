from unittest import TestCase
from problems.UglyNumber import Solution

class TestSolution(TestCase):
    def test_isUgly(self):
        solution = Solution()
        res = solution.isUgly(6)
        self.assertEqual(res, True)

    def test_isUgly_one(self):
        solution = Solution()
        res = solution.isUgly(8)
        self.assertEqual(res, True)

    def test_isUgly_two(self):
        solution = Solution()
        res = solution.isUgly(14)
        self.assertEqual(res, False)

