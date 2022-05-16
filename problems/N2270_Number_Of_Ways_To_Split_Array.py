from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        length = len(nums)
        total = sum(nums)
        prev = 0
        res = 0
        for i in range(length - 1):
            prev += nums[i]
            if prev >= total - prev:
                res += 1
        return res
