from unittest import TestCase
from problems.N1186_Maximum_Subarray_Sum_With_One_Deletion import Solution

class TestSolution(TestCase):
    def test_maximumSum(self):
        self.assertEqual(4, Solution().maximumSum([1,-2,0,3]))

    def test_maximumSum_1(self):
        self.assertEqual(3, Solution().maximumSum([1,-2,-2,3]))

    def test_maximumSum_2(self):
        self.assertEqual(-1, Solution().maximumSum([-1,-1,-1,-1]))
