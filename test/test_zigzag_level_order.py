from unittest import TestCase
from problems.BinaryTreeZigzagLevelOrderTraversal import Solution,TreeNode

class TestSolution(TestCase):
    def test_zigzagLevelOrder(self):
        solution = Solution()
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        res = solution.zigzagLevelOrder(root)
        expected = [
  [3],
  [20,9],
  [15,7]
]
        self.assertEqual(res, expected)
