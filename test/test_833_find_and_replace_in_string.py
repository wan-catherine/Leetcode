from unittest import TestCase
from problems.N833_Find_And_Replace_In_String import Solution

class TestSolution(TestCase):
    def test_findReplaceString(self):
        self.assertEqual("eeebffff", Solution().findReplaceString(S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]))

    def test_findReplaceString_1(self):
        self.assertEqual("eeecd", Solution().findReplaceString(S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]))

    def test_findReplaceString_2(self):
        S = "vmokgggqzp"
        indexes = [3, 5, 1]
        sources = ["kg", "ggq", "mo"]
        targets = ["s", "so", "bfr"]
        self.assertEqual("vbfrssozp", Solution().findReplaceString(S, indexes, sources, targets))
