# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten_before(self, root):
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

    def flatten_(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        preorder = []
        self.helper(root, preorder)
        # print(preorder)
        root.left = None
        cur = root
        for val in preorder[1:]:
            cur.right = TreeNode(val)
            cur = cur.right

    def helper(self, node, arr):
        if not node:
            return
        arr.append(node.val)
        self.helper(node.left, arr)
        self.helper(node.right, arr)

    def flatten_recursive(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        def helper(node):
            if not node.left and not node.right:
                return (node, node)
            end = node
            right = node.right
            if node.left:
                ls, le = helper(node.left)
                node.right = ls
                end = le
                node.left = None
            if right:
                rs, re = helper(right)
                end.right = rs
                end = re
            return (node, end)

        helper(root)

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        left,right = root.left, root.right
        root.left = None
        root.right = left
        while root.right:
            root = root.right
        root.right = right




