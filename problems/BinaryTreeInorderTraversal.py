# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal_before(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        stack = [root]
        while len(stack) > 0:
            node = stack[-1]
            if node.left != None:
                node = node.left
                stack.append(node)
                continue
            res.append(node.val)
            stack.pop()
            if node.right != None:
                node = node.right
                stack.append(node)
                continue

            if len(stack) > 0:
                if node == stack[-1].right:
                    stack[-1].right = None
                else:
                    stack[-1].left = None
        return res

    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = deque()
        stack.append(root)
        while stack:
            node = stack[-1]
            if node.left:
                stack.append(node.left)
                node.left = None
            else:
                res.append(node.val)
                stack.pop()
                if node.right:
                    stack.append(node.right)
                    node.right = None
        return res
