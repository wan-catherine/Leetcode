from unittest import TestCase
from problems.N2407_Longest_Increasing_Subsequence_II import Solution

class TestSolution(TestCase):
    def test_length_of_lis(self):
        self.assertEqual(5, Solution().lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3))

    def test_length_of_lis_1(self):
        self.assertEqual(4, Solution().lengthOfLIS(nums = [7,4,5,1,8,12,4,7], k = 5))

    def test_length_of_lis_2(self):
        self.assertEqual(1, Solution().lengthOfLIS(nums = [1,5], k = 1))