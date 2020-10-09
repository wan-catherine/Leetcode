from unittest import TestCase
from problems.N834_Sum_Of_Distances_In_Tree import Solution

class TestSolution(TestCase):
    def test_sumOfDistancesInTree(self):
        self.assertListEqual([8,12,6,10,10,10], Solution().sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))