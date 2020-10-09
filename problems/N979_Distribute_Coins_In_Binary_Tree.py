class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def dfs(node, num):
            if not node:
                return 0
            left = dfs(node.left, num)
            right = dfs(node.right, num)
            num[0] += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root, res)
        return res[0]