from unittest import TestCase
from problems.N1004_Max_Consecutive_Ones_III import Solution

class TestSolution(TestCase):
    def test_longestOnes(self):
        self.assertEqual(6, Solution().longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], K = 2))

    def test_longestOnes_1(self):
        self.assertEqual(10, Solution().longestOnes(A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3))

    def test_longestOnes_2(self):
        self.assertEqual(4, Solution().longestOnes(A = [0,0,0,1], K = 4))

