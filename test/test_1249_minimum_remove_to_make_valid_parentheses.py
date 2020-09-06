from unittest import TestCase
from problems.N1249_Minimum_Remove_To_Make_Valid_Parentheses import Solution

class TestSolution(TestCase):
    def test_minRemoveToMakeValid(self):
        self.assertEqual("lee(t(c)o)de", Solution().minRemoveToMakeValid("lee(t(c)o)de)"))

    def test_minRemoveToMakeValid_1(self):
        self.assertEqual("ab(c)d", Solution().minRemoveToMakeValid("a)b(c)d"))

    def test_minRemoveToMakeValid_2(self):
        self.assertEqual("", Solution().minRemoveToMakeValid("))(("))

    def test_minRemoveToMakeValid_3(self):
        self.assertEqual("a(b(c)d)", Solution().minRemoveToMakeValid("(a(b(c)d)"))
