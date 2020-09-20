from unittest import TestCase
from problems.N664_Strange_Printer import Solution

class TestSolution(TestCase):
    def test_strangePrinter(self):
        self.assertEqual(2, Solution().strangePrinter("aaabbb"))

    def test_strangePrinter_1(self):
        self.assertEqual(2, Solution().strangePrinter("aba"))

    def test_strangePrinter_2(self):
        self.assertEqual(5, Solution().strangePrinter("abcabc"))

    def test_strangePrinter_3(self):
        self.assertEqual(7, Solution().strangePrinter("abcabcabc"))

    def test_strangePrinter_4(self):
        self.assertEqual(4, Solution().strangePrinter("tbgtgb"))