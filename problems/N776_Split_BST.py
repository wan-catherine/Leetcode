class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return [None, None]
        if root.val == V:
            right = root.right
            root.right = None
            return [root, right]
        if root.val < V:
            left, right = self.splitBST(root.right, V)
            root.right = left
            return [root, right]
        if root.val > V:
            left, right = self.splitBST(root.left, V)
            root.left = right
            return [left, root]