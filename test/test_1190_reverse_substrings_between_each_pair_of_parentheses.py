from unittest import TestCase
from problems.N1190_Reverse_Substrings_Between_Each_Pair_Of_Parentheses import Solution

class TestSolution(TestCase):
    def test_reverseParentheses(self):
        self.assertEqual("dcba", Solution().reverseParentheses("(abcd)"))

    def test_reverseParentheses_1(self):
        self.assertEqual("iloveu", Solution().reverseParentheses("(u(love)i)"))

    def test_reverseParentheses_2(self):
        self.assertEqual("leetcode", Solution().reverseParentheses("(ed(et(oc))el)"))

    def test_reverseParentheses_3(self):
        self.assertEqual("apmnolkjihgfedcbq", Solution().reverseParentheses("a(bcdefghijkl(mno)p)q"))
