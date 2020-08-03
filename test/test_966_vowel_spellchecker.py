from unittest import TestCase
from problems.N966_Vowel_Spellchecker import Solution

class TestSolution(TestCase):
    def test_spellchecker(self):
        wordlist = ["KiTe", "kite", "hare", "Hare"]
        queries = ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear",
                                                                "keti", "keet", "keto"]
        output = ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
        self.assertListEqual(output, Solution().spellchecker(wordlist, queries))

    def test_spellchecker_1(self):
        wordlist = ["ae","aa"]
        queries = ["UU"]
        output = ["ae"]
        self.assertListEqual(output, Solution().spellchecker(wordlist, queries))

    def test_spellchecker_2(self):
        wordlist = ["YellOw"]
        queries = ["yollow"]
        output = ["YellOw"]
        self.assertListEqual(output, Solution().spellchecker(wordlist, queries))
