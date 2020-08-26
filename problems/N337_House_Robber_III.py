from .Utility_Tree import TreeNode
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        self.memo = {}
        res = self.dp(root)
        return res

    def dp(self, node):
        if not node:
            return 0
        if node in self.memo:
            return self.memo[node]

        rob_val = node.val
        if node.left:
            rob_val += self.dp(node.left.left) + self.dp(node.left.right)
        if node.right:
            rob_val += self.dp(node.right.left) + self.dp(node.right.right)
        not_rob_val = self.dp(node.left) + self.dp(node.right)

        self.memo[node] = max(rob_val, not_rob_val)
        return self.memo[node]

