# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum_slow(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        res = root.val
        stack = [root]
        used = []
        while len(stack) > 0:
            node = stack[-1]
            if node.left != None and node.left not in used:
                res += node.left.val
                stack.append(node.left)
                continue
            if node.right != None and node.right not in used:
                res += node.right.val
                stack.append(node.right)
                continue

            if res == sum and node.right == None and node.left == None:
                return True
            else:
                node = stack.pop()
                res -= node.val
                used.append(node)
        return False

