# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, l, r):
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False
        if l.val != r.val:
            return False
        if self.helper(l.right,r.left) and self.helper(l.left, r.right):
            return True
        else:
            return False