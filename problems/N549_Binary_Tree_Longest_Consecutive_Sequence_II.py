"""
549. Binary Tree Longest Consecutive Sequence II
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.res = 0
        def helper(node):
            down, up = 1, 1
            s, l = 0, 0
            if node.left:
                ls, ll = helper(node.left)
                if node.val + 1 == node.left.val:
                    down += ls
                    s = ls
                elif node.val == node.left.val + 1:
                    up += ll
                    l = ll
                self.res = max(self.res, ls, ll)
            if node.right:
                rs, rl = helper(node.right)
                if node.val + 1 == node.right.val:
                    up += rs
                    s = max(s, rs)
                if node.val == node.right.val + 1:
                    down += rl
                    l = max(l, rl)
                self.res = max(self.res, rs, rl)
            self.res = max(self.res, up, down)
            return s+1, l+1
        helper(root)
        return self.res