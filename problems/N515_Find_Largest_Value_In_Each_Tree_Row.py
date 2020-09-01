from .Utility_Tree import TreeNode

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            ans = -2**31 -1
            new_stack = []
            for node in stack:
                ans = max(ans, node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            res.append(ans)
            stack = new_stack
        return res