from unittest import TestCase
from problems.N2049_Count_Nodes_With_The_Highest_Score import Solution

class TestSolution(TestCase):
    def test_count_highest_score_nodes(self):
        self.assertEqual(3, Solution().countHighestScoreNodes([-1,2,0,2,0]))

    def test_count_highest_score_nodes_1(self):
        self.assertEqual(2, Solution().countHighestScoreNodes([-1,2,0]))
