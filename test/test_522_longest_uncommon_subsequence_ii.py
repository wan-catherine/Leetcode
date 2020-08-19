from unittest import TestCase
from problems.N522_Longest_Uncommon_Subsequence_II import Solution

class TestSolution(TestCase):
    def test_findLUSlength(self):
        self.assertEqual(3, Solution().findLUSlength(["aba", "cdc", "eae"]))

    def test_findLUSlength_1(self):
        self.assertEqual(-1, Solution().findLUSlength(["aaa","aaa","aa"]))

    def test_findLUSlength_2(self):
        self.assertEqual(2, Solution().findLUSlength(["aabbcc", "aabbcc","cb","abc"]))

    def test_findLUSlength_3(self):
        self.assertEqual(-1, Solution().findLUSlength(["abcabc","abcabc","abcabc","abc","abc","aab"]))

    def test_findLUSlength_4(self):
        self.assertEqual(7, Solution().findLUSlength(["te","gxkcheu","gxkcheu","wrkbh","wrkbh","iktlekjudj","iktlekjudj","pcw","pcw","flgwshwauv","flgwshwauv","ix","qncmqfl","aohlzbonfg","aohlzbonfg","pzp"]))
