from unittest import TestCase
from problems.ReverseInteger import Solution

class TestSolution(TestCase):
    def test_reverse_by_positive(self):
        solution = Solution()
        res = solution.reverse(123)
        self.assertEquals(321, res)

    def test_reverse_by_negative(self):
        solution = Solution()
        res = solution.reverse(-123)
        self.assertEquals(-321, res)

    def test_reverse_by_end_with_zero(self):
        solution = Solution()
        res = solution.reverse(120)
        self.assertEquals(21, res)

    def test_reverse_by_positive_overflow(self):
        solution = Solution()
        res = solution.reverse(2**31)
        self.assertEquals(0, res)

    def test_reverse_by_negative_overflow(self):
        solution = Solution()
        res = solution.reverse(2**32)
        self.assertEquals(0, res)