# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from .Utility_Tree import TreeNode

class BSTIterator_List(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.res = []
        def helper(root):
            if not root.left and not root.right:
                self.res.append(root.val)
                return
            if root.left:
                helper(root.left)
            self.res.append(root.val)
            if root.right:
                helper(root.right)
        if root:
            helper(root)
            self.length = len(self.res)
            self.index = 0
        else:
            self.length = 0
            self.index = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index >= self.length:
            return False
        return True

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            ans = self.res[self.index]
            self.index += 1
            return ans

"""
This way we can implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree. 
Because all nodes will not be visited than twice. 
first, we add it into self.stack, second we will return its val. So average will be O(1). 
It's actually a way to do loop in-order traverse. 
"""
class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        if not self.hasNext():
            return
        node = self.stack.pop()
        self.push_left(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())