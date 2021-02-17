from unittest import TestCase
from problems.N995_Minimum_Number_Of_K_Consecutive_Bit_Flips import Solution

class TestSolution(TestCase):
    def test_minKBitFlips(self):
        self.assertEqual(2, Solution().minKBitFlips(A = [0,1,0], K = 1))

    def test_minKBitFlips_1(self):
        self.assertEqual(-1, Solution().minKBitFlips(A = [1,1,0], K = 2))

    def test_minKBitFlips_2(self):
        self.assertEqual(3, Solution().minKBitFlips(A = [0,0,0,1,0,1,1,0], K = 3))
