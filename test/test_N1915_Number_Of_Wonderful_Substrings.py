from unittest import TestCase
from problems.N1915_Number_Of_Wonderful_Substrings import Solution

class TestSolution(TestCase):
    def test_wonderful_substrings(self):
        self.assertEqual(4, Solution().wonderfulSubstrings("aba"))

    def test_wonderful_substrings_1(self):
        self.assertEqual(9, Solution().wonderfulSubstrings("aabb"))

    def test_wonderful_substrings_2(self):
        self.assertEqual(2, Solution().wonderfulSubstrings("he"))
