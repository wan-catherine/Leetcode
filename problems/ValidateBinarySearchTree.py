# Definition for a binary tree node.
import sys
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #pre-order traversal tree and check the val is ordered by ascend
    def isValidBST_(self, root):
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

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def check(node):
            if not node:
                return True, None, None
            if not node.left and not node.right:
                return True, node.val, node.val

            l, lm, ln = check(node.left)
            r, rm, rn = check(node.right)

            if not l or not r:
                return False, None, None
            if lm != None and rm == None:
                if node.val > lm:
                    return True, node.val, ln
            elif rm != None and lm == None:
                if node.val < rn:
                    return True, rm, node.val
            else:
                if node.val > lm and node.val < rn:
                    return True, rm, ln
            return False, None, None

        res, _, _ = check(root)
        return res

    def isValidBST_20220614(self, root: Optional[TreeNode]) -> bool:

        def check(node, mx, mi):
            if not node:
                return True
            if node.val >= mx or node.val <= mi:
                return False
            l = check(node.left, node.val, mi)
            r = check(node.right, mx, node.val)
            return l and r

        return check(root, sys.maxsize, -sys.maxsize)
