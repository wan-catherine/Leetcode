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

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(n, node, arr):
            if node == n:
                arr.append(node)
                return True
            if node == None:
                return False
            if dfs(n, node.left, arr) or dfs(n, node.right, arr):
                arr.append(node)
                return True
            return False
        parr, qarr = [], []
        dfs(p, root, parr)
        dfs(q, root, qarr)
        lp, lq = len(parr), len(qarr)
        i, j = lp - 1, lq - 1
        while i >= 0 and j >= 0:
            if parr[i] == qarr[j]:
                i -= 1
                j -= 1
            else:
                break
        if i >= 0:
            return parr[i+1]
        return qarr[j+1]



