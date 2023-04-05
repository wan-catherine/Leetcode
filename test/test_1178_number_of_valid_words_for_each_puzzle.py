from unittest import TestCase
from problems.N1178_Number_Of_Valid_Words_For_Each_Puzzle import Solution

class TestSolution(TestCase):
    def test_findNumOfValidWords(self):
        words = ["aaaa", "asas", "able", "ability", "actt", "actor", "access"]
        puzzles = ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]
        self.assertListEqual([1,1,3,2,4,0], Solution().findNumOfValidWords(words, puzzles))
