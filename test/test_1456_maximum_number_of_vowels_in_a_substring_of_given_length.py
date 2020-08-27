from unittest import TestCase
from problems.N1456_Maximum_Number_Of_Vowels_In_A_Substring_Of_Given_Length import Solution

class TestSolution(TestCase):
    def test_maxVowels(self):
        self.assertEqual(3, Solution().maxVowels(s = "abciiidef", k = 3))

    def test_maxVowels_1(self):
        self.assertEqual(2, Solution().maxVowels(s = "aeiou", k = 2))

    def test_maxVowels_2(self):
        self.assertEqual(2, Solution().maxVowels(s = "leetcode", k = 3))

    def test_maxVowels_3(self):
        self.assertEqual(0, Solution().maxVowels(s = "rhythms", k = 4))

    def test_maxVowels_4(self):
        self.assertEqual(1, Solution().maxVowels(s = "tryhard", k = 4))
