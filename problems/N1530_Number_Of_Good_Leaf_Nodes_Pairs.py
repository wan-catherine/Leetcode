import collections


class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        res = 0
        def dfs(node):
            nonlocal res
            rnt = collections.defaultdict(int)
            if not node:
                rnt[0] = 0
                return rnt
            if not node.left and not node.right:
                rnt[0] = 1
                return rnt

            left = dfs(node.left)
            right = dfs(node.right)
            for dl, cl in left.items():
                for dr, cr in right.items():
                    if dl + dr + 2 <= distance:
                        res += cl*cr
            for i in range(distance):
                rnt[i+1] = left[i] + right[i]
            return rnt
        dfs(root)
        return res