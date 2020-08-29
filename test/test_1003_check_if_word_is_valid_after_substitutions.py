from unittest import TestCase
from problems.N1003_Check_If_Word_Is_Valid_After_Substitutions import Solution

class TestSolution(TestCase):
    def test_isValid(self):
        self.assertTrue(Solution().isValid("aabcbc"))

    def test_isValid_1(self):
        self.assertTrue(Solution().isValid("abcabcababcc"))

    def test_isValid_2(self):
        self.assertFalse(Solution().isValid("abccba"))

    def test_isValid_3(self):
        self.assertFalse(Solution().isValid("cababc"))
