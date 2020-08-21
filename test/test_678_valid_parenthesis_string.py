from unittest import TestCase
from problems.N678_Valid_Parenthesis_String import Solution

class TestSolution(TestCase):
    def test_checkValidString(self):
        self.assertTrue(Solution().checkValidString("()"))

    def test_checkValidString_1(self):
        self.assertTrue(Solution().checkValidString("(*)"))

    def test_checkValidString_2(self):
        self.assertTrue(Solution().checkValidString("(*))"))

    def test_checkValidString_3(self):
        self.assertFalse(Solution().checkValidString("("))
