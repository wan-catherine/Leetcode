from unittest import TestCase
from problems.N2607_Make_K_Subarray_Sums_Equal import Solution

class TestSolution(TestCase):
    def test_make_sub_ksum_equal(self):
        self.assertEqual(1, Solution().makeSubKSumEqual(arr = [1,4,1,3], k = 2))

    def test_make_sub_ksum_equal_1(self):
        self.assertEqual(5, Solution().makeSubKSumEqual(arr = [2,5,5,7], k = 3))
