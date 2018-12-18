from unittest import TestCase
from problems.CountCompleteTreeNodes import Solution, TreeNode

class TestSolution(TestCase):
    def test_countNodes(self):
        solution = Solution()
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        res = solution.countNodes(root)
        self.assertEqual(6, res)
