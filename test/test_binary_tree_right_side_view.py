from unittest import TestCase
from problems.BinaryTreeRightSideView import Solution, TreeNode

class TestSolution(TestCase):
    def test_rightSideView(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)
        res = solution.rightSideView(root)
        self.assertEqual(res, [1, 3, 4])
