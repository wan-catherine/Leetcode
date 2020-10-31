import sys
"""
Key point : 
    In_order traverse BST
"""
from .Utility_Tree import TreeNode
class Solution(object):
    def recoverTree_dfs(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        first, second = None, None
        previous = TreeNode(-sys.maxsize)

        def dfs(node):
            nonlocal first, second, previous
            if not node:
                return
            dfs(node.left)
            if node.val >= previous.val:
                previous = node
            else:
                if not first:
                    first = previous
                    second = node
                    previous = node
                else:
                    second = node
                    return
            dfs(node.right)

        dfs(root)
        first.val, second.val = second.val, first.val

    def recoverTree(self, root):
        arr = [root]
        vals = [TreeNode(-2 ** 31 - 1)]
        visited = set()
        first, second = None, None
        while arr:
            node = arr[-1]
            if node.left and node.left not in visited:
                arr.append(node.left)
                continue
            if node.val < vals[-1].val:
                if not first:
                    first = vals[-1]
                    second = node   # need to set second here , or for test_recoverTree_1, it will failed for second is None
                else:
                    second = node
            vals.append(node)
            visited.add(node)
            arr.pop()
            if node.right and node.right not in visited:
                arr.append(node.right)
                continue
        first.val, second.val = second.val, first.val
