from unittest import TestCase
from problems.N1625_Lexicographically_Smallest_String_After_Applying_Operations import Solution

class TestSolution(TestCase):
    def test_findLexSmallestString(self):
        self.assertEqual("2050", Solution().findLexSmallestString(s = "5525", a = 9, b = 2))

    def test_findLexSmallestString_1(self):
        self.assertEqual("24", Solution().findLexSmallestString(s = "74", a = 5, b = 1))

    def test_findLexSmallestString_2(self):
        self.assertEqual("0011", Solution().findLexSmallestString(s = "0011", a = 4, b = 2))

    def test_findLexSmallestString_3(self):
        self.assertEqual("00553311", Solution().findLexSmallestString(s = "43987654", a = 7, b = 3))

