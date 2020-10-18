from unittest import TestCase
from problems.N1626_Best_Team_With_No_Conflicts import Solution

class TestSolution(TestCase):
    def test_bestTeamScore(self):
        self.assertEqual(34, Solution().bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))

    def test_bestTeamScore_1(self):
        self.assertEqual(16, Solution().bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))

    def test_bestTeamScore_2(self):
        self.assertEqual(6, Solution().bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))
