# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        self.helper(root, sum, res, temp)
        return res

    def helper(self, root, sum, res, temp):
        if root == None:
            return
        if root.left == None and root.right == None:
            if root.val == sum:
                res.append(temp)
        temp.append(root.val)
        if root.left:
            self.helper(root.left, sum-root.val, res, temp.copy())
        if root.right:
            self.helper(root.right, sum-root.val, res, temp.copy())