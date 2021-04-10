from unittest import TestCase
from problems.N233_Number_Of_Digit_One import Solution

class TestSolution(TestCase):
    def test_count_digit_one(self):
        self.assertEqual(6, Solution().countDigitOne(13))

    def test_count_digit_one_1(self):
        self.assertEqual(0, Solution().countDigitOne(0))

    def test_count_digit_one_2(self):
        self.assertEqual(2, Solution().countDigitOne(10))

    def test_count_digit_one_3(self):
        self.assertEqual(12, Solution().countDigitOne(20))

    def test_count_digit_one_4(self):
        self.assertEqual(33, Solution().countDigitOne(110))

