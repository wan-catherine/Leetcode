from unittest import TestCase
from problems.N3373_Maximize_The_Number_Of_Target_Nodes_After_Connecting_Trees_II import Solution

class TestSolution(TestCase):
    def test_max_target_nodes(self):
        self.assertListEqual([8,7,7,8,8], Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))

    def test_max_target_nodes_1(self):
        self.assertListEqual([3,6,6,6,6], Solution().maxTargetNodes(edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]]))
