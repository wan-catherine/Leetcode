from unittest import TestCase
from problems.PathSum import TreeNode, Solution

class TestSolution(TestCase):
    def test_hasPathSum(self):
        solution = Solution()
        root = TreeNode(5)
        root.left=TreeNode(4)
        root.right=TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left=TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left=TreeNode(13)
        root.right.right=TreeNode(4)
        root.right.right.right=TreeNode(1)
        res = solution.hasPathSum(root, 22)
        self.assertEqual(True, res)

    def test_hasPathSum_one(self):
        solution = Solution()
        root = TreeNode(1)
        root.left=TreeNode(2)
        res = solution.hasPathSum(root, 1)
        self.assertEqual(False, res)
