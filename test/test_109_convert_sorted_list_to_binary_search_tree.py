from unittest import TestCase
from problems.ConvertSortedListBinarySearchTree import Solution
from problems.Utility_Tree import TreeNode, treenode_to_list, null
from problems.Utility import create_linklist_from_list

class TestSolution(TestCase):
    def test_sortedListToBST(self):
        head = create_linklist_from_list([-10,-3,0,5,9])
        self.assertListEqual([0,-3,9,-10,null,5], treenode_to_list(Solution().sortedListToBST(head)))