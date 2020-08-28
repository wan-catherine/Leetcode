from unittest import TestCase
from problems.N856_Score_Of_Parentheses import Solution

class TestSolution(TestCase):
    def test_scoreOfParentheses(self):
        self.assertEqual(1, Solution().scoreOfParentheses("()"))

    def test_scoreOfParentheses_1(self):
        self.assertEqual(2, Solution().scoreOfParentheses("(())"))

    def test_scoreOfParentheses_2(self):
        self.assertEqual(2, Solution().scoreOfParentheses("()()"))

    def test_scoreOfParentheses_3(self):
        self.assertEqual(6, Solution().scoreOfParentheses("(()(()))"))
