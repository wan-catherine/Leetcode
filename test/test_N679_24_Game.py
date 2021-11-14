from unittest import TestCase
from problems.N679_24_Game import Solution

class TestSolution(TestCase):
    def test_judge_point24(self):
        self.assertTrue(Solution().judgePoint24([4,1,8,7]))

    def test_judge_point24_1(self):
        self.assertFalse(Solution().judgePoint24([1,2,1,2]))

    def test_judge_point24_2(self):
        self.assertTrue(Solution().judgePoint24([3,3,8,8]))