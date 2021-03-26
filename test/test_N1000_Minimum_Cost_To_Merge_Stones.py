from unittest import TestCase
from problems.N1000_Minimum_Cost_To_Merge_Stones import Solution

class TestSolution(TestCase):
    def test_merge_stones(self):
        self.assertEqual(20, Solution().mergeStones(stones = [3,2,4,1], K = 2))

    def test_merge_stones_1(self):
        self.assertEqual(-1, Solution().mergeStones(stones = [3,2,4,1], K = 3))

    def test_merge_stones_2(self):
        self.assertEqual(25, Solution().mergeStones(stones = [3,5,1,2,6], K = 3))

