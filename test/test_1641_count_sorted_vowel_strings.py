from unittest import TestCase
from problems.N1641_Count_Sorted_Vowel_Strings import Solution

class TestSolution(TestCase):
    def test_countVowelStrings(self):
        self.assertEqual(5, Solution().countVowelStrings(1))

    def test_countVowelStrings_1(self):
        self.assertEqual(15, Solution().countVowelStrings(2))

    def test_countVowelStrings_2(self):
        self.assertEqual(66045, Solution().countVowelStrings(33))
