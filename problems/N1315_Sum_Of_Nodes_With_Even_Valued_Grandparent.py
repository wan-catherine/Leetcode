from .Utility_Tree import TreeNode

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, root, res):
        if not root:
            return res
        if not root.val % 2:
            if root.left:
                if root.left.left:
                    res += root.left.left.val
                if root.left.right:
                    res += root.left.right.val
            if root.right:
                if root.right.left:
                    res += root.right.left.val
                if root.right.right:
                    res += root.right.right.val

        res = self.dfs(root.left, res)
        res = self.dfs(root.right, res)
        return res