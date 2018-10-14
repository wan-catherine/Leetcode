from unittest import TestCase
from problems.ScrambleString import Solution

class TestSolution(TestCase):
    def test_isScramble(self):
        solution = Solution()
        res = solution.isScramble("great","rgtae")
        self.assertEqual(True, res)

    def test_isScramble_one(self):
        solution = Solution()
        res = solution.isScramble("abcde","caebd")
        self.assertEqual(False, res)

    def test_isScramble_two(self):
        solution = Solution()
        res = solution.isScramble("abc","bca")
        self.assertEqual(True, res)

    def test_isScramble_long(self):
        solution = Solution()
        res = solution.isScramble("abcdefghijklmnopq", "efghijklmnopqcadb")
        self.assertEqual(False, res)

    def test_isScramble_long(self):
        solution = Solution()
        res = solution.isScramble("xstjzkfpkggnhjzkpfjoguxvkbuopi", "xbouipkvxugojfpkzjhnggkpfkzjts")
        self.assertEqual(True, res)

