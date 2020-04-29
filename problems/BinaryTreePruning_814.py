from .Utility_Tree import TreeNode

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root :
            return None

        root.right = self.pruneTree(root.right)
        root.left = self.pruneTree(root.left)

        if not root.left and not root.right and not root.val:
            return None
        return root