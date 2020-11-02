from unittest import TestCase
from problems.N1638_Count_Substrings_That_Differ_By_One_Character import Solution

class TestSolution(TestCase):
    def test_countSubstrings(self):
        self.assertEqual(6, Solution().countSubstrings(s = "aba", t = "baba"))

    def test_countSubstrings_1(self):
        self.assertEqual(3, Solution().countSubstrings(s = "ab", t = "bb"))

    def test_countSubstrings_2(self):
        self.assertEqual(0, Solution().countSubstrings(s = "a", t = "a"))

    def test_countSubstrings_3(self):
        self.assertEqual(10, Solution().countSubstrings(s = "abe", t = "bbc"))