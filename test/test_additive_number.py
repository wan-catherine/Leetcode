from unittest import TestCase
from problems.AdditiveNumber import Solution

class TestSolution(TestCase):
    def test_isAdditiveNumber(self):
        solution = Solution()
        res = solution.isAdditiveNumber("112358")
        self.assertEqual(res, True)

    def test_isAdditiveNumber_one(self):
        solution = Solution()
        res = solution.isAdditiveNumber("199100199")
        self.assertEqual(res, True)

    def test_isAdditiveNumber_two(self):
        solution = Solution()
        res = solution.isAdditiveNumber("000")
        self.assertEqual(res, True)

    def test_isAdditiveNumber_three(self):
        solution = Solution()
        res = solution.isAdditiveNumber("0235813")
        self.assertEqual(res, False)