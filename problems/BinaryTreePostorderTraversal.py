# Definition for a binary tree node.
from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.helper(root, [])
    def helper(self, root, res):
        if root == None:
            return res
        if root.left != None:
            self.helper(root.left, res)
        if root.right != None:
            self.helper(root.right, res)
        res.append(root.val)
        return  res

    def postorderTraversal(self, root):
        if not root:
            return None

        stack = [root]
        res = []
        while stack:
            node = stack[-1]
            if not node.left and not node.right:
                res.append(node.val)
                stack.pop()
            if node.right:
                stack.append(node.right)
                node.right = None
            if node.left:
                stack.append(node.left)
                node.left = None
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]