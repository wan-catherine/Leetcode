from .Utility_Tree import TreeNode

class Solution(object):
    def lowestCommonAncestor_TLE(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val == p or root.val == q:
            return root.val
        p_left, p_right = self.check(root.left, p), self.check(root.right, p)
        q_left, q_right = self.check(root.left, q), self.check(root.right, q)
        if (p_left and q_right) or (p_right and q_left):
            return root.val
        if p_left and q_left:
            return self.lowestCommonAncestor(root.left, p, q)
        if p_right and q_right:
            return self.lowestCommonAncestor(root.right, p, q)

    def check(self, node, num):
        if not node:
            return False
        if node.val == num:
            return True
        return self.check(node.left, num) or self.check(node.right, num)

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        if root.val == p or root.val == q:
            return root.val

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if right and left:
            return root.val
        if not right:
            return left
        if not left:
            return right


