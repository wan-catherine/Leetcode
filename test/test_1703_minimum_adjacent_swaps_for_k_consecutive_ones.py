from unittest import TestCase
from problems.N1703_Minimum_Adjacent_Swaps_For_K_Consecutive_Ones import Solution

class TestSolution(TestCase):
    def test_minMoves(self):
        self.assertEqual(1, Solution().minMoves(nums = [1,0,0,1,0,1], k = 2))

    def test_minMoves_1(self):
        self.assertEqual(5, Solution().minMoves(nums = [1,0,0,0,0,0,1,1], k = 3))

    def test_minMoves_2(self):
        self.assertEqual(0, Solution().minMoves(nums = [1,1,0,1], k = 2))