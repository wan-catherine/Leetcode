from unittest import TestCase
from problems.N2926_Maximum_Balanced_Subsequence_Sum import Solution

class TestSolution(TestCase):
    def test_max_balanced_subsequence_sum(self):
        self.assertEquals(14, Solution().maxBalancedSubsequenceSum([3,3,5,6]))

    def test_max_balanced_subsequence_sum_1(self):
        self.assertEquals(13, Solution().maxBalancedSubsequenceSum([5,-1,-3,8]))

    def test_max_balanced_subsequence_sum_2(self):
        self.assertEquals(-1, Solution().maxBalancedSubsequenceSum([-2,-1]))
