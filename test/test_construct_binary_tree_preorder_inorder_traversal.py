from unittest import TestCase
from problems.ConstructBinaryTreePreorderInorderTraversal import TreeNode,Solution

class TestSolution(TestCase):
    def test_buildTree(self):
        solution = Solution()
        res = solution.buildTree([3,9,20,15,7], [9,3,15,20,7])
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(res.val, root.val)
        self.assertEqual(res.left.val, root.left.val)
        self.assertEqual(res.right.val, root.right.val)
