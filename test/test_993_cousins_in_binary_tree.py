from unittest import TestCase
from problems.Utility_Tree import TreeNode,list_to_tree_node, treenode_to_list, null
from problems.N993_Cousins_In_Binary_Tree import Solution

class TestSolution(TestCase):
    def test_isCousins(self):
        root = list_to_tree_node([1,2,3,4])
        self.assertEqual(False, Solution().isCousins(root, 4, 3))

    def test_isCousins_1(self):
        root = list_to_tree_node([1,2,3,null,4,null,5])
        self.assertEqual(True, Solution().isCousins(root, 5, 4))

    def test_isCousins_2(self):
        root = list_to_tree_node([1,2,3,null,4])
        self.assertEqual(False, Solution().isCousins(root, 2, 3))
