from unittest import TestCase
from problems.N1451_Rearrange_Words_In_A_Sentence import Solution

class TestSolution(TestCase):
    def test_arrangeWords(self):
        self.assertEqual("Is cool leetcode", Solution().arrangeWords("Leetcode is cool"))

    def test_arrangeWords_1(self):
        self.assertEqual("On and keep calm code", Solution().arrangeWords("Keep calm and code on"))

    def test_arrangeWords_2(self):
        self.assertEqual("To be or to be not", Solution().arrangeWords("To be or not to be"))