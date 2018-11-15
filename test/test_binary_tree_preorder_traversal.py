from unittest import TestCase
from problems.BinaryTreePreorderTraversal import Solution, TreeNode

class TestSolution(TestCase):
    def test_preorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        solution = Solution()
        res = solution.preorderTraversal(root)
        self.assertEqual([1,2,3], res)
