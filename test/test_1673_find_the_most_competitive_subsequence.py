from unittest import TestCase
from problems.N1673_Find_The_Most_Competitive_Subsequence import Solution

class TestSolution(TestCase):
    def test_mostCompetitive(self):
        self.assertListEqual([2,6], Solution().mostCompetitive(nums = [3,5,2,6], k = 2))

    def test_mostCompetitive_1(self):
        self.assertListEqual([2,3,3,4], Solution().mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4))
