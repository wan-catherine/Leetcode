class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}
        res = 0
        def dfs(node):
            nonlocal  res
            if node in memo:

                return memo[node]
            n_min, n_max = node.val, node.val
            if node.left:
                l_min, l_max = dfs(node.left)
                n_min = min(n_min, l_min)
                n_max = max(n_max, l_max)
            if node.right:
                r_min, r_max = dfs(node.right)
                n_min = min(n_min, r_min)
                n_max = max(n_max, r_max)
            memo[node] = (n_min, n_max)
            res = max(res, abs(n_max - node.val), abs(node.val - n_min))
            return memo[node]
        dfs(root)
        return res




