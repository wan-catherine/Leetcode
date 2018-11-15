# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root == None:
            return
        res.append(root.val)
        if root.left != None:
            self.helper(root.left, res)
        if root.right != None:
            self.helper(root.right, res)
