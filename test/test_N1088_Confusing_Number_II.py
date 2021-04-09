from unittest import TestCase
from problems.N1088_Confusing_Number_II import Solution

class TestSolution(TestCase):
    def test_confusing_number_ii(self):
        self.assertEqual(6, Solution().confusingNumberII(20))

    def test_confusing_number_ii_1(self):
        self.assertEqual(19, Solution().confusingNumberII(100))

    def test_confusing_number_ii_2(self):
        self.assertEqual(30956, Solution().confusingNumberII(1999909))
