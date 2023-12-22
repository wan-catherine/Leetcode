from unittest import TestCase
from problems.N2953_Count_Complete_Substrings import Solution
class TestSolution(TestCase):
    def test_count_complete_substrings(self):
        self.assertEquals(3, Solution().countCompleteSubstrings(word = "igigee", k = 2))

    def test_count_complete_substrings_1(self):
        self.assertEquals(6, Solution().countCompleteSubstrings(word = "aaabbbccc", k = 3))
