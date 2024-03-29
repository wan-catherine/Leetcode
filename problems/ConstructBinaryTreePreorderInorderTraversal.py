# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root =self.helper(preorder,inorder)
        return root

    def helper(self, preorder, inorder):
        if preorder == None or len(preorder) == 0 or len(preorder) != len(inorder):
            return

        node = TreeNode(preorder[0])
        if(len(preorder) == 1):
            return node
        index = inorder.index(preorder[0])
        node.left = self.helper(preorder[1:index+1], inorder[:index])
        node.right = self.helper(preorder[index+1:], inorder[index+1:])

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        length = len(preorder)
        mapping = {inorder[i] : i for i in range(length)}
        def dfs(ps, pe, ins, ine):
            if ps > pe:
                return None
            root = TreeNode(preorder[ps])
            index = mapping[preorder[ps]]
            ll = index - index
            root.left = dfs(ps + 1, ps + ll, ins, ins + ll)
            root.right = dfs(ps + ll + 1, pe, index + 1, ine)
            return root
        dfs(0, length-1, 0, length-1)



