from unittest import TestCase
from problems.N809_Expressive_Words import Solution

class TestSolution(TestCase):
    def test_expressiveWords(self):
        S = "heeellooo"
        words = ["hello", "hi", "helo"]
        self.assertEqual(1, Solution().expressiveWords(S, words))

    def test_expressiveWords_1(self):
        S = "abcd"
        words = ["abc"]
        self.assertEqual(0, Solution().expressiveWords(S, words))

    def test_expressiveWords_2(self):
        S = ""
        words = ["hello","hi","helo"]
        self.assertEqual(0, Solution().expressiveWords(S, words))
