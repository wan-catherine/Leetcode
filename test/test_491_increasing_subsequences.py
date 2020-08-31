from unittest import TestCase
from problems.N491_Increasing_Subsequences import Solution

class TestSolution(TestCase):
    def test_findSubsequences(self):
        self.assertListEqual([[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]], Solution().findSubsequences([4, 6, 7, 7]))