# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from .Utility_Tree import TreeNode

class BSTIterator(object):
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


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())