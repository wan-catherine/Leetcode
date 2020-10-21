from unittest import TestCase
from problems.N99_Recover_Binary_Search_Tree import Solution
from problems.Utility_Tree import list_to_tree_node, treenode_to_list, null

class TestSolution(TestCase):
    def test_recoverTree(self):
        root = list_to_tree_node([1,3,null,null,2])
        Solution().recoverTree(root)
        self.assertListEqual([3,1,null,null,2], treenode_to_list(root))

    def test_recoverTree_1(self):
        root = list_to_tree_node([3,1,4,null,null,2])
        Solution().recoverTree(root)
        self.assertListEqual([2,1,4,null,null,3], treenode_to_list(root))

    def test_recoverTree_2(self):
        root = list_to_tree_node([5,3,9,-2147483648,2])
        Solution().recoverTree(root)
        self.assertListEqual([5,2,9,-2147483648,3], treenode_to_list(root))

    def test_recoverTree_3(self):
        root = list_to_tree_node([146,71,-13,55,null,231,399,321,null,null,null,null,null,-33])
        Solution().recoverTree(root)
        self.assertListEqual([146,71,321,55,null,231,399,-13,null,null,null,null,null,-33], treenode_to_list(root))
