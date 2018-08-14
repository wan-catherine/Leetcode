from unittest import TestCase
from problems.RomanToInteger import Solution

class TestSolution(TestCase):
    def test_roman_Int_3(self):
        solution = Solution()
        res = solution.romanToInt("III")
        self.assertEqual(3, res)

    def test_roman_Int_4(self):
        solution = Solution()
        res = solution.romanToInt("IV")
        self.assertEqual(4, res)

    def test_roman_Int_9(self):
        solution = Solution()
        res = solution.romanToInt("XI")
        self.assertEqual(11, res)

    def test_roman_Int_11(self):
        solution = Solution()
        res = solution.romanToInt("IX")
        self.assertEqual(9, res)

    def test_roman_Int_58(self):
        solution = Solution()
        res = solution.romanToInt("LVIII")
        self.assertEqual(58, res)

    def test_roman_Int_500(self):
        solution = Solution()
        res = solution.romanToInt("D")
        self.assertEqual(500, res)

    def test_roman_Int_1994(self):
        solution = Solution()
        res = solution.romanToInt("MCMXCIV")
        self.assertEqual(1994, res)

    def test_roman_Int_1695(self):
        solution = Solution()
        res = solution.romanToInt("MDCXCV")
        self.assertEqual(1695, res)
