from unittest import TestCase
from problems.IntegerToRoman import Solution

class TestSolution(TestCase):
    def test_int_2_roman_with_single_number(self):
        solution = Solution()
        res = solution.intToRoman(4)
        self.assertEqual("IV", res)

    def test_int_2_roman_with_single_number_three(self):
        solution = Solution()
        res = solution.intToRoman(3)
        self.assertEquals("III", res)

    def test_int_2_roman_with_single_number_nine(self):
        solution = Solution()
        res = solution.intToRoman(9)
        self.assertEquals("IX", res)

    def test_int_2_roman_with_single_number_1994(self):
        solution = Solution()
        res = solution.intToRoman(1994)
        self.assertEqual("MCMXCIV", res)

    def test_int_2_roman_with_single_number_11(self):
        solution = Solution()
        res = solution.intToRoman(11)
        self.assertEqual("XI", res)

    def test_int_2_roman_with_single_number_60(self):
        solution = Solution()
        res = solution.intToRoman(60)
        self.assertEqual("LX", res)

    def test_int_2_roman_with_single_number_600(self):
        solution = Solution()
        res = solution.intToRoman(600)
        self.assertEqual("DC", res)
