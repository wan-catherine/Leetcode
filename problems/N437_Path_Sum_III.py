from .Utility_Tree import TreeNode

class Solution(object):
    def pathSum_recursive(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.count(root, sum) + self.pathSum(root.right, sum) + self.pathSum(root.left, sum)

    def count(self, root, sum):
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        if root.left:
            res += self.count(root.left, sum-root.val)
        if root.right:
            res += self.count(root.right, sum-root.val)
        return res

    def pathSum(self, root, sum):
        pass