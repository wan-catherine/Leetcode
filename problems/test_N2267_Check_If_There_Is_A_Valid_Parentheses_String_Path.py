from unittest import TestCase
from problems.N2267_Check_If_There_Is_A_Valid_Parentheses_String_Path import Solution

class TestSolution(TestCase):
    def test_has_valid_path(self):
        self.assertTrue(Solution().hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]))

    def test_has_valid_path_1(self):
        self.assertFalse(Solution().hasValidPath([[")",")"],["(","("]]))
