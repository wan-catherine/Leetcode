from unittest import TestCase
from problems.N1553_Minimum_Number_Of_Days_To_Eat_N_Oranges import Solution

class TestSolution(TestCase):
    def test_minDays(self):
        self.assertEqual(4, Solution().minDays(10))

    def test_minDays_1(self):
        self.assertEqual(3, Solution().minDays(6))

    def test_minDays_2(self):
        self.assertEqual(1, Solution().minDays(1))

    def test_minDays_3(self):
        self.assertEqual(6, Solution().minDays(56))