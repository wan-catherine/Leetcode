class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        res = [26]
        def dfs(node, current):
            nonlocal res
            if not node.left and not node.right:
                current.append(node.val)
                length = len(res)
                for i, n in enumerate(current[::-1]):
                    if i < length and n < res[i]:
                        res = current[::-1]
                        return
                    if i < length and n > res[i]:
                        return
                    if i >= length:
                        return
                res = current[::-1]
                return
            current.append(node.val)
            if node.left:
                dfs(node.left, current[:])
            if node.right:
                dfs(node.right, current[:])

        dfs(root, [])
        li = 'abcdefghijklmnopqrstuvwxyz'
        ans = []
        for i in res:
            ans.append(li[i])
        return ''.join(ans)