from unittest import TestCase
from problems.IntegerBreak import Solution

class TestSolution(TestCase):
    def test_integerBreak(self):
        solution = Solution()
        res = solution.integerBreak(2)
        self.assertEqual(res, 1)

    def test_integerBreak_one(self):
        solution = Solution()
        res = solution.integerBreak(10)
        self.assertEqual(res, 36)

    def test_integerBreak_two(self):
        solution = Solution()
        res = solution.integerBreak(4)
        self.assertEqual(res, 4)

    def test_integerBreak_three(self):
        solution = Solution()
        res = solution.integerBreak(8)
        self.assertEqual(res, 18)
