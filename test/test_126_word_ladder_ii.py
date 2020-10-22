from unittest import TestCase
from problems.N126_Word_Ladder_II import Solution

class TestSolution(TestCase):
    def test_findLadders(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        output = [
            ["hit", "hot", "lot", "log", "cog"],
  ["hit","hot","dot","dog","cog"]

]
        self.assertListEqual(output, Solution().findLadders(beginWord, endWord, wordList))

    def test_findLadders_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        output = []
        self.assertListEqual(output, Solution().findLadders(beginWord, endWord, wordList))
