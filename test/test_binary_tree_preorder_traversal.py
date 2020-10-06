from unittest import TestCase
from problems.BinaryTreePreorderTraversal import Solution, TreeNode
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_preorderTraversal(self):
        self.assertListEqual([1,2,3], Solution().preorderTraversal(list_to_tree_node([1,null,2,3])))

    def test_preorderTraversal_1(self):
        self.assertListEqual([3,1,2], Solution().preorderTraversal(list_to_tree_node([3,1,2])))

    def test_preorderTraversal_2(self):
        self.assertListEqual([1,4,2,3], Solution().preorderTraversal(list_to_tree_node([1,4,3,2])))
