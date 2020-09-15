from unittest import TestCase
from problems.N673_Number_Of_Longest_Increasing_Subsequence import Solution

class TestSolution(TestCase):
    def test_findNumberOfLIS(self):
        self.assertEqual(2, Solution().findNumberOfLIS([1,3,5,4,7]))

    def test_findNumberOfLIS_1(self):
        self.assertEqual(5, Solution().findNumberOfLIS([2,2,2,2,2]))

    def test_findNumberOfLIS_2(self):
        self.assertEqual(3, Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))

    def test_findNumberOfLIS_3(self):
        self.assertEqual(0, Solution().findNumberOfLIS([]))

    def test_findNumberOfLIS_4(self):
        self.assertEqual(27, Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3]))
