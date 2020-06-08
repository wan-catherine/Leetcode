from unittest import TestCase
from problems.N560_Subarray_Sum_Equals_K import Solution

class TestSolution(TestCase):
    def test_subarraySum(self):
        self.assertEqual(2, Solution().subarraySum([1,1,1], 2))

    def test_subarraySum_1(self):
        self.assertEqual(4, Solution().subarraySum([1,2,1,2,1], 3))

    def test_subarraySum_2(self):
        self.assertEqual(0, Solution().subarraySum([1], 0))
