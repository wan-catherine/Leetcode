from unittest import TestCase
from problems.Utility_Tree import TreeNode, list_to_tree_node, null
from problems.N501_Find_Mode_In_Binary_Search_Tree import Solution

class TestSolution(TestCase):
    def test_findMode(self):
        root = list_to_tree_node([1, null, 2])
        self.assertListEqual([1,2], Solution().findMode(root))

    def test_findMode_1(self):
        root = list_to_tree_node([1,null,2,2])
        self.assertListEqual([2], Solution().findMode(root))
