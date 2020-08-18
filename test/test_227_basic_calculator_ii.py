from unittest import TestCase
from problems.N227_Basic_Calculator_II import Solution

class TestSolution(TestCase):
    def test_calculate(self):
        self.assertEqual(7, Solution().calculate("3+2*2"))

    def test_calculate_1(self):
        self.assertEqual(1, Solution().calculate(" 3/2 "))

    def test_calculate_2(self):
        self.assertEqual(5, Solution().calculate(" 3+5 / 2 "))

    def test_calculate_3(self):
        self.assertEqual(42, Solution().calculate("42"))

    def test_calculate_4(self):
        self.assertEqual(-2147483647, Solution().calculate("0-2147483647"))

    def test_calculate_5(self):
        self.assertEqual(13, Solution().calculate("14-3/2"))
