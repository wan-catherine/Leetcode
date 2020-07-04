from unittest import TestCase
from problems.N1425_Constrained_Subsequence_Sum import Solution

class TestSolution(TestCase):
    def test_constrainedSubsetSum(self):
        nums = [10, 2, -10, 5, 20]
        k = 2
        self.assertEqual(37, Solution().constrainedSubsetSum(nums,k))

    def test_constrainedSubsetSum_1(self):
        nums = [-1,-2,-3]
        k = 1
        self.assertEqual(-1, Solution().constrainedSubsetSum(nums,k))

    def test_constrainedSubsetSum_2(self):
        nums = [10,-2,-10,-5,20]
        k = 2
        self.assertEqual(23, Solution().constrainedSubsetSum(nums,k))

    def test_constrainedSubsetSum_3(self):
        nums = [-5266,4019,7336,-3681,-5767]
        k = 2
        self.assertEqual(11355, Solution().constrainedSubsetSum(nums,k))
