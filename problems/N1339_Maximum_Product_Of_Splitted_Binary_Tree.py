from .Utility_Tree import TreeNode
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.total = self.get_tree_sum(root)
        self.res = 0
        self.check(root)
        return self.res % (10**9+7) # only mod here, don't mod in the check funtion.

    def check(self, root):
        if root.left:
            self.res = max(self.res, (self.total-root.left.val)*root.left.val)
            self.check(root.left)
        if root.right:
            self.res = max(self.res, (self.total - root.right.val) * root.right.val)
            self.check(root.right)

    def get_tree_sum(self, node):
        if not node.left and not node.right:
            return node.val
        value = node.val
        if node.left:
            value += self.get_tree_sum(node.left)
        if node.right:
            value += self.get_tree_sum(node.right)
        node.val = value
        return value

