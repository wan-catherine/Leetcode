from unittest import TestCase
from problems.FlattenBinaryTreeLinkedList import TreeNode, Solution

class TestSolution(TestCase):
    def test_flatten(self):
        solution = Solution()
        root = TreeNode(1)
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        solution.flatten(root)

