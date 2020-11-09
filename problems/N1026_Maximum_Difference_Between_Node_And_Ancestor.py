import sys


class Solution(object):
    def maxAncestorDiff_before(self, root):
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

    def maxAncestorDiff(self, root) -> int:
        res = 0

        def helper(node):
            nonlocal res
            lmin, lmax, rmin, rmax = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize
            if not node:
                return (lmin, lmax)
            if not node.right and not node.left:
                return (node.val, node.val)
            else:
                lmin, lmax = helper(node.left)
                rmin, rmax = helper(node.right)
                m = abs(node.val - min(lmin, rmin))
                n = abs(node.val - max(lmax, rmax))
                res = max(res, m, n)

                return (min(lmin, rmin, node.val), max(lmax, rmax, node.val))

        helper(root)
        return res



