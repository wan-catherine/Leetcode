# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers_before(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return self.dfs(root, 0, 0)

    def dfs_before(self, root, num, res):
        num = num * 10 + root.val
        if root.left == None and root.right == None:
            return num + res

        if root.left != None:
            res = self.dfs(root.left, num, res)
        if root.right != None:
            res = self.dfs(root.right, num, res)
        return res

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return  0
        return self.dfs(root, 0, [])

    def dfs(self, root, res, nums):
        if root.left:
            res = self.dfs(root.left, res, nums + [str(root.val)])
        if root.right:
            res = self.dfs(root.right, res, nums + [str(root.val)])
        if not root.right and not root.left:
            res += int(''.join(nums + [str(root.val)]))

        return res

