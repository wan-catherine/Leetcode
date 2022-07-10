from unittest import TestCase
from problems.N2335_Minimum_Amount_Of_Time_To_Fill_Cups import Solution

class TestSolution(TestCase):
    def test_fill_cups(self):
        self.assertEqual(4, Solution().fillCups([1,4,2]))

    def test_fill_cups_1(self):
        self.assertEqual(7, Solution().fillCups([5,4,4]))

    def test_fill_cups_2(self):
        self.assertEqual(5, Solution().fillCups([5,0,0]))


