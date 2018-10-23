from unittest import TestCase
from problems.BinaryTreeLevelOrderTraversal import TreeNode,Solution

class TestSolution(TestCase):
    def test_levelOrder(self):
        solution = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        res = solution.levelOrder(root)
        expected = [
  [3],
  [9,20],
  [15,7]
]
        self.assertEqual(res, expected)
