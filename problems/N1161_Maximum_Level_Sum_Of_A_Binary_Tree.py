class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = root.val
        ans = 1
        level = 0
        stack = [root]
        while stack:
            new_stack = []
            val = 0
            for node in stack:
                val += node.val
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            level += 1
            if val > res:
                res = val
                ans = level
            stack = new_stack

        return ans
