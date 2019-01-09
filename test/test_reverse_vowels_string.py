from unittest import TestCase
from problems.ReverseVowelsString import Solution

class TestSolution(TestCase):
    def test_reverseVowels(self):
        solution = Solution()
        res = solution.reverseVowels("hello")
        self.assertEqual("holle", res)

    def test_reverseVowels_one(self):
        solution = Solution()
        res = solution.reverseVowels("leetcode")
        self.assertEqual("leotcede", res)

    def test_reverseVowels_two(self):
        solution = Solution()
        res = solution.reverseVowels("aA")
        self.assertEqual("Aa", res)


