import collections
"""
666. Path Sum IV
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

It's guaranteed that the given list represents a valid connected binary tree.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
 

Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        mapping = collections.defaultdict(dict)
        for num in nums:
            h, p, v = num // 100, num%100//10, num%10
            mapping[h][p] = v

        # def create_tree(h,p):
        #     node = TreeNode(mapping[h][p])
        #     if h+1 not in mapping:
        #         return node
        #     if 2*p-1 in mapping[h+1]:
        #         node.left = create_tree(h+1, 2*p-1)
        #     if 2*p in mapping[h+1]:
        #         node.right = create_tree(h+1, 2*p)
        #     return node
        # root = create_tree(1, 1)
        #
        # self.res = 0
        # def get_sum(node, cur):
        #     if not node.left and not node.right:
        #         self.res += cur + node.val
        #         return
        #     cur += node.val
        #     if node.left:
        #         get_sum(node.left, cur)
        #     if node.right:
        #         get_sum(node.right, cur)
        # get_sum(root, 0)
        # return self.res
        self.res = 0
        def dfs(h,p,cur):
            cur += mapping[h][p]
            if h+1 not in mapping or (2*p-1 not in mapping[h+1] and 2*p not in mapping[h+1]):
                self.res += cur
                return
            if 2*p-1 in mapping[h+1]:
                dfs(h+1, 2*p-1, cur)
            if 2*p in mapping[h+1]:
                dfs(h+1, 2*p, cur)
        dfs(1,1,0)
        return self.res

