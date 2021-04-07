from unittest import TestCase
from problems.N940_Distinct_Subsequences_II import Solution

class TestSolution(TestCase):
    def test_distinct_subseq_ii(self):
        self.assertEqual(7, Solution().distinctSubseqII("abc"))

    def test_distinct_subseq_ii_1(self):
        self.assertEqual(6, Solution().distinctSubseqII("aba"))

    def test_distinct_subseq_ii_2(self):
        self.assertEqual(3, Solution().distinctSubseqII("aaa"))