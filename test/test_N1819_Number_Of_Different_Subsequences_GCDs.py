from unittest import TestCase
from problems.N1819_Number_Of_Different_Subsequences_GCDs import Solution

class TestSolution(TestCase):
    def test_count_different_subsequence_gcds(self):
        self.assertEqual(5, Solution().countDifferentSubsequenceGCDs([6,10,3]))

    def test_count_different_subsequence_gcds_1(self):
        self.assertEqual(7, Solution().countDifferentSubsequenceGCDs([5,15,40,5,6]))
