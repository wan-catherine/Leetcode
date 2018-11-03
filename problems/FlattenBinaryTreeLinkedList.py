# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None or (root.left == None and root.right == None):
            return
        res = [root.val]
        stack = [root]
        while len(stack) > 0:
            node = stack[-1]
            if node.left != None:
                node = node.left
                res.append(node.val)
                stack.append(node)
                continue
            stack.pop()
            if node.right != None:
                node = node.right
                res.append(node.val)
                stack.append(node)
                continue
            if len(stack) > 0:
                if node == stack[-1].right:
                    stack[-1].right = None
                else:
                    stack[-1].left = None
        root.val = res[0]
        node = root
        for i in res[1:]:
            node.right = TreeNode(i)
            node = node.right

