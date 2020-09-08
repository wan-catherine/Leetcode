from unittest import TestCase
from problems.N300_Longest_Increasing_Subsequence import Solution

class TestSolution(TestCase):
    def test_lengthOfLIS(self):
        self.assertEqual(4, Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))

    def test_lengthOfLIS_1(self):
        self.assertEqual(1, Solution().lengthOfLIS([2,2]))

    def test_lengthOfLIS_2(self):
        self.assertEqual(6, Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))