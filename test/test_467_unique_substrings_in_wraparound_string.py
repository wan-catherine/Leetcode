from unittest import TestCase
from problems.N467_Unique_Substrings_In_Wraparound_String import Solution

class TestSolution(TestCase):
    def test_findSubstringInWraproundString(self):
        self.assertEqual(1, Solution().findSubstringInWraproundString("a"))

    def test_findSubstringInWraproundString_1(self):
        self.assertEqual(2, Solution().findSubstringInWraproundString("cac"))

    def test_findSubstringInWraproundString_2(self):
        self.assertEqual(6, Solution().findSubstringInWraproundString("zab"))

    def test_findSubstringInWraproundString_3(self):
        self.assertEqual(3, Solution().findSubstringInWraproundString("abaab"))
