# Definition for a binary tree node.
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees_before(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(1,n)


    def helper(self, before, end):
        res = []
        if before > end:
            return res
        for num in range(before, end + 1):
            leftList = self.helper(before, num-1)
            rightList = self.helper(num+1, end)
            if len(leftList) == 0 and len(rightList) == 0:
                root = TreeNode(num)
                res.append(root)
            elif len(leftList) == 0:
                for node in rightList:
                    root = TreeNode(num)
                    root.right = node
                    res.append(root)
            elif len(rightList) == 0:
                for node in leftList:
                    root = TreeNode(num)
                    root.left = node
                    res.append(root)
            else:
                for nleft in leftList:
                    for nright in rightList:
                        root = TreeNode(num)
                        root.left = nleft
                        root.right = nright
                        res.append(root)
        return res
