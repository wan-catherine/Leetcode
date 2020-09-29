from unittest import TestCase
from problems.N921_Minimum_Add_To_Make_Parentheses_Valid import Solution

class TestSolution(TestCase):
    def test_minAddToMakeValid(self):
        self.assertEqual(1, Solution().minAddToMakeValid("())"))

    def test_minAddToMakeValid_1(self):
        self.assertEqual(3, Solution().minAddToMakeValid("((("))

    def test_minAddToMakeValid_2(self):
        self.assertEqual(0, Solution().minAddToMakeValid("()"))

    def test_minAddToMakeValid_3(self):
        self.assertEqual(4, Solution().minAddToMakeValid("()))(("))

