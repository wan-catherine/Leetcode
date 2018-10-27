from unittest import TestCase
from problems.BinaryTreeLevelOrderTraversalII import TreeNode, Solution

class TestSolution(TestCase):
    def test_levelOrderBottom(self):
        solution = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        res = solution.levelOrderBottom(root)
        expected = [
[15,7],
[9, 20],
[3]
]
        self.assertEqual(res, expected)