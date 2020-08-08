import collections

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
        if not root:
            return 0
        return self.count_(root, sum, {})

    def count_(self, node, sum, counter):
        res = 0
        if sum == node.val:
            res += 1
        if sum-node.val in counter:
            res += counter[sum-node.val]
        counter = {k + node.val:v for k,v in counter.items()}
        if node.val in counter:
            counter[node.val] += 1
        else:
            counter[node.val] = 1
        if node.left:
            res += self.count_(node.left, sum, counter)
        if node.right:
            res += self.count_(node.right, sum, counter)
        return res
