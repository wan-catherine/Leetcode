"""
Find the next greater number --> Monotone stack , non-increasing stack.
Find the next smaller number --> Monotone stack, non-descreasing stack.
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        length = len(nums)
        if length == 1:
            return [-1]
        stack = []

        res = [-1] * length
        for i in range(length):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                res[index] = nums[i]
            stack.append(i)

        for i in range(stack[0] + 1):
            while nums[i] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[i]
        return res
