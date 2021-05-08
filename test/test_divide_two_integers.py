from unittest import TestCase
from problems.DivideTwoIntegers import Solution

class TestSolution(TestCase):
    def test_divide(self):
        solution = Solution()
        res = solution.divide(10, 3)
        self.assertEqual(3, res)

    def test_divide_1(self):
        solution = Solution()
        res = solution.divide(1, 1)
        self.assertEqual(1, res)

    def test_divide_2(self):
        solution = Solution()
        res = solution.divide(-2147483648, -1)
        self.assertEqual(2147483647, res)

    def test_divide_3(self):
        solution = Solution()
        res = solution.divide(-2147483648, 1)
        self.assertEqual(-2147483648, res)
