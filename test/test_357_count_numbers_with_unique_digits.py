from unittest import TestCase
from problems.N357_Count_Numbers_With_Unique_Digits import Solution

class TestSolution(TestCase):
    def test_countNumbersWithUniqueDigits(self):
        self.assertEqual(91, Solution().countNumbersWithUniqueDigits(2))

    def test_countNumbersWithUniqueDigits_1(self):
        self.assertEqual(1, Solution().countNumbersWithUniqueDigits(0))

    def test_countNumbersWithUniqueDigits_2(self):
        self.assertEqual(739, Solution().countNumbersWithUniqueDigits(3))
