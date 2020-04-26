from unittest import TestCase
from problems.SearchInBinarySearchTree_700 import TreeNode, Solution

class TestSolution(TestCase):
    def test_searchBST(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right = TreeNode(7)
        solution = Solution().searchBST(root, 2)
        self.assertEqual(solution.left.val , 1)
