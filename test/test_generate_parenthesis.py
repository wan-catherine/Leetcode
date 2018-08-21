from unittest import TestCase
from problems.GenerateParentheses import Solution

class TestSolution(TestCase):
    def test_generateParenthesis_3(self):
        solution = Solution()
        res = solution.generateParenthesis(3)
        self.assertEqual([
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
], res)
