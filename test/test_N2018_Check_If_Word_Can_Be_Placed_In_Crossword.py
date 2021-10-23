from unittest import TestCase
from problems.N2018_Check_If_Word_Can_Be_Placed_In_Crossword import Solution

class TestSolution(TestCase):
    def test_place_word_in_crossword(self):
        self.assertTrue(Solution().placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"))

    def test_place_word_in_crossword_1(self):
        self.assertFalse(Solution().placeWordInCrossword(board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"))

    def test_place_word_in_crossword_2(self):
        self.assertTrue(Solution().placeWordInCrossword(board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"))

    def test_place_word_in_crossword_3(self):
        self.assertFalse(Solution().placeWordInCrossword([[" "],["b"],[" "],["a"]], "abcd"))

    def test_place_word_in_crossword_4(self):
        self.assertTrue(Solution().placeWordInCrossword(board = [["#", " ", "#"], ["#", " ", "#"], ["#", " ", "c"]], word = "ca"))