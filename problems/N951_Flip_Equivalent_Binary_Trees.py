class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        left_no_flip = self.flipEquiv(root1.left, root2.left)
        right_no_flip = self.flipEquiv(root1.right, root2.right)
        if left_no_flip and right_no_flip:
            return True
        left_flip = self.flipEquiv(root1.left, root2.right)
        right_flip = self.flipEquiv(root1.right, root2.left)
        if left_flip and right_flip:
            return True

        return False
