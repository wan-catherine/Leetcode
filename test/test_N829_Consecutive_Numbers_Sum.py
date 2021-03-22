from unittest import TestCase
from problems.N829_Consecutive_Numbers_Sum import Solution

class TestSolution(TestCase):
    def test_consecutive_numbers_sum(self):
        self.assertEqual(2, Solution().consecutiveNumbersSum(5))

    def test_consecutive_numbers_sum_1(self):
        self.assertEqual(3, Solution().consecutiveNumbersSum(9))

    def test_consecutive_numbers_sum_2(self):
        self.assertEqual(4, Solution().consecutiveNumbersSum(15))
