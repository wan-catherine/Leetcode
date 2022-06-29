from unittest import TestCase
from problems.N2322_Minimum_Score_After_Removals_On_A_Tree import Solution

class TestSolution(TestCase):
    def test_minimum_score(self):
        self.assertEqual(9, Solution().minimumScore(nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]))

    def test_minimum_score_1(self):
        self.assertEqual(0, Solution().minimumScore(nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]))
