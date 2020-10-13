class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def dfs(node, cur):
            if not node:
                return cur, node
            if not node.left and not node.right:
                val = cur + node.val
                if val < limit:
                    return val, None
                return val, node

            left, right, val = None, None, None
            if node.left:
                left, ln = dfs(node.left, cur+node.val)
                node.left = ln
                val = left
            if node.right:
                right, rn = dfs(node.right, cur+node.val)
                node.right = rn
                val = right if not val else max(val, right)
            if (left and right and left < limit and right < limit) or (left and left < limit and not right) or (right and right < limit and not left):
                return val, None
            return val, node

        return dfs(root, 0)[1]