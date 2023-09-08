from unittest import TestCase
from problems.N2786_Visit_Array_Positiions_To_Maximize_Score import Solution

class TestSolution(TestCase):
    def test_max_score(self):
        self.assertEquals(13, Solution().maxScore(nums = [2,3,6,1,9,2], x = 5))

    def test_max_score_1(self):
        self.assertEquals(20, Solution().maxScore(nums = [2,4,6,8], x = 3))
