from unittest import TestCase
from problems.N1191_K_Concatenation_Maximum_Sum import Solution

class TestSolution(TestCase):
    def test_kConcatenationMaxSum(self):
        self.assertEqual(9, Solution().kConcatenationMaxSum(arr = [1,2], k = 3))

    def test_kConcatenationMaxSum_1(self):
        self.assertEqual(2, Solution().kConcatenationMaxSum(arr = [1,-2,1], k = 5))

    def test_kConcatenationMaxSum_2(self):
        self.assertEqual(0, Solution().kConcatenationMaxSum(arr = [-1,-2], k = 7))

    def test_kConcatenationMaxSum_3(self):
        self.assertEqual(1, Solution().kConcatenationMaxSum([1,-1], 1))
