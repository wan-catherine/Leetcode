# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return self.dfs(root, 0, 0)

    def dfs(self, root, num, res):
        num = num * 10 + root.val
        if root.left == None and root.right == None:
            return num + res

        if root.left != None:
            res = self.dfs(root.left, num, res)
        if root.right != None:
            res = self.dfs(root.right, num, res)
        return res


