from unittest import TestCase
from problems.N150_Evaluate_Reverse_Polish_Notation import Solution

class TestSolution(TestCase):
    def test_evalRPN(self):
        self.assertEqual(9, Solution().evalRPN(["2", "1", "+", "3", "*"]))

    def test_evalRPN_1(self):
        self.assertEqual(6, Solution().evalRPN(["4", "13", "5", "/", "+"]))

    def test_evalRPN_2(self):
        self.assertEqual(22, Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
