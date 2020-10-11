"""
All tree problems, first to consider recursive method.
This one is first check its children, then itself.
So it kinds of post-order problem. We recursively check its children, then check itself.
"""
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        if not root:
            return None
        if not root.left and not root.right and root.val == target:
            return None
        return root





