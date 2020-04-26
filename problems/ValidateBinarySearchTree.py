# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #pre-order traversal tree and check the val is ordered by ascend
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        stack = [root]
        values = []
        while len(stack) > 0:
            node = stack[-1]
            if node.left!= None:
                stack.append(node.left)
                continue
            if len(values)>0 and node.val <= values[-1]:
                return False
            values.append(node.val)
            stack.pop()
            if node.right != None:
                node = node.right
                stack.append(node)
                continue

            #remove the compared subtrees to avoid duplicating
            if len(stack) > 0:
                if node == stack[-1].right:
                    stack[-1].right = None
                else:
                    stack[-1].left = None
        return True

    # pre-order traversal tree
    def isValidBST_20200426(self, root):
        if not root:
            return True
        stack = []
        value = float(-inf)
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                node = stack.pop()
                if value >= node.val:
                    return False
                    value = node.val
                current = node.right
            else:
                break
        return True

    #use the up and down limit to check
    def isValidBST_with_border(self, root):
        if not root:
            return True
        return self.isBST(root, float(-inf), float(inf))

    def isBST(self, root, min, max):
        if not root:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.isBST(root.left, min, root.val) and self.isBST(root.right, root.val, max)



