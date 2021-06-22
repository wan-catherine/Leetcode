from unittest import TestCase
from problems.N224_Basic_Calculator import Solution

class TestSolution(TestCase):
    def test_calculate(self):
        self.assertEqual(2, Solution().calculate("1 + 1"))

    def test_calculate_1(self):
        self.assertEqual(3, Solution().calculate(" 2-1 + 2 "))

    def test_calculate_2(self):
        self.assertEqual(23, Solution().calculate("(1+(4+5+2)-3)+(6+8)"))

    def test_calculate_3(self):
        self.assertEqual(0, Solution().calculate("+48 + -48"))
