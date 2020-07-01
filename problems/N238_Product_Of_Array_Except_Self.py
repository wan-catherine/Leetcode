"""
use the prefix/suffix of the product of the array.

let's say res[i] = product(nums[:i]) * product(nums[i+1:])
product(nums[:i]) == prefix[i]
product(nums[i+1:]) == suffix[i+1]

Anther key point is to handle the index always in the [0, length-1]
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        length = len(nums)
        prefix = [nums[0]] * length
        suffix = [nums[-1]] * length

        for i in range(1, length):
            prefix[i] = nums[i] * prefix[i-1]
            if i <= length - 1:
                suffix[length - i - 1] = nums[length - i - 1] * suffix[length - i]

        res = [0] * length
        for i in range(length):
            left, right = 1, 1
            if i >= 1:
                left = prefix[i-1]
            if i < length - 1:
                right = suffix[i+1]
            res[i] = left * right
        return res


