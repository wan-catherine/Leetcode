# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        stack = [root]
        next = []
        res = []
        while stack:
            level_nodes = []
            for node in stack:
                if not node:
                    continue
                level_nodes.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            res.append(level_nodes)
            stack = next
            next = []

        return res



