from math import inf

from .Utility_Tree import TreeNode

# the trick part of this problem is as a subtree you can only return the larger side , but as a result you can
# include both side add root
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float(-inf)
        return self.max_one_side(root, max_sum)[0]

    def max_one_side(self,root, max_sum):
        if not root:
            return max_sum, 0

        max_sum, right_sum = self.max_one_side(root.right, max_sum)
        right_sum = max(0, right_sum)
        max_sum, left_sum = self.max_one_side(root.left, max_sum)
        left_sum = max(0, left_sum)
        max_sum = max(max_sum, right_sum + left_sum + root.val)
        return max_sum, max(right_sum, left_sum) + root.val
