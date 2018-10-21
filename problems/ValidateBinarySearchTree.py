# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
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
                node = node.left
                continue
            if len(values)>0 and node.val <= values[-1]:
                return False
            values.append(node.val)
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
        return True
