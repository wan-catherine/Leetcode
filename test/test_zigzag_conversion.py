from unittest import TestCase
from problems.ZigZagConversion import Solution

class TestSolution(TestCase):
    def test_convert_by_three_rows(self):
        solution = Solution()
        res = solution.convert("PAYPALISHIRING", 3)
        self.assertEquals("PAHNAPLSIIGYIR", res)

    def test_convert_by_four_rows(self):
        solution = Solution()
        res = solution.convert("PAYPALISHIRING", 4)
        self.assertEquals("PINALSIGYAHRPI", res)

    def test_convert_by_one_column(self):
        solution = Solution()
        res = solution.convert("ab", 4)
        self.assertEquals("ab", res)

    def test_convert_by_empty(self):
        solution = Solution()
        res = solution.convert("", 4)
        self.assertEquals("", res)

    def test_convert_by_one_row_one_column(self):
        solution = Solution()
        res = solution.convert("a", 1)
        self.assertEquals("a", res)
