from unittest import TestCase
from problems.N1027_Longest_Arithmetic_Subsequence import Solution

class TestSolution(TestCase):
    def test_longestArithSeqLength(self):
        self.assertEqual(4, Solution().longestArithSeqLength([3,6,9,12]))

    def test_longestArithSeqLength_1(self):
        self.assertEqual(3, Solution().longestArithSeqLength([9,4,7,2,10]))

    def test_longestArithSeqLength_2(self):
        self.assertEqual(4, Solution().longestArithSeqLength([20,1,15,3,10,5,8]))