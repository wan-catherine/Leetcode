# Definition for a binary tree node.
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
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




    #     res = [None, [node1], [node2,node3]]
    #     i = 3
    #     while i <= n:
    #         temp = []
    #         for j in range(1,i+1):
    #             node = TreeNode(j)
    #             for treeleft in res[j-1]:
    #                 for treeright in res[i-j]:
    #                     node.left = self.copyTree(treeleft)
    #                     node.right = self.increaseTree(res,i,j)
    #             temp.append(node)
    #         res.append(temp)
    #     return res[-1]
    #
    # def copyTree(self, root):
    #     return copy.deepcopy(root)
    #
    # def increaseTree(self, res, i, j):
    #     if i == j:
    #         return None
    #     newTree = copy.deepcopy(res[i-j])
    #     stack = [newTree]
    #     while len(stack) > 0:
    #         node = stack[-1]
    #         if node.left != None:
    #             stack.append(node.left)
    #             node = node.left
    #             continue
    #         node.val += j
    #         stack.pop()
    #         if node.right != None:
    #             node = node.right
    #             stack.append(node)
    #             continue
    #     return newTree


