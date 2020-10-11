import collections


class Solution(object):
    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def dfs(node, current):
            nonlocal res
            if not node:
                return
            current.append(node.val)
            if not node.left and not node.right:
                count = collections.Counter(current)
                num = 0
                for i, n in count.items():
                    if n % 2:
                        num += 1
                if num <= 1:
                    res += 1
                return
            dfs(node.left, current[:])
            dfs(node.right, current[:])
            current.pop()

        dfs(root, [])

        return res
