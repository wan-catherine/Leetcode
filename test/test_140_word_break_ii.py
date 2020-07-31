from unittest import TestCase
from problems.N140_Word_Break_II import Solution

class TestSolution(TestCase):
    def test_wordBreak(self):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        output = [
  "cats and dog",
  "cat sand dog"
]
        self.assertListEqual(output, Solution().wordBreak(s, wordDict))

    def test_wordBreak_1(self):
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        output = [
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple"
        ]
        self.assertListEqual(output, Solution().wordBreak(s, wordDict))

    def test_wordBreak_2(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        output = []
        self.assertListEqual(output, Solution().wordBreak(s, wordDict))
