class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        def helper(node, count):
            if not node:
                return count
            count += 1
            count = helper(node.left, count)
            count = helper(node.right, count)
            return count

        def find_node(root):
            if not root:
                return None
            if root.val == x:
                return root
            if root.val != x:
                l = find_node(root.left)
                r = find_node(root.right)
                return l if l else r

        node = find_node(root)
        left = helper(node.left, 0)
        right = helper(node.right, 0)
        other = n - left - right - 1
        li = sorted([left, right, other])
        if li[0]+li[1] < li[2]:
            return True
        return False
