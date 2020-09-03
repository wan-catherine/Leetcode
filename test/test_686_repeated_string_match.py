from unittest import TestCase
from problems.N686_Repeated_String_Match import Solution

class TestSolution(TestCase):
    def test_repeatedStringMatch(self):
        self.assertEqual(3, Solution().repeatedStringMatch("abcd", "cdabcdab"))

    def test_repeatedStringMatch_1(self):
        self.assertEqual(2, Solution().repeatedStringMatch("a", "aa"))

    def test_repeatedStringMatch_2(self):
        self.assertEqual(1, Solution().repeatedStringMatch("a", "a"))

    def test_repeatedStringMatch_3(self):
        self.assertEqual(-1, Solution().repeatedStringMatch("abc", "wxyz"))

    def test_repeatedStringMatch_4(self):
        self.assertEqual(-1, Solution().repeatedStringMatch("abaabaa", "abaababaab"))

    def test_repeatedStringMatch_5(self):
        self.assertEqual(-1, Solution().repeatedStringMatch("abcd", "abcdb"))
