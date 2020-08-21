from unittest import TestCase
from problems.N127_Word_Ladder import Solution

class TestSolution(TestCase):
    def test_ladderLength(self):
        self.assertEqual(5, Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))

    def test_ladderLength_1(self):
        self.assertEqual(0, Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log"]))

    def test_ladderLength_2(self):
        self.assertEqual(0, Solution().ladderLength("hit","dog",["hot","dog"]))

    def test_ladderLength_3(self):
        words = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci",
         "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
         "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb",
         "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo",
         "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr",
         "pa", "he", "lr", "sq", "ye"]
        self.assertEqual(5, Solution().ladderLength("qa","sq",words))
