from unittest import TestCase
from problems.N1012_Numbers_With_Repeated_Digits import Solution

class TestSolution(TestCase):
    def test_num_dup_digits_at_most_n(self):
        self.assertEqual(1, Solution().numDupDigitsAtMostN(20))

    def test_num_dup_digits_at_most_n_1(self):
        self.assertEqual(10, Solution().numDupDigitsAtMostN(100))

    def test_num_dup_digits_at_most_n_2(self):
        self.assertEqual(262, Solution().numDupDigitsAtMostN(1000))

    def test_num_dup_digits_at_most_n_3(self):
        self.assertEqual(1, Solution().numDupDigitsAtMostN(12))

    def test_num_dup_digits_at_most_n_4(self):
        self.assertEqual(12, Solution().numDupDigitsAtMostN(110))
