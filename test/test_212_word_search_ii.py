from unittest import TestCase
from problems.N212_Word_Search_II import Solution

class TestSolution(TestCase):
    def test_findWords(self):
        board =  [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
        words = ["oath","pea","eat","rain"]
        output = ["oath", "eat"]
        self.assertListEqual(output, Solution().findWords(board, words))

    def test_findWords_1(self):
        board = [["a"]]
        words = ["a"]
        output = ["a"]
        self.assertListEqual(output, Solution().findWords(board, words))

    def test_findWords_2(self):
        board = [["a","a"]]
        words = ["a"]
        output = ["a"]
        self.assertListEqual(output, Solution().findWords(board, words))
