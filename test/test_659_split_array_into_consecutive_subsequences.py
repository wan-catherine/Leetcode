from unittest import TestCase
from problems.N659_Split_Array_Into_Consecutive_Subsequences import Solution

class TestSolution(TestCase):
    def test_isPossible(self):
        self.assertTrue(Solution().isPossible([1,2,3,3,4,5]))

    def test_isPossible_1(self):
        self.assertTrue(Solution().isPossible([1,2,3,3,4,4,5,5]))

    def test_isPossible_2(self):
        self.assertFalse(Solution().isPossible([1,2,3,4,4,5]))

    def test_isPossible_3(self):
        self.assertTrue(Solution().isPossible([1,2,3,4,6,7,8,9,10,11]))
