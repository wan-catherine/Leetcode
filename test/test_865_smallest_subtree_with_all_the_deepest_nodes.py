from unittest import TestCase
from problems.N865_Smallest_Subtree_With_All_The_Deepest_Nodes import Solution
from problems.Utility_Tree import list_to_tree_node, null, treenode_to_list

class TestSolution(TestCase):
    def test_subtreeWithAllDeepest(self):
        root = list_to_tree_node([3,5,1,6,2,0,8,null,null,7,4])
        self.assertListEqual([2,7,4], treenode_to_list(Solution().subtreeWithAllDeepest(root)))

    def test_subtreeWithAllDeepest_1(self):
        root = list_to_tree_node([1])
        self.assertListEqual([1], treenode_to_list(Solution().subtreeWithAllDeepest(root)))

    def test_subtreeWithAllDeepest_2(self):
        root = list_to_tree_node([0,1,3,null,2])
        self.assertListEqual([2], treenode_to_list(Solution().subtreeWithAllDeepest(root)))

    def test_subtreeWithAllDeepest_3(self):
        root = list_to_tree_node([0,3,1,4,null,2,null,null,6,null,5])
        self.assertListEqual([0,3,1,4,null,2,null,null,6,null,5], treenode_to_list(Solution().subtreeWithAllDeepest(root)))
