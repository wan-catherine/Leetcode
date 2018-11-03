from unittest import TestCase
from problems.PopulatingNextRightPointersEachNode import TreeLinkNode, Solution

class TestSolution(TestCase):
    def test_connect(self):
        solution = Solution()
        root = TreeLinkNode(1)
        root.left = TreeLinkNode(2)
        root.left.left = TreeLinkNode(4)
        root.left.right = TreeLinkNode(5)
        root.right = TreeLinkNode(3)
        root.right.left = TreeLinkNode(6)
        root.right.right = TreeLinkNode(7)
        solution.connect(root)
        self.assertEqual(root.left.next, root.right)
        self.assertEqual(root.left.left.next, root.left.right)
        self.assertEqual(root.left.right.next, root.right.left)
        self.assertEqual(root.right.left.next, root.right.right)
