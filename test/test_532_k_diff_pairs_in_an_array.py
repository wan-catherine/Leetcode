from unittest import TestCase
from problems.N532_K_Diff_Pairs_In_An_Array import Solution

class TestSolution(TestCase):
    def test_findPairs(self):
        self.assertEqual(2, Solution().findPairs(nums = [3,1,4,1,5], k = 2))

    def test_findPairs_1(self):
        self.assertEqual(4, Solution().findPairs(nums = [1,2,3,4,5], k = 1))

    def test_findPairs_2(self):
        self.assertEqual(1, Solution().findPairs(nums = [1,3,1,5,4], k = 0))

    def test_findPairs_3(self):
        self.assertEqual(2, Solution().findPairs(nums = [1,2,4,4,3,3,0,9,2,3], k = 3))

    def test_findPairs_4(self):
        self.assertEqual(2, Solution().findPairs(nums = [-1,-2,-3], k = 1))
