from unittest import TestCase
from problems.N418_Sentence_Screen_Fitting import Solution

class TestSolution(TestCase):
    def test_words_typing(self):
        self.assertEqual(1, Solution().wordsTyping(rows = 2, cols = 8, sentence = ["hello", "world"]))

    def test_words_typing_1(self):
        self.assertEqual(2, Solution().wordsTyping(rows = 3, cols = 6, sentence = ["a", "bcd", "e"]))

    def test_words_typing_2(self):
        self.assertEqual(1, Solution().wordsTyping(rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]))

    def test_words_typing_3(self):
        self.assertEqual(5293333, Solution().wordsTyping(["try","to","be","better"], 10000, 9001))