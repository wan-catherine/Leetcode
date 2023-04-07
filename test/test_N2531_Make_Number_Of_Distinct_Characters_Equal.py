from unittest import TestCase
from problems.N2531_Make_Number_Of_Distinct_Characters_Equal import Solution

class TestSolution(TestCase):
    def test_is_it_possible(self):
        self.assertFalse(Solution().isItPossible(word1 = "ac", word2 = "b"))

    def test_is_it_possible_1(self):
        self.assertTrue(Solution().isItPossible(word1 = "abcc", word2 = "aab"))

    def test_is_it_possible_2(self):
        self.assertTrue(Solution().isItPossible(word1 = "abcde", word2 = "fghij"))

    def test_is_it_possible_3(self):
        self.assertFalse(Solution().isItPossible(word1 = "a", word2 = "bb"))

    def test_is_it_possible_4(self):
        self.assertTrue(Solution().isItPossible(word1 = "aa", word2 = "bb"))

    def test_is_it_possible_5(self):
        self.assertTrue(Solution().isItPossible(word1 = "aab", word2 = "bccd"))