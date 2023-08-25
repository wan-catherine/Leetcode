from unittest import TestCase
from problems.N2818_Apply_Operations_To_Maximize_Score import Solution

class TestSolution(TestCase):
    def test_maximum_score(self):
        self.assertEquals(81, Solution().maximumScore(nums = [8,3,9,3,8], k = 2))

    def test_maximum_score_1(self):
        self.assertEquals(4788, Solution().maximumScore(nums = [19,12,14,6,10,18], k = 3))

    def test_maximum_score_2(self):
        self.assertEquals(630596200, Solution().maximumScore([6,1,13,10,1,17,6], 27))
