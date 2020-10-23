from unittest import TestCase
from problems.N1382_Balance_A_Binary_Search_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, treenode_to_list, null

class TestSolution(TestCase):
    def test_balanceBST(self):
        root = list_to_tree_node([1,null,2,null,3,null,4,null,null])
        self.assertListEqual([2,1,3,null,null,null,4], treenode_to_list(Solution().balanceBST(root)))

    def test_balanceBST_1(self):
        root = list_to_tree_node([14,9,16,2,13])
        self.assertListEqual([13,2,14,null,9,null,16], treenode_to_list(Solution().balanceBST(root)))