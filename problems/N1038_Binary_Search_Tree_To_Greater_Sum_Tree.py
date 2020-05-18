from .Utility_Tree import TreeNode, null

class Solution:
    def bstToGst_recurse(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.inorder(root)
        return root

    def inorder(self, root):
        if not root:
            return
        if root.right:
            self.inorder(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.inorder(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        pass



