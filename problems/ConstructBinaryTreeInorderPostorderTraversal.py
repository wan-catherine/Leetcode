# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root = self.helper(inorder, postorder)
        return root

    def helper(self, inorder, postorder):
        if postorder == None or len(postorder) == 0 or len(inorder) != len(postorder):
            return

        node = TreeNode(postorder[-1])
        if (len(postorder) == 1):
            return node
        index = inorder.index(postorder[-1])
        node.left = self.helper(inorder[0:index], postorder[0:index])
        node.right = self.helper(inorder[index + 1:], postorder[index:-1])

        return node