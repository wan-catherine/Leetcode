# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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