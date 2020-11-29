class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        length = len(nums)
        stack = []
        for i, n in enumerate(nums):
            while stack and nums[stack[-1]] > n:
                if k - len(stack) > length - i - 1:
                    break
                stack.pop()
            if len(stack) < k:
                stack.append(i)
        return [nums[i] for i in stack]