from unittest import TestCase
from problems.N1433_Check_If_A_String_Can_Break_Another_String import Solution

class TestSolution(TestCase):
    def test_checkIfCanBreak(self):
        self.assertTrue(Solution().checkIfCanBreak(s1 = "abc", s2 = "xya"))

    def test_checkIfCanBreak_1(self):
        self.assertFalse(Solution().checkIfCanBreak(s1 = "abe", s2 = "acd"))

    def test_checkIfCanBreak_2(self):
        self.assertTrue(Solution().checkIfCanBreak(s1 = "leetcodee", s2 = "interview"))

    def test_checkIfCanBreak_3(self):
        self.assertTrue(Solution().checkIfCanBreak("yopumzgd", "pamntyya"))