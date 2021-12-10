from .Utility_Tree import TreeNode

class Solution(object):
    def minCameraCover_(self, root):
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

    # return 0: node need to be covered
    # return 1: node has camera , covered by itself
    # return 2: node doesn't have camera, covered by its child
    def minCameraCover(self, root):
        res = 0
        def check(node):
            nonlocal res
            covered, camera = False, False
            if not node.left and not node.right:
                return 0
            if node.left:
                l = check(node.left)
                if l == 0:
                    covered, camera = True, True
                elif l == 1:
                    covered = True
            if node.right:
                r = check(node.right)
                if r == 0:
                    covered, camera = True, True
                elif r == 1:
                    covered = True
            if camera:
                res += 1
                return 1
            if covered:
                return 2
            return 0

        status = check(root)
        return res + (1 if status == 0 else 0)

    # update at 20211209
    def minCameraCover(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1
        res = 0

        def dfs(node):
            nonlocal res
            if not node.left and not node.right:
                return 0
            l, r = None, None
            if node.left:
                l = dfs(node.left)
            if node.right:
                r = dfs(node.right)
            if l == 0 or r == 0:
                res += 1
                return 2
            if l == 2 or r == 2:
                return 1
            return 0

        status = dfs(root)
        return res + (1 if status == 0 else 0)



