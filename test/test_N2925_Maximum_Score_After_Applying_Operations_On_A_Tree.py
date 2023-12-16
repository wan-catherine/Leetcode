from unittest import TestCase
from problems.N2925_Maximum_Score_After_Applying_Operations_On_A_Tree import Solution

class TestSolution(TestCase):
    def test_maximum_score_after_operations(self):
        self.assertEquals(11, Solution().maximumScoreAfterOperations(edges = [[0,1],[0,2],[0,3],[2,4],[4,5]], values = [5,2,5,2,1,1]))

    def test_maximum_score_after_operations_1(self):
        self.assertEquals(40, Solution().maximumScoreAfterOperations(edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [20,10,9,7,4,3,5]))
