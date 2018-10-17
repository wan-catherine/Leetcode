from unittest import TestCase
from problems.BinaryTreeInorderTraversal import Solution, TreeNode

class TestSolution(TestCase):
    def test_inorderTraversal(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = None
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        root.right.right = None
        res = solution.inorderTraversal(root)
        self.assertEqual([1,3,2], res)
