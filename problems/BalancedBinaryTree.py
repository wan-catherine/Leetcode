# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.helper(0, root) >= 0

    def helper(self, hight, root):
        if not root:
            return hight

        l = self.helper(hight + 1, root.left)
        r = self.helper(hight + 1, root.right)

        if abs(l-r) > 1 or l == -1 or r == -1:
            return -1
        return max(l, r)
