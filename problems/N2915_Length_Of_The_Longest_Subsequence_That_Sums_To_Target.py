import sys
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums.sort()
        memo = {}

        def dp(index, total) :
            if (index, total) in memo:
                return memo[(index, total)]
            if total == 0:
                return 0
            if index == length or total < nums[index]:
                return -float("inf")
            res = max(1 + dp(index + 1, total - nums[index]), dp(index + 1, total))
            memo[(index, total)] = res
            return res

        res = dp(0, target)
        return res if res != -float("inf") else -1
