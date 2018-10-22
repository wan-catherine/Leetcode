# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)

    def helper(self, node):
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 1

        nleft = self.helper(node.left)
        nright = self.helper(node.right)

        nsubTree = nleft if nleft > nright else nright
        return nsubTree + 1