from unittest import TestCase
from problems.MaximumDepthBinaryTree import Solution, TreeNode

class TestSolution(TestCase):
    def test_max_depth(self):
        vals = [3,9,20, None, None, 15, 7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        res = Solution().maxDepth(root)
        self.assertEqual(3, res)
