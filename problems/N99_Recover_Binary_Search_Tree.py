import sys
"""
Key point : 
    In_order traverse BST
"""
from .Utility_Tree import TreeNode
class Solution(object):
    def recoverTree(self, root):
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

