from unittest import TestCase
from problems.N1803_Count_Pairs_With_XOR_In_A_Range import Solution

class TestSolution(TestCase):
    def test_count_pairs(self):
        self.assertEqual(6, Solution().countPairs(nums = [1,4,2,7], low = 2, high = 6))

    def test_count_pairs_1(self):
        self.assertEqual(8, Solution().countPairs([9,8,4,2,1], low = 5, high = 14))


