from unittest import TestCase
from problems.N3372_Maximize_The_Number_Of_Target_Nodes_After_Connecting_Trees_I import Solution

class TestSolution(TestCase):
    def test_max_target_nodes(self):
        self.assertListEqual([9,7,9,8,8], Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2))

    def test_max_target_nodes_1(self):
        self.assertListEqual([6,3,3,3,3], Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1))

    def test_max_target_nodes_2(self):
        self.assertListEqual([15,15,15,15,15,15,15,15,15], Solution().maxTargetNodes(edges1 = [[5,2],[3,4],[7,3],[1,5],[0,1],[6,0],[6,7],[6,8]], edges2 = [[5,0],[2,4],[3,2],[1,3],[1,5]], k = 8))
