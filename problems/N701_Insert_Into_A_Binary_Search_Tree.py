from .Utility_Tree import TreeNode


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insert(node, val):
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)
        if not root:
            return TreeNode(val)
        insert(root, val)
        return root
