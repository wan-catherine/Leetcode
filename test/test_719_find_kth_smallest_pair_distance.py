from unittest import TestCase
from problems.N719_Find_Kth_Smallest_Pair_Distance import Solution

class TestSolution(TestCase):
    def test_smallestDistancePair(self):
        self.assertEqual(0, Solution().smallestDistancePair(nums = [1,3,1], k = 1))

    def test_smallestDistancePair_1(self):
        self.assertEqual(0, Solution().smallestDistancePair([1,1,1], 2))
