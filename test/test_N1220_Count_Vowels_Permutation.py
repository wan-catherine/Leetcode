from unittest import TestCase
from problems.N1220_Count_Vowels_Permutation import Solution

class TestSolution(TestCase):
    def test_count_vowel_permutation(self):
        self.assertEqual(5, Solution().countVowelPermutation(1))

    def test_count_vowel_permutation_1(self):
        self.assertEqual(10, Solution().countVowelPermutation(2))

    def test_count_vowel_permutation_2(self):
        self.assertEqual(68, Solution().countVowelPermutation(5))
