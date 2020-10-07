from unittest import TestCase
from problems.N863_All_Nodes_Distance_K_In_Binary_Tree import Solution
from problems.Utility_Tree import list_to_tree_node,null

class TestSolution(TestCase):
    def test_distanceK(self):
        root = list_to_tree_node([3,5,1,6,2,0,8,null,null,7,4])
        self.assertListEqual([7,4,1], Solution().distanceK(root, 5, 2))
