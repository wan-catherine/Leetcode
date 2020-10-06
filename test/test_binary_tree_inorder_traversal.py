from unittest import TestCase
from problems.BinaryTreeInorderTraversal import Solution
from problems.Utility_Tree import list_to_tree_node, null

class TestSolution(TestCase):
    def test_inorderTraversal(self):
        self.assertListEqual([1,3,2], Solution().inorderTraversal(list_to_tree_node([1,null,2,3])))
