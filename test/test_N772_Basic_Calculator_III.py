from unittest import TestCase
from problems.N772_Basic_Calculator_III import Solution

class TestSolution(TestCase):
    def test_calculate(self):
        self.assertEqual(2, Solution().calculate("1+1"))

    def test_calculate_1(self):
        self.assertEqual(4, Solution().calculate("6-4/2"))

    def test_calculate_2(self):
        self.assertEqual(21, Solution().calculate("2*(5+5*2)/3+(6/2+8)"))

    def test_calculate_3(self):
        self.assertEqual(-12, Solution().calculate("(2+6*3+5-(3*14/7+2)*5)+3"))

    def test_calculate_4(self):
        self.assertEqual(0, Solution().calculate("0"))

    def test_calculate_5(self):
        self.assertEqual(0, Solution().calculate("(0-3)/4"))