# 255. Verify Preorder Sequence in Binary Search Tree
# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Consider the following binary search tree:
#
#      5
#     / \
#    2   6
#   / \
#  1   3
#
# Example 1:
# Input: [5,2,6,1,3]
# Output: false
#
# Example 2:
# Input: [5,2,1,3,6]
# Output: true
# Follow up:
# Could you do it using only constant space complexity?
import sys


class Solution(object):
    def verifyPreorder_TLE(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        def dfs(start, end):
            if start >= end:
                return True
            root = preorder[start]
            index = start+1
            while index <= end and preorder[index] < root:
                index += 1
            for i in range(index, end+1):
                if preorder[i] < root:
                    return False
            return dfs(start+1, index-1) and dfs(index, end)
        return dfs(0, len(preorder)-1)

    # for every pair (a,b) and a < b, we need a < c for all c after b.
    def verifyPreorder(self, preorder):
        stack = []
        a_max = -sys.maxsize
        for n in preorder:
            if n < a_max:
                return False
            while stack and stack[-1] < n:
                a_max = max(a_max, stack.pop())
            stack.append(n)
        return True
