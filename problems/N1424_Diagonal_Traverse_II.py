import collections
"""
For diagonal , the key point is row+col always the same.
"""

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if not nums or not nums[0]:
            return []

        rows = len(nums)

        res = []
        diagon = collections.defaultdict(list)
        for row in range(rows):
            for col in range(len(nums[row])):
                diagon[row+col].append(nums[row][col])

        for i in range(len(diagon)):
            res.extend(diagon[i][::-1])
        return res


