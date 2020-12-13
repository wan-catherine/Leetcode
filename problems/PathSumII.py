# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum_(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        self.helper(root, sum, res, temp)
        return res

    def helper(self, node, sum, temp, res):
        if not node:
            return
        val = sum - node.val
        temp.append(node.val)
        if not node.right and not node.left and val == 0:
            res.append(temp[:])
            return
        if node.left:
            self.helper(node.left, val, temp[:], res)
        if node.right:
            self.helper(node.right, val, temp[:], res)

    def helper_before(self, root, sum, res, temp):
        if root == None:
            return
        if root.left == None and root.right == None:
            if root.val == sum:
                res.append(temp)
        temp.append(root.val)
        if root.left:
            self.helper(root.left, sum-root.val, res, temp.copy())
        if root.right:
            self.helper(root.right, sum-root.val, res, temp.copy())

    def pathSum(self, root: TreeNode, sum: int) :
        if not root:
            return []
        res = []

        def dfs(node, cur, ans):
            if not node.left and not node.right:
                if cur + node.val == sum:
                    ans.append(node.val)
                    res.append(ans)
                return
            new_ans = ans + [node.val]
            if node.left:
                dfs(node.left, cur + node.val, new_ans[:])
            if node.right:
                dfs(node.right, cur + node.val, new_ans[:])

        dfs(root, 0, [])
        return res