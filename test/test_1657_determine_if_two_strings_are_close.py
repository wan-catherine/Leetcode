from unittest import TestCase
from problems.N1657_Determine_If_Two_Strings_Are_Close import Solution

class TestSolution(TestCase):
    def test_closeStrings(self):
        self.assertTrue(Solution().closeStrings(word1 = "abc", word2 = "bca"))

    def test_closeStrings_1(self):
        self.assertFalse(Solution().closeStrings(word1 = "a", word2 = "aa"))

    def test_closeStrings_2(self):
        self.assertTrue(Solution().closeStrings(word1 = "cabbba", word2 = "abbccc"))

    def test_closeStrings_3(self):
        self.assertFalse(Solution().closeStrings(word1 = "cabbba", word2 = "aabbss"))

    def test_closeStrings_4(self):
        self.assertFalse(Solution().closeStrings("abbzzca", "babzzcz"))
