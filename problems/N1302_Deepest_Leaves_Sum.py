class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leaves = []
        def dfs(node, level):
            if not node.left and not node.right:
                leaves.append([node, level])
                return
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)
        res = 0
        leaves.sort(key=lambda item:item[1], reverse=True)
        mx = leaves[0][1]
        for node, level in leaves:
            if level != mx:
                break
            res += node.val
        return res