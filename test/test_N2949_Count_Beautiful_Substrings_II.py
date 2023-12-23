from unittest import TestCase
from problems.N2949_Count_Beautiful_Substrings_II import Solution

class TestSolution(TestCase):
    def test_beautiful_substrings(self):
        self.assertEquals(2, Solution().beautifulSubstrings(s = "baeyh", k = 2))

    def test_beautiful_substrings_1(self):
        self.assertEquals(3, Solution().beautifulSubstrings(s = "abba", k = 1))

    def test_beautiful_substrings_2(self):
        self.assertEquals(0, Solution().beautifulSubstrings(s = "bcdf", k = 1))
