from .Utility_Tree import TreeNode
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        if not root or root.val < val:
            new_node.left = root
            return new_node

        node = root
        previous = None
        while node:
            if node.val > val:
                if node.right:
                    previous = node
                    node = node.right
                else:
                    node.right = new_node
                    break
            else:
                new_node.left = node
                previous.right = new_node
                break
        return root

