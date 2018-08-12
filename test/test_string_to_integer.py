from unittest import TestCase
from problems.StringToInteger import Solution

class TestSolution(TestCase):
    def test_myAtoi_with_normal_number(self):
        solution = Solution()
        res = solution.myAtoi("42")
        self.assertEquals(42, res)

    def test_myAtoi_with_starts_whitespace_number(self):
        solution = Solution()
        res = solution.myAtoi("   42")
        self.assertEquals(42, res)

    def test_myAtoi_with_starts_whitespace_negative_number(self):
        solution = Solution()
        res = solution.myAtoi("   -42")
        self.assertEquals(-42, res)

    def test_myAtoi_with_ends_nonnumber(self):
        solution = Solution()
        res = solution.myAtoi("4193 with words")
        self.assertEquals(4193, res)

    def test_myAtoi_with_starts_nonnumber(self):
        solution = Solution()
        res = solution.myAtoi("words and 987")
        self.assertEquals(0, res)

    def test_myAtoi_with_out_of_range_nonnumber(self):
        solution = Solution()
        res = solution.myAtoi("-91283472332")
        self.assertEquals(-2147483648, res)

    def test_myAtoi_with_positive_number(self):
        solution = Solution()
        res = solution.myAtoi("+12")
        self.assertEquals(12, res)

    def test_myAtoi_with_negative_positive_number(self):
        solution = Solution()
        res = solution.myAtoi("+-12")
        self.assertEquals(0, res)

    def test_myAtoi_with_positive_negative_number(self):
        solution = Solution()
        res = solution.myAtoi("-+12")
        self.assertEquals(0, res)

    def test_myAtoi_with_strange_number(self):
        solution = Solution()
        res = solution.myAtoi("   +0 123")
        self.assertEquals(0, res)