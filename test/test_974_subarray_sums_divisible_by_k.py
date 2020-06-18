from unittest import TestCase
from problems.N974_Subarray_Sums_Divisible_By_K import Solution

class TestSolution(TestCase):
    def test_subarraysDivByK(self):
        self.assertEqual(7, Solution().subarraysDivByK( A = [4,5,0,-2,-3,1], K = 5))

    def test_subarraysDivByK_1(self):
        self.assertEqual(7, Solution().subarraysDivByK([8,9,7,8,9],8))
