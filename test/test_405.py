from unittest import TestCase
from problems.DeleteNodeInBST_450 import TreeNode, Solution

class TestSolution(TestCase):
    def test_deleteNode(self):
        root = TreeNode(5)
        root.right = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)

        solution = Solution().deleteNode(root, 3)
        self.assertEqual(solution.left.val, 4)

    def tes_by_only_one_node(self):
        root = TreeNode(0)
        solution = Solution().deleteNode(root, 0)
        self.assertEqual(solution, None)

    def test_by_two(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        solution = Solution().deleteNode(root, 1)
        self.assertEqual(solution.val , 2)

    def test_by_three(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        solution = Solution().deleteNode(root, 2)
        self.assertEqual(solution.val , 1)

    def test_by_four(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        solution = Solution().deleteNode(root, 2)
        self.assertEqual(solution.val , 1)
