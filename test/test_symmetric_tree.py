from unittest import TestCase
from problems.SymmetricTree import TreeNode, Solution

class TestSolution(TestCase):
    def test_isSymmetric(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(2)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        res = solution.isSymmetric(root)
        self.assertEqual(res, True)

    def test_isSymmetric_one(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        res = solution.isSymmetric(root)
        self.assertEqual(res, False)

