from unittest import TestCase
from problems.N400_Nth_Digit import Solution

class TestSolution(TestCase):
    def test_find_nth_digit(self):
        self.assertEqual(3, Solution().findNthDigit(3))

    def test_find_nth_digit_1(self):
        self.assertEqual(0, Solution().findNthDigit(11))

    def test_find_nth_digit_2(self):
        self.assertEqual(1, Solution().findNthDigit(10))

    def test_find_nth_digit_3(self):
        self.assertEqual(3, Solution().findNthDigit(1000))
