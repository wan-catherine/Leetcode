from unittest import TestCase
from problems.BinaryTreePostorderTraversal import TreeNode, Solution

class TestSolution(TestCase):
    def test_postorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        solution = Solution()
        res = solution.postorderTraversal(root)
        self.assertEqual([3,2,1], res)
