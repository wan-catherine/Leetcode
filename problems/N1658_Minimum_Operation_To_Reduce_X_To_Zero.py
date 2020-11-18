"""
If we don't check target == 0, we need to set longest = -1 or any number < 0.
If we check target == 0, we can set longest = 0.

We convert this problem to find the longest subarray which sum equals to sum(nums) - x.
Then we can use two pointer to find the subarray!!!
"""
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        # if not target:
        #     return len(nums)
        longest = -1
        length = len(nums)
        left, right, cur = 0, 0, 0
        while right < length:
            cur += nums[right]

            while cur > target and left <= right:
                cur -= nums[left]
                left += 1

            if cur == target:
                longest = max(longest, right - left + 1)
            right += 1
        return length - longest if longest != -1 else -1