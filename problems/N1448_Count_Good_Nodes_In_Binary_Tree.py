class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def dfs(node, maximum):
            nonlocal res
            if not node:
                return
            if node.val >= maximum:
                res += 1
                maximum = node.val
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, root.val)
        return res