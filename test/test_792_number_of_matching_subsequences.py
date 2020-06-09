from unittest import TestCase
from problems.N792_Number_Of_Matching_Subsequences import Solution

class TestSolution(TestCase):
    def test_numMatchingSubseq(self):
        S = "abcde"
        words = ["a", "bb", "acd", "ace"]
        self.assertEqual(3, Solution().numMatchingSubseq(S, words))

    def test_numMatchingSubseq_1(self):
        S = "dsahjpjauf"
        words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
        self.assertEqual(2, Solution().numMatchingSubseq(S, words))
