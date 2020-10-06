from unittest import TestCase
from problems.Utility_Tree import list_to_tree_node, treenode_to_list, null
from problems.N538_Convert_BST_To_Greater_Tree import Solution

class TestSolution(TestCase):
    def test_convertBST(self):
        root = list_to_tree_node([4,1,6,0,2,5,7,null,null,null,3,null,null,null,8])
        self.assertListEqual([30,36,21,36,35,26,15,null,null,null,33,null,null,null,8], treenode_to_list(Solution().convertBST(root)))

    def test_convertBST_1(self):
        root = list_to_tree_node([0,null,1])
        self.assertListEqual([1,null,1], treenode_to_list(Solution().convertBST(root)))

    def test_convertBST_2(self):
        root = list_to_tree_node([1,0,2])
        self.assertListEqual([3,3,2], treenode_to_list(Solution().convertBST(root)))

    def test_convertBST_3(self):
        root = list_to_tree_node([3,2,4,1])
        self.assertListEqual([7,9,4,10], treenode_to_list(Solution().convertBST(root)))