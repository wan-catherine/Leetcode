from unittest import TestCase
from problems.N736_Parse_Lisp_Expression import Solution

class TestSolution(TestCase):
    def test_evaluate(self):
        self.assertEqual(14, Solution().evaluate(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"))

    def test_evaluate_1(self):
        self.assertEqual(2, Solution().evaluate(expression = "(let x 3 x 2 x)"))

    def test_evaluate_2(self):
        self.assertEqual(5, Solution().evaluate(expression = "(let x 1 y 2 x (add x y) (add x y))"))

    def test_evaluate_3(self):
        self.assertEqual(6, Solution().evaluate(expression = "(let x 2 (add (let x 3 (let x 4 x)) x))"))

    def test_evaluate_4(self):
        self.assertEqual(4, Solution().evaluate(expression = "(let a1 3 b2 (add a1 1) b2)"))
