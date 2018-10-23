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
        while len(stack) > 0:
            temp = []
            for node in stack:
                temp.append(node.val)
                if node.left != None:
                    next.append(node.left)
                if node.right != None:
                    next.append(node.right)
            res.append(temp)
            stack = next
            next = []

        return res