from .Utility_Tree import TreeNode
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        level = 1
        stack = [root]
        while level != d - 1:
            new_stack = []
            for node in stack:
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            level += 1
            stack = new_stack

        for node in stack:
            left, right = node.left, node.right
            node.left, node.right = TreeNode(v), TreeNode(v)
            node.left.left = left
            node.right.right = right
        return root


