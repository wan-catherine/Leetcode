from .Utility_Tree import TreeNode

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        def in_order(node):
            if not node:
                return
            if node.left:
                in_order(node.left)
            arr.append(node.val)
            if node.right:
                in_order(node.right)

        in_order(root)

        def create_tree(arr):
            if not arr:
                return None
            length = len(arr)
            if length == 1:
                return TreeNode(arr[0])
            index = (length-1)//2
            root = TreeNode(arr[index])
            root.left = create_tree(arr[:index])
            root.right = create_tree(arr[index+1:])
            return root

        return create_tree(arr)
