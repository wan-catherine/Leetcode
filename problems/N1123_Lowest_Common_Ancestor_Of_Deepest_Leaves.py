class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, current):
            if not node:
                return current - 1, node

            left, l_node = dfs(node.left, current + 1)
            right, r_node = dfs(node.right, current + 1)
            if left == right:
                return left, node
            if left > right:
                return left, l_node
            if left < right:
                return right, r_node

        height, node = dfs(root, 0)
        return node