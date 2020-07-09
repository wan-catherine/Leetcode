from unittest import TestCase
from problems.Utility_Tree import TreeNode, list_to_tree_node, treenode_to_list, null
from problems.N662_Maximum_Width_Of_Binary_Tree import Solution

class TestSolution(TestCase):
    def test_widthOfBinaryTree(self):
        self.assertEqual(4, Solution().widthOfBinaryTree(list_to_tree_node([1,3,2,5,3,null,9])))

    def test_widthOfBinaryTree_1(self):
        self.assertEqual(2, Solution().widthOfBinaryTree(list_to_tree_node([1,3,null,5,3])))

    def test_widthOfBinaryTree_2(self):
        self.assertEqual(1, Solution().widthOfBinaryTree(list_to_tree_node([1])))

    def test_widthOfBinaryTree_3(self):
        self.assertEqual(8, Solution().widthOfBinaryTree(list_to_tree_node([1,1,1,1,1,1,1,null,null,null,1,null,null,null,null,2,2,2,2,2,2,2,null,2,null,null,2,null,2])))