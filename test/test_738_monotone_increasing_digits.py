from unittest import TestCase
from problems.N738_Monotone_Increasing_Digits import Solution

class TestSolution(TestCase):
    def test_monotoneIncreasingDigits(self):
        self.assertEqual(9, Solution().monotoneIncreasingDigits(10))

    def test_monotoneIncreasingDigits_1(self):
        self.assertEqual(1234, Solution().monotoneIncreasingDigits(1234))

    def test_monotoneIncreasingDigits_2(self):
        self.assertEqual(299, Solution().monotoneIncreasingDigits(332))

    def test_monotoneIncreasingDigits_3(self):
        self.assertEqual(99, Solution().monotoneIncreasingDigits(101))

    def test_monotoneIncreasingDigits_4(self):
        self.assertEqual(667999, Solution().monotoneIncreasingDigits(668841))
