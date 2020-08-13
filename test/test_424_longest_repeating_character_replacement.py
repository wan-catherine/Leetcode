from unittest import TestCase
from problems.N424_Longest_Repeating_Character_Replacement import Solution

class TestSolution(TestCase):
    def test_characterReplacement(self):
        self.assertEqual(4, Solution().characterReplacement(s = "ABAB", k = 2))

    def test_characterReplacement_1(self):
        self.assertEqual(4, Solution().characterReplacement(s = "AABABBA", k = 1))
