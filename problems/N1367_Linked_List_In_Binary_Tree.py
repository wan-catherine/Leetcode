from .Utility import ListNode
from .Utility_Tree import TreeNode

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if self.check(head, root):
            return True
        if root:
            if self.isSubPath(head, root.left):
                return True
            if self.isSubPath(head, root.right):
                return True
        return False

    def check(self, list_node, tree_node):
        if not list_node:
            return True
        if not tree_node and list_node:
            return False
        if tree_node.val != list_node.val:
            return False
        if self.check(list_node.next, tree_node.left) or self.check(list_node.next, tree_node.right):
            return True
        return False
