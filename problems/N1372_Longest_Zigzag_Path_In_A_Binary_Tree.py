from .Utility_Tree import TreeNode


class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        def dfs(root, direction, step):
            nonlocal res
            if not root:
                return

            if direction == "l":
                dfs(root.right, 'r', step+1) # previous direciton is left, then it's right node + 1
                dfs(root.left, 'l', 1) # or count start from 1, root.left
            else:
                dfs(root.left, 'l', step + 1)
                dfs(root.right, 'r', 1)
            res = max(res, step)

        dfs(root, 'l', 0)  # previous direction .
        dfs(root, 'r', 0)
        return res
