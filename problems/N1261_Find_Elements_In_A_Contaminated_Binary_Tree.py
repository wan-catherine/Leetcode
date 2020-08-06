import bisect

from problems.Utility_Tree import TreeNode


class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.elements = set()
        self.recover(root, 0)

    def recover(self, node, val):
        if not node:
            return
        node.val = val
        self.elements.add(val)
        if node.left:
            self.recover(node.left, 2*val + 1)
        if node.right:
            self.recover(node.right, 2*val + 2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.elements
