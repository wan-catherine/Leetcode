from unittest import TestCase
from problems.N3306_Count_Of_Substrings_Containing_Every_Vowel_And_K_Consonants_II import Solution

class TestSolution(TestCase):
    def test_count_of_substrings(self):
        self.assertEquals(0, Solution().countOfSubstrings(word = "aeioqq", k = 1))

    def test_count_of_substrings_1(self):
        self.assertEquals(1, Solution().countOfSubstrings(word = "aeiou", k = 0))

    def test_count_of_substrings_2(self):
        self.assertEquals(3, Solution().countOfSubstrings(word = "ieaouqqieaouqq", k = 1))
