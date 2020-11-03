from .Utility_Tree import TreeNode

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        covered = set({None})
        def dfs(node, parent):
            nonlocal res
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)

            if (not parent and node not in covered) or (node.left not in covered or node.right not in covered):
                res += 1
                covered.update({node, parent, node.right, node.left})
        dfs(root, None)
        return res


