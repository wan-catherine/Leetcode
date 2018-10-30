# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.helper(0, root)

    def helper(self, hight, root):
        if root.left == None and root.right == None:
            return hight + 1
        if root.left == None:
            return self.helper(hight+1, root.right)
        if root.right == None:
            return self.helper(hight+1, root.left)
        hightL = self.helper(hight+1, root.left)
        hightR = self.helper(hight+1, root.right)
        return hightL if hightL < hightR else hightR