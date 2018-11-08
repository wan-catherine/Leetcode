from unittest import TestCase
from problems.PopulatingNextRightPointersEachNodeII import Solution, TreeLinkNode

class TestSolution(TestCase):
    def test_connect(self):
        root = TreeLinkNode(1)
        root.left = TreeLinkNode(2)
        solution = Solution()
        solution.connect(root)

