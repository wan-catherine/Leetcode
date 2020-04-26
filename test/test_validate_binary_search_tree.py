from unittest import TestCase
from problems.ValidateBinarySearchTree import Solution, TreeNode

class TestSolution(TestCase):
    def test_isValidBST(self):
        solution = Solution()
        root = TreeNode(2)
        root.right = TreeNode(3)
        root.left = TreeNode(1)
        res = solution.isValidBST_20200426(root)
        self.assertEqual(True, res)

    def test_isValidBST_one(self):
        solution = Solution()
        root = TreeNode(1)
        root.right = TreeNode(1)
        res = solution.isValidBST_20200426(root)
        self.assertEqual(False, res)
