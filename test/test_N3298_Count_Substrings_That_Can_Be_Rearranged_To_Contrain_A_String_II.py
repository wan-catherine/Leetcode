from unittest import TestCase
from problems.N3298_Count_Substrings_That_Can_Be_Rearranged_To_Contrain_A_String_II import Solution

class TestSolution(TestCase):
    def test_valid_substring_count(self):
        self.assertEquals(1, Solution().validSubstringCount(word1 = "bcca", word2 = "abc"))

    def test_valid_substring_count_2(self):
        self.assertEquals(10, Solution().validSubstringCount(word1 = "abcabc", word2 = "abc"))

    def test_valid_substring_count_3(self):
        self.assertEquals(0, Solution().validSubstringCount(word1 = "abcabc", word2 = "aaabc"))
