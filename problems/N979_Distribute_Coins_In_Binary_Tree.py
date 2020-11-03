"""
Consider the flow on the edge .
for a node , how many coins does it have to make his left and right children balance?
if a child has more coins, it needs to move node.val - 1 to his parents , if a child has less than one coins,
it needs get some coins from his parent. 
"""
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def dfs(node, num):
            if not node:
                return 0
            left = dfs(node.left, num)
            right = dfs(node.right, num)
            num[0] += abs(left) + abs(right)
            return node.val - 1 + left + right

        dfs(root, res)
        return res[0]