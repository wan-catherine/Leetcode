from .Utility_Tree import TreeNode

class Solution(object):
    def bstFromPreorder(self, order):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        if not order:
            return None
        root = TreeNode(order[0])
        order_len = len(order)
        has_right = False
        if order_len > 1:
            for i in range(1,order_len):
                if order[i] > root.val:
                    has_right = True
                    break

            if has_right:
                root.left = self.bstFromPreorder(order[1:i])
                root.right = self.bstFromPreorder(order[i:])
            else:
                root.left = self.bstFromPreorder(order[1:])
        return root


