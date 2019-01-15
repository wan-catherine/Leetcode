from unittest import TestCase
from problems.UglyNumberII import Solution

class TestSolution(TestCase):
    def test_nthUglyNumber(self):
        solution = Solution()
        res = solution.nthUglyNumber(10)
        self.assertEqual(res, 12)

    def test_nthUglyNumber_one(self):
        solution = Solution()
        res = solution.nthUglyNumber(1)
        self.assertEqual(res, 1)

    def test_nthUglyNumber_two(self):
        solution = Solution()
        res = solution.nthUglyNumber(2)
        self.assertEqual(res, 2)

    def test_nthUglyNumber_three(self):
        solution = Solution()
        res = solution.nthUglyNumber(11)
        self.assertEqual(res, 15)
