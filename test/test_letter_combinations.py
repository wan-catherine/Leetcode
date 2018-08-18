from unittest import TestCase
from problems.LetterCombinationsPhoneNumber import Solution

class TestSolution(TestCase):
    def test_letterCombinations_with_two(self):
        solution = Solution()
        res = solution.letterCombinations("23")
        self.assertEqual(sorted(res), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_letterCombinations_empty(self):
        solution = Solution()
        res = solution.letterCombinations("")
        self.assertEqual(sorted(res), [])

    def test_letterCombinations_one(self):
        solution = Solution()
        res = solution.letterCombinations("2")
        self.assertEqual(sorted(res), ["a","b","c"])

    def test_letterCombinations_22(self):
        solution = Solution()
        res = solution.letterCombinations("22")
        self.assertEqual(sorted(res), ["aa","ab","ac","ba","bb","bc","ca","cb","cc"])
