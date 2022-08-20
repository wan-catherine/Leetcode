from unittest import TestCase
from problems.N2376_Count_Special_Integers import Solution

class TestSolution(TestCase):
    def test_count_special_numbers(self):
        self.assertEqual(19, Solution().countSpecialNumbers(20))

    def test_count_special_numbers_1(self):
        self.assertEqual(5, Solution().countSpecialNumbers(5))

    def test_count_special_numbers_2(self):
        self.assertEqual(110, Solution().countSpecialNumbers(135))

